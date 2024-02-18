"""
Python module for easier handling of the generalized
susceptibility matrices generated from
'w2dynamics' DMFT calculations
"""

import numpy as np
import scipy as sp
import scipy.integrate as integ
import h5py
import re
import matplotlib as mpl



####################################################################################################################################
######################################### Class to handle Generalized Susceptibilities #############################################
####################################################################################################################################

#TODO:
# - docstrings

class read(object):
    def __init__(self, file, iter=-1):
        self.file = file
        self.iter = iter
        self.iter_str = self.get_iter()

    def get(self, string):
        f = h5py.File(self.file,"r")
        data = f[string]
        return data

    def get_iter(self, twp=False):
        if self.iter==-1:
            iterpat = re.compile(r"^(?:dmft-last|stat-001|worm-001)+$")
            f = h5py.File(self.file,"r")
            iters = sorted([k for k in f.keys() if iterpat.match(k)])
            return iters[0]
        else:
            iterpat = re.compile(r"^(?:dmft|stat|worm)-\d+$")
            f = h5py.File(self.file,"r") 
            iters = sorted([k for k in f.keys() if iterpat.match(k)])
            max_iter = len(iters)
            try:
                iter = iters[self.iter-1]
            except IndexError:
                raise IndexError(f"Iteration index is too large, max iteration: {max_iter}")
            return iters[self.iter-1]

    @property
    def beta(self):
        beta = self.get(".config").attrs["general.beta"]
        return beta

    def U(self, atom=1):
        U = self.get(".config").attrs["atoms."+str(atom)+".udd"]
        return U

    @property
    def mu(self):
        try:
            strg = self.iter_str+"/mu/value"
            mu = self.get(strg)[()]
        except KeyError:
            mu = self.get(".config").attrs["general.mu"]
        
        return mu

    def occ(self, atom=1):
        strg = self.iter_str+"/ineq-"+str(atom).zfill(3)
        occ = np.array(self.get(strg+"/occ/value"))
        return occ

    def magn(self, atom=1):
        """
        n_up - n_down
        """
        occ = self.occ(atom)
        magn = occ[:,0,:,0] - occ[:,1,:,1]
        return magn

    @property
    def iw(self):
        return self.get(".axes/iw")[:]

    def giw(self, atom=1, worm=False):
        if worm:
            gf_strg = "glocnew"
        else:
            gf_strg = "giw"
        strg = self.iter_str+"/ineq-"+str(atom).zfill(3)
        giw = np.array(self.get(strg+f"/{gf_strg}/value"))
        return giw

    def g0iw(self, atom=1):
        strg = self.iter_str+"/ineq-"+str(atom).zfill(3)
        g0iw = np.array(self.get(strg+"/g0iw/value"))
        return g0iw

    def siw(self, atom=1, worm=False):
        if worm:
            g0iw = self.g0iw(atom)
            giw = self.giw(atom=atom, worm=worm)
            shape = g0iw.shape
            siw = np.empty(shape, dtype=complex)
            for i in range(shape[0]):
                for j in range(shape[1]):
                    siw[i,j,:] = 1/g0iw[i,j,:] - 1/giw[i,j,:]
        else:
            strg = self.iter_str+"/ineq-"+str(atom).zfill(3)
            siw = np.array(self.get(strg+"/siw/value"))
        return siw
    
    def fiw(self, atom=1):
        strg = self.iter_str+"/ineq-"+str(atom).zfill(3)
        fiw = np.array(self.get(strg+"/fiw/value"))
        return fiw
     
    def gkiw(self, ek, biw=0, atom=1, worm=False):
        """ Computes k-dependent GF G_k(v+w) """
        kdim = np.ones(ek.ndim,dtype=int)
        mu = self.mu
        if biw==0:
            iw = 1j*np.array(self.get(".axes/iw"))
            iw = iw.reshape(1,1,-1,*kdim)
            siw = self.siw(atom=atom, worm=worm)
        else:
            if np.abs(biw) > len(self.iw)//2:
                raise ValueError(f"Bosonic Matsubara index exceeds number of fermionic frequencies, " \
                                 + f"number of fermionic freqencies: {len(self.iw)//2}")
            iW = 1j*2*np.pi*biw / self.beta
            iw = 1j*np.array(self.get(".axes/iw"))[abs(biw):-abs(biw)]+iW
            iw = iw.reshape(1,1,-1,*kdim)
            if biw>0:
                siw = self.siw(atom=atom, worm=worm)[:,:,2*biw:]
            else:
                siw = self.siw(atom=atom, worm=worm)[:,:,:-2*abs(biw)]
        gkiw = 1/(iw + mu -ek.reshape(1,1,1,*ek.shape) \
                    - siw.reshape(*siw.shape,*kdim))
        return gkiw

    def bubble(self, niw4f=None, biw=0, iw4f=True, norbs=[0,0], 
               para=True, transv=False, atom=1, worm=False):
        """ Compute local bubble chi_loc(v+w) """
        # extract local greens function from hdf5 file
        gloc = self.giw(worm=worm)

        # trim fermionic freq grid for finite omega
        if biw==0:
            giw = gloc
            giw_o = gloc
        else:
            if np.abs(biw) > len(self.iw)//2:
                raise ValueError(f"Bosonic Matsubara index exceeds number of fermionic frequencies, " \
                                 + f"number of fermionic freqencies: {len(self.iw)//2}")    

            if biw>0:
                giw = gloc[:,:,biw:-biw]
                giw_o = gloc[:,:,2*biw:]
            else:
                giw = gloc[:,:,abs(biw):-abs(biw)]
                giw_o = gloc[:,:,:-2*abs(biw)]
        
        # trim fermionic freq grid according to 2P grid
        if iw4f:
            g4iw  = self.g4iw(atom=atom, worm=worm)
            niw = giw.shape[-1]
            niw4f = niw4f or g4iw.shape[-2]
            i_start = (niw-niw4f)//2
            iw4f_slice = slice(i_start, i_start+niw4f)
            giw = giw[..., iw4f_slice]
            giw_o = giw_o[..., iw4f_slice]

        #orbital indices
        o1 = norbs[0]
        o2 = norbs[1]
        try:
            giw = giw[o1,...]
            giw_o = giw_o[o2,...]
        except IndexError:
            raise IndexError(f"Orbital indices are too large, this object has {giw.shape[0]} orbitals")

        # for transversal channel flip spin indices of second GF
        if transv:
            giw_o = giw_o[::-1, ...]
        
        # consider SU(2) broken case as well -> chi0_up,down
        if para:
            return - self.beta*(giw*giw_o)[0,:]
        else:
            return - self.beta*np.array(
                [(giw*giw_o)[0,:],(giw*giw_o)[1,:]])
    
    def bubble_q(self, ek, ekq, niw4f=None, biw=0, norbs=[0,0], 
                 iw4f=True, para=True, transv=False, atom=1, worm=False):
        """ Compute q-dependent bubble chi_q(v+w) """
        sum_ax = np.arange(-ek.ndim,0,dtype=int)
        # extract lattice GF
        gk = self.gkiw(ek, biw=0, worm=worm)

        # trim fermionic freq grid for finite omega
        if biw==0:
            giw = gk
        else:    
            if np.abs(biw) > len(self.iw)//2:
                raise ValueError(f"Bosonic Matsubara index exceeds number of fermionic frequencies, " \
                                 + f"number of fermionic freqencies: {len(self.iw)//2}")
            giw = gk[:,:,abs(biw):-abs(biw),:,:]
        giw_q = self.gkiw(ekq, biw=biw, worm=worm)

        # trim fermionic freq grid according to 2P grid
        if iw4f:
            g4iw  = self.g4iw(atom=atom, worm=worm)
            niw = giw.shape[2]
            niw4f = niw4f or g4iw.shape[-2]
            i_start = (niw-niw4f)//2
            iw4f_slice = slice(i_start, i_start+niw4f)
            giw = giw[:, :, iw4f_slice,:]
            giw_q = giw_q[:, :, iw4f_slice,:]

        #orbital indices
        o1 = norbs[0]
        o2 = norbs[1]
        try:
            giw = giw[o1,...]
            giw_q = giw_q[o2,...]
        except IndexError:
            raise IndexError(f"Orbital indices are too large, this object has {giw.shape[0]} orbitals")

        # for transversal channel flip spin indices of second GF
        if transv:
            giw_q = giw_q[::-1,...]

        # consider SU(2) broken case
        if para:
            return (- self.beta*np.sum(giw*giw_q,axis=tuple(sum_ax))/ek.size)[0,...]
        else :
            return -self.beta*np.array(
                [(np.sum(giw*giw_q,axis=tuple(sum_ax))/ek.size)[0,...],
                 (np.sum(giw*giw_q,axis=tuple(sum_ax))/ek.size)[1,...]])

    def g4iw(self, norb=1, atom=1, worm=False):
        strg = self.iter_str+"/ineq-"+str(atom).zfill(3)
        if worm:
            f = h5py.File(self.file,"r")
            g4_all_components = compose_g4iw_worm(f[strg], self.beta, norb)
            spins = g4_all_components.shape[1]
            niw4f = g4_all_components.shape[-2]
            niw4b = g4_all_components.shape[-1]
            g4iw = np.zeros([norb, spins, norb, spins, niw4f, niw4f, niw4b], dtype=complex)
            for o1 in range(norb):
                for s1 in range(spins):
                    for o2 in range(norb):
                        for s2 in range(spins):
                            g4iw[o1,s1,o2,s2,...] = g4_all_components[o1,s1,o1,s1,o2,s2,o2,s2,...]
            return g4iw

        else:
            g4iw = np.array(self.get(strg+"/g4iw/value"))
            return g4iw

    def g4iw_bar_worm(self, atom=1):
        strg = self.iter_str+"/ineq-"+str(atom).zfill(3)
        g4iw_barud = np.array(self.get(strg+"/g4iw-worm/00007/value")) #     uddu
        g4iw_bardu = np.array(self.get(strg+"/g4iw-worm/00010/value")) #     duud
        g4iw_bar = np.zeros((1,2,1,2,*g4iw_barud.shape),dtype=complex)
        g4iw_bar[0,0,0,0,:] = g4iw_barud
        g4iw_bar[0,1,0,1,:] = g4iw_bardu
        return g4iw_bar

    def g4iw_pp(self, norb=1, atom=1, worm=False):
        strg = self.iter_str+"/ineq-"+str(atom).zfill(3)
        if worm:
            with h5py.File(self.file,"r") as f:
                g4_all_components = compose_g4iw_worm(f[strg], self.beta, norb, channel="pp")
            spins = g4_all_components.shape[1]
            niw4f = g4_all_components.shape[-2]
            niw4b = g4_all_components.shape[-1]
            g4iw = np.zeros([norb, spins, norb, spins, niw4f, niw4f, niw4b], dtype=complex)
            for o1 in range(norb):
                for s1 in range(spins):
                    for o2 in range(norb):
                        for s2 in range(spins):
                            g4iw[o1,s1,o2,s2,...] = g4_all_components[o1,s1,o1,s1,o2,s2,o2,s2,...]
            return g4iw
        else:
            g4iw_pp = np.array(self.get(strg+"/g4iw-pp/value"))
            return g4iw_pp
    
    def chi_ph(self, biw=0, norb=1, norbs=[0,0], atom=1, worm=False):
        def get_ggstraight_ph(giw, niw4f):
            """ taken from w2dyn/auxilaries/postporcessing.py
            Helper function for getting the straight part from GG
            The "straight" disconnected part of the two-particle Green's function is
            given by:
            GG_AB(iv, iv', iw) = G_A(iv) G_B(iv') delta(iw,0)
            and is returned as six-dimensional array GG(A,B,iv,iv'), omitting the
            bosonic frequency for brevity.
            """
            nband, nspin, niw = giw.shape
            startidx = (niw-niw4f)//2
            iw4f_slice = slice(startidx, startidx+niw4f)
            giw = giw.reshape(-1, niw)[:, iw4f_slice]
            gg_straight = np.tensordot(giw, giw, ((),()))  # i,iv,j,iv'
            gg_straight = gg_straight.transpose(0, 2, 1, 3)
            return gg_straight.reshape(nband, nspin, nband, nspin, niw4f, niw4f) 

        giw = self.giw(atom=atom, worm=worm)
        try:
            g4iw  = self.g4iw(worm=worm, norb=norb) 
        except KeyError:
            raise KeyError("No 2p-GF found, this file contains one-particle data only")

        iw4b0 = g4iw.shape[-1]//2
        chi = g4iw.copy()
        chi[..., iw4b0] -= get_ggstraight_ph(giw, g4iw.shape[-2])
        chi *= self.beta

        iw4b = iw4b0 + biw
        o1 = norbs[0]
        o2 = norbs[1]
        try:
            giw = giw[o1,...]
        except IndexError:
            raise IndexError(f"Orbital indices are too large, this object has {giw.shape[0]} orbitals")
        
        susc = susz(self.beta, self.U(atom), self.mu,
                            chi[o1,0,o2,0,...,iw4b],
                            chi[o1,0,o2,1,...,iw4b],
                            chi[o1,1,o2,1,...,iw4b],
                            chi[o1,1,o2,0,...,iw4b])

        return susc

    def chi_ph_bar(self, other_giw=None, atom=1):
        try:
            g4iw  = self.g4iw_bar_worm(atom=atom) 
        except KeyError:
            raise KeyError("No 2p-GF found, this file contains one-particle data only")

        iw4b0 = g4iw.shape[-1]//2
        chi = g4iw.copy()
        chi *= self.beta
        return chi

    def chi_pp(self, other_giw=None, biw=0, norb=1, norbs=[0,0], atom=1, worm=False):
        """ taken from w2dyn/auxilaries/postporcessing.py
        generalised susceptibility (particle-particle channel)
        """
        def get_ggstraight_pp(giw, g4iw_pp_shape):
            """ taken from w2dyn/auxilaries/postporcessing.py
            Computes GG = G(iv)G(iv')delta(iw',-iv-iv')
            """
            #print giw.shape, g4iw_pp_shape
            assert giw.shape[-3:] == g4iw_pp_shape[-5:-2], "Shape mismatch"
            dotnot = ((),())
            nneq = g4iw_pp_shape[0]
            N = g4iw_pp_shape[-3]
            K = g4iw_pp_shape[-1]
            KhpNm1 = + K//2 - N + 1
            # TODO slow
            chi0_pp = np.zeros(shape=g4iw_pp_shape, dtype=complex)
            #chi0_pp[...] = np.nan
            for m in range(N):
                for n in range(N):
                    ktarg = KhpNm1 + m + n
                    if 0 <= ktarg < K:
                        chi0_pp[...,m,n,ktarg] = \
                                   np.tensordot(giw[...,m], giw[...,n], dotnot)
            return chi0_pp

        giw = self.giw(atom=atom, worm=worm) if other_giw is None else other_giw
        try:
            g4iw_pp  = self.g4iw_pp(norb=norb, atom=atom, worm=worm) 
        except KeyError:
            raise KeyError("No 2p-GF found, this file contains one-particle data only")
        
        iw4st = (giw.shape[-1] - g4iw_pp.shape[-2])//2
        iw4sl = slice(iw4st, -iw4st)
        chi0_pp = get_ggstraight_pp(giw[...,iw4sl], g4iw_pp.shape)
        chi = self.beta * (g4iw_pp - chi0_pp)

        iw4b = g4iw_pp.shape[-1]//2 + biw
        o1 = norbs[0]
        o2 = norbs[1]
        try:
            giw = giw[o1,...]
        except IndexError:
            raise IndexError(f"Orbital indices are too large, this object has {giw.shape[0]} orbitals")
        susc = susz(self.beta, self.U(atom), self.mu,
                        chi[o1,0,o2,0,...,iw4b],
                        chi[o1,0,o2,1,...,iw4b],
                        chi[o1,1,o2,1,...,iw4b],
                        chi[o1,1,o2,0,...,iw4b])

        return susc

    def chi_loc_phys(self, num_w, atom=1):
        """
        Calculates tuple of local, physical Xs, Xc

        Parameters:
        ---------------
        num_w: int
            Corresponds to the num_w-th bosonic Matsubara frequency, where iOmega_n
            ranges from -num_w to num_w
        atom: int (optional), default:atom=1
            Defines the impurity site

        Returns:
        ---------------
        Tuple with following entries:
        chi_c: (niw), ndarray
            Local, physical charge susceptibility as a function of bosonic iw
        chi_s: (niw), ndarray
            Local, physical spin susceptibility as a function of bosonic iw
        """

        # extract data
        strg = self.iter_str+"/ineq-"+str(atom).zfill(3)
        dat_ntn0 = np.array(self.get(strg+"/ntau-n0/value"))
        dat_tausus = np.array(self.get(".axes/tausus"))
        dat_occ =  np.array(self.get(strg+"/occ/value"))
        occ = dat_occ[0,0,0,0] + dat_occ[0,1,0,1]
        magn = dat_occ[0,0,0,0] - dat_occ[0,1,0,1]
        dtau = dat_tausus[1] - dat_tausus[0]
        print('# delta_tau =', dtau)

        # compute spin and charge susz
        w = [2*np.pi/self.beta * ni for ni in np.arange(-num_w, num_w+1)]
        chi_phys_charge = []
        chi_phys_spin = []
        for wi in w:
            e = np.exp(1j*wi*dat_tausus)
            if wi==0:
                chi_tau_charge = dat_ntn0[0,1,0,1,:] + dat_ntn0[0,1,0,0,:] + dat_ntn0[0,0,0,1,:] + dat_ntn0[0,0,0,0,:] - occ**2
                chi_tau_magn = dat_ntn0[0,1,0,1,:] - dat_ntn0[0,1,0,0,:] - dat_ntn0[0,0,0,1,:] + dat_ntn0[0,0,0,0,:] - magn**2
            else:
                chi_tau_charge = e*(dat_ntn0[0,1,0,1,:] + dat_ntn0[0,1,0,0,:] + dat_ntn0[0,0,0,1,:] + dat_ntn0[0,0,0,0,:])
                chi_tau_magn = e*(dat_ntn0[0,1,0,1,:] - dat_ntn0[0,1,0,0,:] - dat_ntn0[0,0,0,1,:] + dat_ntn0[0,0,0,0,:])
            chi_phys_charge.append(1/2.*integ.simps(chi_tau_charge, dx = dtau))
            chi_phys_spin.append(1/2.*integ.simps(chi_tau_magn, dx = dtau))
        
        return  np.array(chi_phys_charge), np.array(chi_phys_spin)

    def bse_ph(self, ek, ekq, r, biw=0, atom=1, worm=False):
        """ 
        Computes q-dependent generalized c/s susceptibility chi_r(q,w) by solving the BSE 

        Parameters:
        ----------------
        ek : (..., Nk, Nk) array_like
            Dispersion relation of given lattice
        ekq : (..., Nk, Nk) array_like
            Dispersion relation of given lattice shifted by momentum q
        r: {"c", "s"}
            Definition of channel, i.e. charge - 'c' or spin - 's'
        biw: int (optional), default: biw=0
            index n of bosonic Matsubara frequency iw_n
        worm: bool (optional), default: worm=False
            indicates whether the 2P-data was obtained with state or worm sampling

        Returns:
        ----------------
        chi_q: (niv, niv) ndarray
            q-dependent lattice susceptibility in channel r=c/s

        """
        # bubble susceptibilities
        chi0_loc = np.diag(self.bubble(biw=biw, atom=atom, worm=worm))
        chi0_q = np.diag(self.bubble_q(ek, ekq, biw=biw, atom=atom, worm=worm))

        # extract generalized local susceptibility chi_r
        if r=="c":
            chi_r = self.chi_ph(biw=biw, atom=atom, worm=worm).c
        elif r=="s":
            chi_r = self.chi_ph(biw=biw, atom=atom, worm=worm).s
        else:
            raise ValueError("Incorrect susceptibility was specified, options are c - Charge, s - Spin")

        # generalized charge susc via BSE
        chi_q = np.linalg.inv( np.linalg.inv(chi_r) \
            + np.linalg.inv(chi0_q) - np.linalg.inv(chi0_loc) )

        return chi_q
    


class susz(object):
    def __init__(self,beta,U,mu,uu,ud,dd,du):
        assert uu.shape == ud.shape == dd.shape == du.shape \
            ,"shape of spin components must be equal"
        assert uu.ndim == 2, "dimension 2 for spin components expected"
        self.beta   = float(beta)
        self.U      = float(U)
        self.mu      = float(mu)
        self.Niwf   = int(uu.shape[0]//2) 
        self.uu     = np.array(uu)
        self.ud     = np.array(ud)
        self.dd     = np.array(dd)
        self.du     = np.array(du)
        self.c     = 0.5 * (self.uu + self.dd + self.ud + self.du)
        self.s     = 0.5 * (self.uu + self.dd - self.ud - self.du)
        self.sc    = 0.5 * (self.uu - self.dd + self.ud - self.du)
        self.cs    = 0.5 * (self.uu - self.dd - self.ud + self.du)
        self.matrix = np.vstack(( np.hstack((self.uu, self.ud)),  
                                  np.hstack((self.du,self.dd)) )) 
        
        self.cs_matrix = np.vstack(( np.hstack((self.s, self.sc)),  
                                     np.hstack((self.cs,self.c)) )) 
        self.nu = np.linspace(-(2*(self.Niwf-1)+1)*np.pi/self.beta,\
                                  (2*(self.Niwf-1)+1)*np.pi/self.beta,num=2*self.Niwf)
        








####################################################################################################################################
##################################### Class and functions to handle worm-sampled 2p GF #############################################
####################################################################################################################################

#functions
# from w2dyn.auxiliaries.compoundIndex
class GFComponent:
    """ Class for indexing green's functions.
    An instance of GFComponent holds the following fields:
    *** index: compound index of all indices (one-based single number)
    *** bands: band indices (zero-based list)
    *** spins: spin indices (zero-based list)
    *** bandspin: band-spin compound indices
    *** n_bands: number of impurity orbitals
    *** n_ops: number of operators in Greens function
             2 -> 1-particle Green's function
             4 -> 2-particle Green's function"""


    def __init__(self, index=None,
                 bands=None, spins=None, bandspin=None,
                 n_bands=0, n_ops=0, n_spins=2):

        if n_bands == 0 or n_ops == 0:
            raise ValueError('n_bands and n_ops have to be set'
                             ' to non-zero positive integers')

        self.n_bands = n_bands
        self.n_ops = n_ops
        dims_bs = n_ops * (n_bands*n_spins,)
        dims_1 = (n_bands, n_spins)

        # initialize from compound index
        if index is not None and bands is None:  
            self.index = index
            self.bandspin = list(np.unravel_index(self.index-1, dims_bs))
            self.bands, self.spins = np.unravel_index(self.bandspin, dims_1)

         # initialize from bands (and spins)
        elif bands is not None and index is None: 
            self.bands = bands
            if spins is None:  # use only band indices (e.g. d/m channel)
                self.spins = n_ops * (0,)
            else:
                self.spins = spins

            self.bandspin = np.ravel_multi_index(
                (self.bands, self.spins), (n_bands, n_spins))
            self.index = np.ravel_multi_index(self.bandspin, dims_bs) + 1

        elif bandspin is not None and index is None:
            self.index = np.ravel_multi_index(bandspin, dims_bs) + 1

        else:
            raise ValueError('index and bands both supplied')

    def bsbs(self):
        bsbs = np.vstack((self.bands, self.spins)).transpose().reshape(-1)
        return tuple(bsbs)

def component2index_general(Nbands, N, b, s):
    """ converting a band-spin pattern into an index
    :param N: number of operators
    :param b: band array of length N
    :param s: spin array of length N
    :return index: general flavor index"""
      
    comp = GFComponent(n_bands=Nbands, n_ops=N, bands=b, spins=s)
     
    return comp.index

# adaption of w2dyn_g4iw_worm_to_triqs_block2gf
def compose_g4iw_worm(g4iw, beta, norb, channel="ph", qtype="value"):
    """Converts a dictionary mapping zero-padded five digits long string
    representations of compound indices to components of the
    two-particle Green's function as ndarrays with two fermionic
    frequency indices nu, nu' and one bosonic frequency index omega in
    the order [nu, nu', omega], as produced by w2dynamics, into one 
    single array with indices [o, s, o, s, o, s, o, s, nu, nu', omega].
    Missing components are filled with zeros.

    Takes:
    g4iw : mapping from compound indices to components of the two-particle
           Green's function
    beta : inverse temperature
    norb : number of orbitals
    qtype : type/statistic of quantity to extract (value, error)

    Returns:
    np.ndarray : two-particle Green's function with one bosonic and two
                 fermionic frequencies

    Author: Alexander Kowalski (2019) """

    # modify directory string according to ph/pp channel
    if channel=="ph": 
        strg = "g4iw-worm"
    elif channel=="pp":
        strg = "g4iwpp-worm"
    else:
        raise ValueError("Wrong channel specified, options are: {ph, pp}")

    # get number of positive freqs from a component of the result
    for i in range(100000):
        try:
            arr = g4iw[f"{strg}/{i:05}"][qtype][()]
            n4iwf, n4iwf_check, n4iwb = arr.shape
            assert(n4iwf == n4iwf_check)
            n4iwf, n4iwb = n4iwf//2, n4iwb//2 + 1
            break
        except KeyError:
            continue
        except AssertionError:
            raise ValueError("At least one component of g4iw-worm has an inc"\
                             +"orrect shape: should be (n4iwf, n4iwf, n4iwb)")

        return ValueError("g4iw-worm does not contain any valid components")

    nsp = 2
    # Piece blocks for the triqs block Green's function together from
    # individual components, looping over blocks and then indices,
    # with offsets keeping track of the previous block sizes for
    # constructing the right w2dynamics compound indices
    result = np.zeros((norb, nsp, norb, nsp, norb, nsp, norb, nsp,
                       n4iwf * 2, n4iwf * 2, n4iwb * 2 - 1), arr.dtype)
    for o1 in range(norb):
        for s1 in range(nsp):
            for o2 in range(norb):
                for s2 in range(nsp):
                    for o3 in range(norb):
                        for s3 in range(nsp):
                            for o4 in range(norb):
                                for s4 in range(nsp):
                                    # we assume that spin is desired to be the
                                    # slowest changing index in the triqs
                                    # block structure, so we get orbital
                                    # indices for the compound index from the
                                    # block index by modulo and spin indices
                                    # by integer division
                                    cindex = component2index_general(
                                        norb, 4,
                                        np.array((o1, o2, o3, o4)),
                                        np.array((s1, s2, s3, s4)))
                                    try:
                                        result[o1, s1, o2, s2, o3, s3, o4, s4, :, :, :] = (
                                            g4iw[(f"{strg}/{cindex:05}")]
                                            [qtype][()])
                                    except KeyError:
                                        pass  # writing into zeros, 
                                              # leave it zeroed

    return result







####################################################################################################################################
############################################## Some general utility functions ######################################################
####################################################################################################################################

def bubble_asymp(susc, bubble):
    niwf = bubble.shape[-1]//2
    x0 = bubble.copy()
    niw4f = susc.shape[-1]//2
    nu_range = slice(niwf-niw4f, niwf+niw4f)
    x0[nu_range,nu_range] = susc
    return x0

def asymp_chi(nu, beta):
    """
    Returns bubble asymptotic -2*beta/nu^2,
    excluding inner fermionic Matsubara frequencies up
    to nu for +/-omega_max = pi/beta*(2*nu+1)
    """
    summ = np.sum(1/(2*np.arange(nu//2)+1)**2)
    return 2*beta*(1/8. - summ/np.pi**2)

def gradient(x, y):
    '''returns central differences and simple
    differences at begin and end of output vector'''
    assert len(x) == len(y), 'arguments must be of same length'
    yoverx=np.divide(np.diff(y), np.diff(x))
    diff = np.empty(len(x),dtype='complex')
    diff[0]=yoverx[0]
    for i in range(len(x)-2):
        f = np.diff(x)[i]/(np.diff(x)[i]+np.diff(x)[i+1])
        diff[i+1]= (1-f)*yoverx[i]+ f*yoverx[i+1]
    diff[-1]=yoverx[-1]
    return diff
    

def sub_matrix(matrix,N):
    """
    Returns n x n  numpy.matrix around mid of quadratic numpy.matrix

    Exampe: matrix=
               [[ 1, 2, 3, 4],
                [ 5, 6, 7, 8],
                [ 9,10,11,12],
                [13,14,15,16]]

    sub_matrix(matrix,2)=
                  [[6 , 7],
                   [10,11]]
    """
    if type(matrix) is np.ndarray:
        if matrix.ndim == 2 and matrix.shape[0] == matrix.shape[1]:
            mid = matrix.shape[0]//2
            if int(N) > matrix.shape[0]:
                print('Error: shape of submatrix greater then input matrix')
                print('input N =', N, 'is set to', matrix.shape[0])
                N = matrix.shape[0]
            if matrix.shape[0]%2 == 0:
                n = (int(N)//2)*2
                if n <2:
                    n=2
                if N%2 != 0 or N<2:
                    print('even input matrix')
                    print('input N =', N, 'is set to', n)
                return matrix[(int(mid)-int((n+1)//2)):(int(mid)+int(n//2)),\
                              (int(mid)-int((n+1)//2)):(int(mid)+int(n//2))]
            else:
                n = (int(N)//2)*2+1
                if n <1:
                    n=1
                if N%2 == 0 or N<1:
                    print('uneven input matrix')
                    print('input N =', N, 'is set to', n)
                return matrix[(int(mid)-int((n)//2)):(int(mid)+int((n+1)//2)),\
                              (int(mid)-int((n)//2)):(int(mid)+int((n+1)//2))]
        else:
            print('Error: sub_matrix() expecting'\
                  +' quadratic two-dimensional matrix')
    else:
        print('TypeError: sub_matrix() expecting'\
              +' argument of type numpy.ndarray')

def off_diag(matrix):
    """
    Returns off diagonal values of the upper left
    and lower right submatrix as numpy.matrix

    Exampe: matrix=
                   [[ 1, 2, 3, 4],
                    [ 5, 6, 7, 8],
                    [ 9,10,11,12],
                    [13,14,15,16]]

    off_diag(matrix)=
                   [[ 0, 2, 0, 0],
                    [ 5, 0, 0, 0],
                    [ 0, 0, 0,12],
                    [ 0, 0,15, 0]]
    """
    if type(matrix) is np.ndarray:
        if matrix.ndim == 2 and matrix.shape[0] == matrix.shape[1]\
                            and matrix.shape[0]%2 == 0:
            end                 = matrix.shape[0]
            half                = end//2
            new                 = np.copy(matrix)
            new[:half,half:end] = 0
            new[half:end,:half] = 0
            np.fill_diagonal(new,0)
            return new
        else:
            print('Error: off_diag() expecting quadratic'\
                  +' even two-dimensional matrix')
    else:
        raise TypeError('off_diag() expecting argument of type numpy.ndarray')


def off_counter(matrix):
    """
    Returns off diagonal values of the upper right and lower left submatrix
    along the counter diagonal as numpy.matrix

    Exampe: matrix=
                   [[ 1, 2, 3, 4],
                    [ 5, 6, 7, 8],
                    [ 9,10,11,12],
                    [13,14,15,16]]

    off_counter(matrix)=
                   [[ 0, 0, 3, 4],
                    [ 0, 0, 7, 8],
                    [ 9,10, 0, 0],
                    [13,14, 0, 0]]
    """
    if type(matrix) is np.ndarray:
        if (matrix.ndim == 2 
            and matrix.shape[0] == matrix.shape[1] 
            and matrix.shape[0]%2 == 0):
            end                    = matrix.shape[0]
            half                   = end//2
            new                    = np.copy(matrix)
            new[:half,:half]       = 0
            new[half:end,half:end] = 0
            return new
        else:
            print('Error: off_counter() expecting quadratic'\
                  +' even two-dimensional matrix')
    else:
        raise TypeError('off_counter() expecting argument'\
                        +' of type numpy.ndarray')

# ---------------------------------------
# free lattice Hamlitonians
# ---------------------------------------
def ek(t=0.25,tpr=0,tsec=0,kpoints=48,q=[0.,0.]):
    "return 2d sqaured lattice Hamiltonian"
    k = np.linspace(0.,2*np.pi,kpoints,endpoint=False)
    kx = np.array(k+q[0])[:,None]
    ky = np.array(k+q[1])[None,:]
    # way to automatically treat arbitrary dimension
    # ---------------------------------------------
    # from sympy.utilities.iterables import multiset_permutations
    # shape = np.ones(dim,dtype=int)
    # shape[0] = -1
    # shapes = multiset_permutations(shape)
    # ek =  sum([- 2*t*np.cos(2*np.pi*k.reshape(s)) for s in shapes])\
    
    return - 2*t*(np.cos(kx) + np.cos(ky))\
               - 4*tpr*np.cos(kx)*np.cos(ky)\
               - 2*tsec*(np.cos(2*kx)+np.cos(2*ky))
               

def is_centroherm(M):
    """
    Checks if input matrix M(-v:v, -v':v', -w:w) is centrohermitian: 
    Matrix(v,v',w)* = Matrix(-v,-v',-w) 
    """
    dim  = M.shape
    n,m,w = dim

    if n!=m:
        raise ValueError("First two dimensions of input Matrix should be equal")

    M_buf = np.empty([n,m,w], dtype=complex)
    for i in range(n):
        for j in range(m):
            for k in range(w):
                M_buf[i,j,k] = M[n-1-i,m-1-j,w-1-k]
    
    M_cc = np.conjugate(M)

    return np.allclose(M_buf, M_cc)

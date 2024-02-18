# %%
import numpy as np
import matplotlib.pyplot as plt


class model(object):
    """"
    A class to co calulate the quantities for the model Hamiltonian
    H = Σ_kσ [(e_k - µ) n_kσ + (e_k+Q - µ) n_k+Qσ + U n_kσ n_k+Q-σ ]

    attributes:
        U (float): value of pseudogap interaction.
        beta (float): inverse temperature.
        mu (float): chemical potential.
        t (float, optional): nearest neighbor hopping
        tpr (float, optional): next-nearest neighbor hopping
        tsec (float, optional): next-next-nearest neighbor hopping
        Qx (float, optional): x-component of coupling vector
        Qy (float, optional): y-component of coupling vector
        kpoints (int, optional): number of k-points in one dimension
        Niwf (int, optional): number of positive fermionic Matsubara 
                              frequencies
        Niwb (int, optional): number of positive bosonic Matsubara
                              frequencies
        deltino (float, optional): imaginary offset for real frequency
        D (float, optional): bandwidth for real frequency
        vpoints (int, optional): number of real frequency points

    """
    def __init__(self, U, beta, mu, t=1, tpr=-0.2, tsec=0.1,
                 Qx=np.pi, Qy=np.pi, kpoints: int=200, Niwf: int=100,
                 Niwb: int=7 , deltino=1e-2, D=4, vpoints: int=401) -> None:
        self.U = U
        self.beta = beta
        self.mu = mu
        self.t = t
        self.tpr = tpr
        self.tsec = tsec
        self.Qx = Qx
        self.Qy = Qy
        self.kpoints = kpoints
        self.Niwf = Niwf
        self.Niwb = Niwb
        self.deltino = deltino
        self.D = D
        self.vpoints = vpoints
        self.k = np.linspace(-np.pi, np.pi,kpoints, endpoint=False)

    def ek(self,kx,ky):
        """
        args:
            kx (array): k-vector in x direction
            ky (array): k-vector in y direction
        returns:
            dispersion relation of 2D square lattice for 2 atomic basis
            for hopping between atoms (a) and atoms (b)
        """
        return  - 2*self.t*(np.cos(kx)+np.cos(ky)) \
                - 4*self.tpr*np.cos(kx)*np.cos(ky)\
                - 2*self.tsec*(np.cos(2*kx)+np.cos(2*ky))

    def Z(self,kx,ky):
        """
        args:
            kx (array): k-vector in x direction
            ky (array): k-vector in y direction
        returns:
            the partition function
        """
        hk = self.ek(kx,ky)-self.mu
        hq = self.ek(kx+self.Qx,ky+self.Qy)-self.mu
        z = (1 + np.exp(-self.beta*hk) + np.exp(-self.beta*hq) \
                    + np.exp(-self.beta*(hk+hq+self.U)))
        return z

    def v(self):
        """
        returns:
            real frequencies: v
        """
        return np.linspace(-2*self.D,2*self.D,self.vpoints)

    def iv(self):
        """
        returns:
            fermionic Matsubara frequencies iv
        """
        return 1j*(2*np.arange(-self.Niwf,self.Niwf)+1)*np.pi/self.beta
    
    def iOmega(self):
        """
        returns:
            bosonic Matsubara frequencies iΩ
        """
        return 1j*(2*np.arange(-self.Niwb,self.Niwb))*np.pi/self.beta
        
    def g0(self,kx,ky,mats=True):
        """
        args:
            kx (array): k-vector in x direction
            ky (array): k-vector in y direction
            mats (bool, optional): Matsubara or real frequencies 
        returns:
            non-interacting Green's function
        """
        hk = self.ek(kx,ky)-self.mu
        if mats:
            nu = self.iv()
        else:
            nu = self.v()+1j*self.deltino

        if (type(kx).__module__ == np.__name__ 
            and type(ky).__module__ == np.__name__
            and kx.ndim == 2 and ky.ndim == 2):
            hk = hk[None,:,:]
            nu = nu[:,None,None]
        return 1/(nu-hk)

    def g(self,kx,ky,mats=True):
        """
        args:
            kx (array): k-vector in x direction
            ky (array): k-vector in y direction
            mats (bool, optional): Matsubara or real frequencies 
        returns:
            Green's function
        """
        hk = self.ek(kx,ky)-self.mu
        hq = self.ek(kx+self.Qx,ky+self.Qy)-self.mu
        nq = self.nk(kx+self.Qx,ky+self.Qy)

        if mats:
            nu = self.iv()
        else:
            nu = self.v()+1j*self.deltino

        if (type(kx).__module__ == np.__name__ 
            and type(ky).__module__ == np.__name__
            and kx.ndim == 2 and ky.ndim == 2):
            hk = hk[None,:,:]
            hq = hq[None,:,:]
            nq = nq[None,:,:]
            nu = nu[:,None,None]

        green = (1-nq)/(nu-hk) + nq/(nu-hk-self.U) 
        return green

    def dgdv(self,kx,ky,mats=True):
        """
        args:
            kx (array): k-vector in x direction
            ky (array): k-vector in y direction
            mats (bool, optional): Matsubara or real frequencies 
        returns:
            Green's function
        """
        hk = self.ek(kx,ky)-self.mu
        hq = self.ek(kx+self.Qx,ky+self.Qy)-self.mu
        nq = self.nk(kx+self.Qx,ky+self.Qy)

        if mats:
            nu = self.iv()
        else:
            nu = self.v()+1j*self.deltino

        if (type(kx).__module__ == np.__name__ 
            and type(ky).__module__ == np.__name__
            and kx.ndim == 2 and ky.ndim == 2):
            hk = hk[None,:,:]
            hq = hq[None,:,:]
            nq = nq[None,:,:]
            nu = nu[:,None,None]

        green = -(1-nq)/(nu-hk)**2 - nq/(nu-hk-self.U)**2 
        return green
    
    def Ak(self):
        """
        returns:
            spectral function
        """
        Gk = self.g(self.k[:,None],self.k[None,:],mats=False)
        return - Gk.imag/np.pi
    
    def A(self):
        """
        returns:
            k-summed spectral function for each k point
        """
        return np.sum(self.Ak(),axis=(1,2))/self.kpoints**2

    def sigma(self,kx,ky,mats=True):
        """
        args:
            kx (array): k-vector in x direction
            ky (array): k-vector in y direction
            mats (bool, optional): Matsubara or real frequencies 
        returns:
            self energy
        """
        G0 = self.g0(kx,ky,mats=mats)
        G = self.g(kx,ky,mats=mats)
        return 1./G0 - 1./G

    def nk(self,kx,ky):
        """
        args:
            kx (array): k-vector in x direction
            ky (array): k-vector in y direction
        returns:
            occupation for k-vector and spin
        """
        hk = self.ek(kx,ky)-self.mu
        hq = self.ek(kx+self.Qx,ky+self.Qy)-self.mu
        # numerator denominator handling
        return np.where(hk>0
                        ,np.where(hq+self.U>0
                                ,(np.exp(-self.beta*hk)\
                                  +  np.exp(-self.beta*(hk+hq+self.U)))\
                                /(1 + np.exp(-self.beta*hk)\
                                  + np.exp(-self.beta*hq)\
                                  + np.exp(-self.beta*(hk+hq+self.U)))
                                ,(np.exp(-self.beta*(hk-hq-self.U))\
                                  +  np.exp(-self.beta*(hk)))\
                                /(np.exp(self.beta*(hq+self.U))\
                                  + np.exp(-self.beta*(hk-hq-self.U))\
                                  + np.exp(self.beta*self.U)\
                                  + np.exp(-self.beta*(hk)))
                        )
                        ,np.where(hq+self.U>0
                                ,(1 +  np.exp(-self.beta*(hq+self.U)))\
                                /(np.exp(self.beta*hk) + 1\
                                 + np.exp(-self.beta*(hq-hk))\
                                 + np.exp(-self.beta*(hq+self.U)))
                                ,(np.exp(self.beta*(hq+self.U)) + 1)\
                                /(np.exp(self.beta*(hk+hq+self.U))\
                                  + np.exp(self.beta*(hq+self.U))\
                                  + np.exp(self.beta*(hk+self.U)) + 1)
                        )
                    )
    def N(self):
        """
        returns:
            occupation for one spin
        """
        return np.sum(self.nk(self.k[:,None],self.k[None,:]))/self.kpoints**2

    def Dk(self,kx,ky):
        """
        args:
            kx (array): k-vector in x direction
            ky (array): k-vector in y direction
        returns:
            double occupation for k-vector
        """
        hk = self.ek(kx,ky)-self.mu
        hq = self.ek(kx+self.Qx,ky+self.Qy)-self.mu
        return np.where(hk+hq+self.U>0
                        ,np.exp(-self.beta*(hk+hq+self.U))\
                         /(1 + np.exp(-self.beta*hk)\
                          + np.exp(-self.beta*hq)\
                          + np.exp(-self.beta*(hk+hq+self.U)))
                        ,1\
                         /(1 + np.exp(self.beta*(hk+self.U))\
                          + np.exp(self.beta*(hq+self.U))\
                          + np.exp(self.beta*(hk+hq+self.U)))
                    )

        #z   = self.Z(kx,ky)
        #return 1/z*np.exp(-self.beta*(hk+hq+self.U))
    
    def cv_k(self,subspace=None):
        """
        returns:
            specific heat for each k point
        """
        sl = slice(subspace)
        kx = self.k[sl,None]
        ky = self.k[None,sl]
        hk = self.ek(kx,ky)-self.mu
        hq = self.ek(kx+self.Qx,ky+self.Qy)-self.mu

        dzdb_z = np.where((hk>0) | ((hk<0) & (hq<=hk) & (hk+self.U>0))
                        ,np.where(hq>0
                                  ,-(hk*np.exp(-self.beta*hk)\
                                     + hq*np.exp(-self.beta*hq)\
                                     + (hk+hq+self.U)\
                                        *np.exp(-self.beta*(hk+hq+self.U)))\
                                   /(1 + np.exp(-self.beta*hk)\
                                     + np.exp(-self.beta*hq)\
                                     + np.exp(-self.beta*(hk+hq+self.U)))
                                  ,-(hk*np.exp(self.beta*(-hk+hq)) + hq \
                                     + (hk+hq+self.U)\
                                        *np.exp(-self.beta*(hk+self.U)))\
                                   /(np.exp(self.beta*(hq))\
                                     + np.exp(self.beta*(-hk+hq)) + 1 \
                                     + np.exp(-self.beta*(hk+self.U)))
                                   #*np.exp(self.beta*(hq)) 
                        )
                        ,np.where((hq>0) | ((hq<0) & (hk<=hq) & (hq+self.U>0))
                                  ,-(hk + hq*np.exp(self.beta*(hk-hq))\
                                     + (hk+hq+self.U)\
                                        *np.exp(-self.beta*(hq+self.U)))\
                                    /(np.exp(self.beta*(hk)) + 1\
                                     + np.exp(self.beta*(hk-hq))\
                                     + np.exp(-self.beta*(hq+self.U)))
                                    #*np.exp(self.beta*(hk))
                                  ,-(hk*np.exp(self.beta*(hq+self.U))\
                                     + hq*np.exp(self.beta*(hk+self.U))\
                                     + (hk+hq+self.U)) \
                                    /(np.exp(self.beta*(hk+hq+self.U))\
                                      + np.exp(self.beta*(hq+self.U))\
                                      + np.exp(self.beta*(hk+self.U)) + 1)
                                    #*np.exp(self.beta*(hk+hq+self.U))
                        )
        )
        d2zdb2_z = np.where((hk>0) | ((hk<0) &  (hq<=hk) &(hk+self.U>0))
                        ,np.where(hq>0 
                                  ,(hk**2*np.exp(-self.beta*hk)\
                                    + hq**2*np.exp(-self.beta*hq) \
                                    + (hk+hq+self.U)**2\
                                        *np.exp(-self.beta*(hk+hq+self.U)))\
                                   /(1 + np.exp(-self.beta*hk)\
                                     + np.exp(-self.beta*hq)\
                                     + np.exp(-self.beta*(hk+hq+self.U)))
                                  ,(hk**2*np.exp(self.beta*(-hk+hq)) + hq**2\
                                    + (hk+hq+self.U)**2\
                                        *np.exp(-self.beta*(hk+self.U)))\
                                   /(np.exp(self.beta*(hq))\
                                     + np.exp(self.beta*(-hk+hq)) + 1\
                                     + np.exp(-self.beta*(hk+self.U)))
                                   #*np.exp(self.beta*(hq))
                        )
                        ,np.where((hq>0) | ((hq<0) & (hk<=hq) & (hq+self.U>0))
                                  ,(hk**2 + hq**2*np.exp(self.beta*(hk-hq))\
                                    + (hk+hq+self.U)**2\
                                        *np.exp(-self.beta*(hq+self.U)))\
                                    /(np.exp(self.beta*(hk)) + 1\
                                      + np.exp(self.beta*(hk-hq))\
                                      + np.exp(-self.beta*(hq+self.U)))
                                    #*np.exp(self.beta*(hk))\
                                  ,(hk**2*np.exp(self.beta*(hq+self.U))\
                                    + hq**2*np.exp(self.beta*(hk+self.U))\
                                    + (hk+hq+self.U)**2)\
                                  /(np.exp(self.beta*(hk+hq+self.U))\
                                    + np.exp(self.beta*(hq+self.U))
                                    + np.exp(self.beta*(hk+self.U)) + 1)
                                  #*np.exp(self.beta*(hk+hq+self.U))\
                        )
        )
        return (d2zdb2_z - (dzdb_z)**2)*self.beta**2
    
    def cv(self):
        """
        returns:
            specific heat
        """
        return 4*np.sum(self.cv_k(subspace=self.kpoints//2))/self.kpoints**2
    

    def x0(self,q=[0.,0.],mats=True):
        """
        args:
            q (array,optional): transfer momentum
            mats (bool, optional): Matsubara or real frequencies
        returns:
            bubble susceptibility
        """
        if mats == True:
            Omega = self.iOmega()
        else:
            Omega = self.v()
        if q == [0.,0.]:
            xx = np.zeros(Omega.shape,dtype='complex')
            Omega = Omega[:,None,None]
            kx = self.k[None,:,None]
            ky = self.k[None,None,:]
            z  = self.Z (kx,ky)
            Hk = self.ek(kx,ky)-self.mu
            HQ = self.ek(kx+self.Qx,ky+self.Qy)-self.mu
            xx[self.Niwb] = self.beta\
                            *np.sum(1/z**2*(np.exp(-self.beta*Hk)\
                                    + np.exp(-self.beta*(Hk+2*HQ+self.U)))
                                    ,axis=(1,2))/self.kpoints**2
            xx = xx + np.sum(1/z**2\
                             *(np.exp(-self.beta*(Hk+HQ+self.U))\
                               *(np.exp(self.beta*(self.U))-1)/(Omega+self.U)\
                              + np.exp(-self.beta*(Hk+HQ))\
                               *(np.exp(-self.beta*(self.U))-1)\
                                /(Omega-self.U))
                            ,axis=(1,2))/self.kpoints**2
            return xx
        else:
            xx = np.zeros(Omega.shape,dtype='complex')
            Omega = Omega[:,None,None]
            kx = self.k[None,:,None]
            ky = self.k[None,None,:]
            z   = self.Z (kx, ky)
            zq  = self.Z (kx+q[0], ky+q[1])
            Hk  = self.ek(kx, ky) - self.mu
            HQ  = self.ek(kx+self.Qx, ky+self.Qy) - self.mu
            H_q = self.ek(kx+q[0], ky+q[1]) - self.mu
            HQq = self.ek(kx+self.Qx+q[0], ky+self.Qy+q[1]) - self.mu
            xx =  np.sum(1/z/zq\
                         *((1 + np.exp(-self.beta*(HQ+HQq+self.U)))\
                           *(np.exp(-self.beta*H_q) - np.exp(-self.beta*Hk ))\
                            /(Omega+Hk-H_q)\
                          + np.exp(-self.beta*HQ)\
                            *(np.exp(-self.beta*H_q)\
                              - np.exp(-self.beta*(Hk+self.U)))\
                             /(Omega+Hk-H_q+self.U)\
                          + np.exp(-self.beta*HQq)\
                            *(np.exp(-self.beta*(H_q+self.U))\
                              - np.exp(-self.beta*Hk))\
                             /(Omega+Hk-H_q-self.U))
                        ,axis=(1,2))/self.kpoints**2
            xx[self.Niwb] = np.sum(1/z/zq\
                *(np.where(Hk==H_q
                          ,self.beta*(np.exp(-self.beta*Hk )\
                                     + np.exp(-self.beta*(Hk+HQ+HQq+self.U)))\
                           + np.exp(-self.beta*HQ)\
                             *(np.exp(-self.beta*H_q)\
                               - np.exp(-self.beta*(Hk+self.U)))\
                              /(Hk-H_q+self.U)\
                           + np.exp(-self.beta*HQq)\
                             *(np.exp(-self.beta*(H_q+self.U))\
                               - np.exp(-self.beta*Hk))\
                              /(Hk-H_q-self.U)
                          ,(1 + np.exp(-self.beta*(HQ+HQq+self.U)))\
                           *(np.exp(-self.beta*H_q) - np.exp(-self.beta*Hk ))\
                            /(Hk-H_q)\
                           + np.exp(-self.beta*HQ)\
                             *(np.exp(-self.beta*H_q)\
                               - np.exp(-self.beta*(Hk+self.U)))\
                              /(Hk-H_q+self.U)\
                            + np.exp(-self.beta*HQq)\
                              *(np.exp(-self.beta*(H_q+self.U))\
                                - np.exp(-self.beta*Hk))\
                               /(Hk-H_q-self.U))
                 )
                               ,axis=(1,2))/self.kpoints**2
            return xx
        
    def x0_pp(self,q=[0.,0.],mats=True):
        """
        args:
            q (array,optional): transfer momentum
            mats (bool, optional): Matsubara or real frequencies
        returns:
            bubble susceptibility
        """
        if mats == True:
            Omega = self.iOmega()
        else:
            Omega = self.v()
        
        xx = np.zeros(Omega.shape,dtype='complex')
        Omega = Omega[:,None,None]
        kx = self.k[None,:,None]
        ky = self.k[None,None,:]
        z   = self.Z (kx             ,ky)
        zq  = self.Z (kx+q[0]        ,ky+q[1])
        Hk  = self.ek(kx             ,ky)             -self.mu
        HQ  = self.ek(kx+self.Qx     ,ky+self.Qy)     -self.mu
        H_q = self.ek(-kx+q[0]        ,-ky+q[1])        -self.mu
        HQq = self.ek(-kx+self.Qx+q[0],-ky+self.Qy+q[1])-self.mu
        xx =  np.sum(1/z/zq
                     *((1 + np.exp(-self.beta*(HQ+HQq+self.U)))\
                       *(np.exp(-self.beta*H_q) - np.exp(-self.beta*Hk))\
                        /(Omega+Hk-H_q)\
                      + np.exp(-self.beta*HQ)\
                        *(np.exp(-self.beta*H_q)\
                          - np.exp(-self.beta*(Hk+self.U)))\
                         /(Omega+Hk-H_q+self.U)\
                      + np.exp(-self.beta*HQq)\
                        *(np.exp(-self.beta*(H_q+self.U))\
                          - np.exp(-self.beta*Hk))\
                         /(Omega+Hk-H_q-self.U))
                    ,axis=(1,2))/self.kpoints**2
        xx[self.Niwb] = np.sum(1/z/zq\
              *(np.where(Hk==H_q
                        ,self.beta*(np.exp(-self.beta*Hk )
                                    + np.exp(-self.beta*(Hk+HQ+HQq+self.U)))\
                         + np.exp(-self.beta*HQ)\
                           *(np.exp(-self.beta*H_q)\
                             - np.exp(-self.beta*(Hk+self.U)))\
                            /(Hk-H_q+self.U)\
                         + np.exp(-self.beta*HQq)\
                           *(np.exp(-self.beta*(H_q+self.U))\
                             - np.exp(-self.beta*Hk))\
                            /(Hk-H_q-self.U)
                        ,(1 + np.exp(-self.beta*(HQ+HQq+self.U)))\
                         *(np.exp(-self.beta*H_q) - np.exp(-self.beta*Hk ))\
                           /(Hk-H_q)\
                         + np.exp(-self.beta*HQ)\
                           *(np.exp(-self.beta*H_q)\
                             - np.exp(-self.beta*(Hk+self.U)))\
                            /(Hk-H_q+self.U)\
                         + np.exp(-self.beta*HQq)\
                           *(np.exp(-self.beta*(H_q+self.U))\
                             - np.exp(-self.beta*Hk))\
                            /(Hk-H_q-self.U))\
                )
                            ,axis=(1,2))/self.kpoints**2
        return xx
    
    def chi_uu(self,q=[0.,0.],mats=True):
        """
        args:
            q (array,optional): transfer momentum
            mats (bool, optional): Matsubara or real frequencies
        returns:
            susceptibility for C+_up c_up c*_up c_up component
        """
        if mats == True:
            Omega = self.iOmega()
        else:
            Omega = self.v()
        if q == [0.,0.]:
            chi = np.zeros(Omega.shape,dtype='complex')
            nkk = self.nk(self.k[:,None],self.k[None,:])
            chi[self.Niwb] = self.beta * np.sum(nkk-nkk**2)/self.kpoints**2
            return chi
        else:
            chi = self.x0(q=q,mats=mats)
            return chi
        
    def chi_ud(self,q=[0.,0.],mats=True):
        """
        args:
            q (array,optional): transfer momentum
            mats (bool, optional): Matsubara or real frequencies
        returns:
            susceptibility for C+_up c_up c*_dn c_dn component
        """
        if mats == True:
            Omega = self.iOmega()
        else:
            Omega = self.v()
        if q == [0.,0.]:
            chi = np.zeros(Omega.shape,dtype='complex')
            nkk = self.nk(self.k[:,None],self.k[None,:])
            nQQ = self.nk(self.k[:,None]+self.Qx,self.k[None,:]+self.Qy)
            dkk = self.Dk(self.k[:,None],self.k[None,:])
            chi[self.Niwb] =  self.beta * np.sum(dkk-nkk*nQQ)/self.kpoints**2
            return chi
        else:
            return np.zeros(Omega.shape,dtype='complex')
        
    def chi_bar_ud(self,q=[0.,0.],mats=True):
        """
        args:
            q (array,optional): transfer momentum
            mats (bool, optional): Matsubara or real frequencies
        returns:
            susceptibility for C+_up c_dn c*_dn c_up component
        """
        if mats == True:
            Omega = self.iOmega()
        else:
            Omega = self.v()
        if q == [self.Qx,self.Qy]:
            chi = np.zeros(Omega.shape,dtype='complex')
            Omega = Omega[:,None,None]
            kx = self.k[None,:,None]
            ky = self.k[None,None,:]
            z   = self.Z (kx, ky)
            Hk  = self.ek(kx, ky) - self.mu
            HQ  = self.ek(kx+self.Qx, ky+self.Qy) - self.mu

            chi =  np.sum(1/z*(np.exp(-self.beta*HQ) - np.exp(-self.beta*Hk))\
                              /(Omega+Hk-HQ) 
                         ,axis=(1,2))/self.kpoints**2
            chi[self.Niwb] =  np.sum(np.where(Hk==HQ
                                             ,self.beta/z\
                                              *np.exp(-self.beta*Hk)
                                             ,1/z*(np.exp(-self.beta*HQ)\
                                                   - np.exp(-self.beta*Hk))\
                                                  /(Hk-HQ)
                                              )
                                    ,axis=(1,2))/self.kpoints**2
            return chi
        else:
            chi = self.x0(q=q,mats=mats)
            return chi

    def chi_s(self,q=[0.,0.],mats=True):
        """
        args:
            q (array,optional): transfer momentum
            mats (bool, optional): Matsubara or real frequencies
        returns:
            spin susceptibility
        """
        return 1/3*(self.chi_uu(q=q,mats=mats)-self.chi_ud(q=q,mats=mats))\
               + 2/3*self.chi_bar_ud(q=q,mats=mats)

    def chi_c(self,q=[0.,0.],mats=True):
        """
        args:
            q (array,optional): transfer momentum
            mats (bool, optional): Matsubara or real frequencies
        returns:
            charge susceptibility
        """
        return self.chi_uu(q=q,mats=mats) + self.chi_ud(q=q,mats=mats)
# %%

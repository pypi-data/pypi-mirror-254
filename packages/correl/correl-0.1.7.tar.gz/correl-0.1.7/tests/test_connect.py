# Test script for w2dyn_post module
import correl.w2dyn_post as w5
import pytest
import numpy as np

@pytest.fixture
def g2_data():
    data = w5.read("tests/b53_u2_4_mu1_0995_g2-2020-05-14-Thu-21-56-56.hdf5")
    yield data

@pytest.fixture
def g1_data():
    data = w5.read("tests/b53_u2_4_mu1_0995_stat-2022-11-10-Thu-12-38-14.hdf5")
    yield data

# test reading of 1P/2P data at different iters
def test_iter_err():
    with pytest.raises(IndexError) as excinfo:  
          file = w5.read("tests/b53_u2_4_mu1_0995_stat-2022-11-10-Thu-12-38-14.hdf5", iter=5)
    assert str(excinfo.value) == "Iteration index is too large, max iteration: 1"

def test_2p_err():
    file = w5.read("tests/b53_u2_4_mu1_0995_stat-2022-11-10-Thu-12-38-14.hdf5")
    with pytest.raises(KeyError) as excinfo:  
          chi = file.chi_ph()
    assert str(excinfo.value) == "'No 2p-GF found, this file contains one-particle data only'"


# check omega shift
def test_omega_shift(g2_data):
    data = g2_data
    biw = 5
    gk = data.gkiw(w5.ek(), biw=biw)
    assert gk.shape[-3] == len(data.iw)-2*biw, "Shifting grid by bonosic frequency biw leads to wrong frequency grid size"

def test_omega_shift_value(g2_data):
    data = g2_data
    biw = 1
    gk = data.gkiw(w5.ek(), biw=biw)
    gk0 = data.gkiw(w5.ek(), biw=0)
    assert np.allclose(gk0[:,:,2*abs(biw):,:,:], gk), "Shifting by bosonic freq is not executed properly"


# check 2P quantities shape
def test_p2_bubble(g2_data):
    data = g2_data
    bub = data.bubble(iw4f=False)
    assert bub.shape[-1] == len(data.iw), "Bubble has not same grid size as one-particle data"

def test_p2_orbs(g2_data):
    data = g2_data
    with pytest.raises(IndexError) as excinfo:  
          chi = data.bubble(norbs=[1,1])
    assert str(excinfo.value) == "Orbital indices are too large, this object has 1 orbitals"

# chi bse
def test_bse_channel(g2_data):
    data = g2_data
    with pytest.raises(ValueError) as excinfo:
        chi = data.bse_ph(w5.ek(), w5.ek(), "x")
    assert str(excinfo.value) == "Incorrect susceptibility was specified, options are c - Charge, s - Spin"

# asymptotics
def test_asymp(g2_data):
    data = g2_data
    chi = data.bse_ph(w5.ek(), w5.ek(), "c")
    bub = np.diag(data.bubble_q(w5.ek(), w5.ek(), iw4f=False))
    asy = w5.bubble_asymp(chi, bub)
    assert asy.shape==bub.shape, "Mismatch between shapes of bubble term and bubble asymptotic susc."



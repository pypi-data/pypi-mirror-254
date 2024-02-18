# encoding: utf-8
#
#Copyright (C) 2017-2023, P. R. Wiecha
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
"""
python implementations of the Green's Dyads, accelerated using `numba`
"""
from __future__ import print_function
from __future__ import absolute_import

import copy
import time
import warnings

import multiprocessing
import math
import cmath
import numpy as np

import numba

from pyGDM2.propagators import propagators



@numba.njit(cache=True)
def moving_average(a, n=15):
    ret = np.cumsum(a)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n


### --- 3D periodic Dyads - until now homogeneous environment only, normal incidence only
@numba.njit(cache=True)
def G0_periodic_123_direct_sum(R1, R2, wavelength, 
                    eps1=1.0+0j, eps2=1.0+0j, eps3=1.0+0j, spacing=5000, 
                    k_x=0.0, N_u=0, N_v=0, 
                    u=np.array([0., 0., 0.]), v=np.array([0., 0., 0.])):
    xx = np.zeros((N_u*2 + 1, N_v*2 + 1), dtype=np.complex64)
    yy = np.zeros((N_u*2 + 1, N_v*2 + 1), dtype=np.complex64)
    zz = np.zeros((N_u*2 + 1, N_v*2 + 1), dtype=np.complex64)
    xy = np.zeros((N_u*2 + 1, N_v*2 + 1), dtype=np.complex64)
    xz = np.zeros((N_u*2 + 1, N_v*2 + 1), dtype=np.complex64)
    yx = np.zeros((N_u*2 + 1, N_v*2 + 1), dtype=np.complex64)
    yz = np.zeros((N_u*2 + 1, N_v*2 + 1), dtype=np.complex64)
    zx = np.zeros((N_u*2 + 1, N_v*2 + 1), dtype=np.complex64)
    zy = np.zeros((N_u*2 + 1, N_v*2 + 1), dtype=np.complex64)
    
    for u_i in numba.prange(-N_u, N_u+1):
        for v_i in numba.prange(-N_v, N_v+1):
            _R1 = R1 + u*u_i + v*v_i     # position of emitter-copy from periodic cell [u_i, v_i]
            _xx, _yy, _zz, _xy, _xz, _yx, _yz, _zx, _zy = propagators.G0_EE_123(
                    _R1, R2, wavelength, eps1, eps2, eps3, spacing)
            
            ## !!! exp_term_k_x = np.exp(1j* k_x * (u*u_i + v*v_i)[0])  # should be added, see HE-tensor
            xx[u_i, v_i] = _xx
            yy[u_i, v_i] = _yy
            zz[u_i, v_i] = _zz
            xy[u_i, v_i] = _xy
            xz[u_i, v_i] = _xz
            yx[u_i, v_i] = _yx
            yz[u_i, v_i] = _yz
            zx[u_i, v_i] = _zx
            zy[u_i, v_i] = _zy
    
    return np.sum(xx), np.sum(yy), np.sum(zz), \
            np.sum(xy), np.sum(xz), np.sum(yx), \
            np.sum(yz), np.sum(zx), np.sum(zy)




### --- 3D periodic Dyads - until now homogeneous environment only, normal incidence only
@numba.njit(cache=True)
def G0_periodic_123(R1, R2, wavelength, 
                    eps1=1.0+0j, eps2=1.0+0j, eps3=1.0+0j, spacing=5000, 
                    k_x=0.0, N_u=0, N_v=0, 
                    u=np.array([0., 0., 0.]), v=np.array([0., 0., 0.])):
    xx = np.zeros((N_u*2 + 1, N_v*2 + 1), dtype=np.complex128)   # np.cumsum suffers from roudoff errors --> 128bit complex
    yy = np.zeros((N_u*2 + 1, N_v*2 + 1), dtype=np.complex128)
    zz = np.zeros((N_u*2 + 1, N_v*2 + 1), dtype=np.complex128)
    xy = np.zeros((N_u*2 + 1, N_v*2 + 1), dtype=np.complex128)
    xz = np.zeros((N_u*2 + 1, N_v*2 + 1), dtype=np.complex128)
    yx = np.zeros((N_u*2 + 1, N_v*2 + 1), dtype=np.complex128)
    yz = np.zeros((N_u*2 + 1, N_v*2 + 1), dtype=np.complex128)
    zx = np.zeros((N_u*2 + 1, N_v*2 + 1), dtype=np.complex128)
    zy = np.zeros((N_u*2 + 1, N_v*2 + 1), dtype=np.complex128)
    
    for _u_i in numba.prange(1, 2*(N_u+1)):
        u_i = (_u_i%2-0.5)*2 * _u_i//2       # start at center then hopping increasingly +/-1 in both directions
        for _v_i in numba.prange(1, 2*(N_v+1)):
            v_i = (_v_i%2-0.5)*2 * _v_i//2 
            _R1 = R1 + u*u_i + v*v_i     # position of emitter-copy from periodic cell [u_i, v_i]
            _xx, _yy, _zz, _xy, _xz, _yx, _yz, _zx, _zy = propagators.G0_EE_123(
                    _R1, R2, wavelength, eps1, eps2, eps3, spacing)
            
            ## !!! exp_term_k_x = np.exp(1j* k_x * (u*u_i + v*v_i)[0])  # should be added, see HE-tensor
            xx[_u_i-1, _v_i-1] = _xx
            yy[_u_i-1, _v_i-1] = _yy
            zz[_u_i-1, _v_i-1] = _zz
            xy[_u_i-1, _v_i-1] = _xy
            xz[_u_i-1, _v_i-1] = _xz
            yx[_u_i-1, _v_i-1] = _yx
            yz[_u_i-1, _v_i-1] = _yz
            zx[_u_i-1, _v_i-1] = _zx
            zy[_u_i-1, _v_i-1] = _zy
    
    # return np.sum(xx), np.sum(yy), np.sum(zz), \
    #        np.sum(xy), np.sum(xz), np.sum(yx), \
    #        np.sum(yz), np.sum(zx), np.sum(zy)
    
    ## calc. mean of moving average of tail of series to dampen oscillations
    xx = np.mean(moving_average(np.cumsum(xx.flatten()), n=N_u+N_v)[2*N_u*N_v:-1])
    yy = np.mean(moving_average(np.cumsum(yy.flatten()), n=N_u+N_v)[2*N_u*N_v:-1])
    zz = np.mean(moving_average(np.cumsum(zz.flatten()), n=N_u+N_v)[2*N_u*N_v:-1])
    xy = np.mean(moving_average(np.cumsum(xy.flatten()), n=N_u+N_v)[2*N_u*N_v:-1])
    xz = np.mean(moving_average(np.cumsum(xz.flatten()), n=N_u+N_v)[2*N_u*N_v:-1])
    yx = np.mean(moving_average(np.cumsum(yx.flatten()), n=N_u+N_v)[2*N_u*N_v:-1])
    yz = np.mean(moving_average(np.cumsum(yz.flatten()), n=N_u+N_v)[2*N_u*N_v:-1])
    zx = np.mean(moving_average(np.cumsum(zx.flatten()), n=N_u+N_v)[2*N_u*N_v:-1])
    zy = np.mean(moving_average(np.cumsum(zy.flatten()), n=N_u+N_v)[2*N_u*N_v:-1])
    
    return xx, yy, zz, xy, xz, yx, yz, zx, zy


@numba.njit(cache=True)
def Gs_periodic_123(R1, R2, wavelength, 
                    eps1=1.0+0j, eps2=1.0+0j, eps3=1.0+0j, spacing=5000, 
                    k_x=0.0, N_u=0, N_v=0, 
                    u=np.array([0., 0., 0.]), v=np.array([0., 0., 0.])):
    xx = np.zeros((N_u*2 + 1, N_v*2 + 1), dtype=np.complex128)   # np.cumsum suffers from roudoff errors --> 128bit complex
    yy = np.zeros((N_u*2 + 1, N_v*2 + 1), dtype=np.complex128)
    zz = np.zeros((N_u*2 + 1, N_v*2 + 1), dtype=np.complex128)
    xy = np.zeros((N_u*2 + 1, N_v*2 + 1), dtype=np.complex128)
    xz = np.zeros((N_u*2 + 1, N_v*2 + 1), dtype=np.complex128)
    yx = np.zeros((N_u*2 + 1, N_v*2 + 1), dtype=np.complex128)
    yz = np.zeros((N_u*2 + 1, N_v*2 + 1), dtype=np.complex128)
    zx = np.zeros((N_u*2 + 1, N_v*2 + 1), dtype=np.complex128)
    zy = np.zeros((N_u*2 + 1, N_v*2 + 1), dtype=np.complex128)
    
    for _u_i in numba.prange(1, 2*(N_u+1)):
        u_i = (_u_i%2-0.5)*2 * _u_i//2
        for _v_i in numba.prange(1, 2*(N_v+1)):
            v_i = (_v_i%2-0.5)*2 * _v_i//2 
            _R1 = R1 + u*u_i + v*v_i     # position of emitter-copy from periodic cell [u_i, v_i]
            _xx, _yy, _zz, _xy, _xz, _yx, _yz, _zx, _zy = propagators.Gs_EE_123(
                    _R1, R2, wavelength, eps1, eps2, eps3, spacing)
            
            ## !!! exp_term_k_x = np.exp(1j* k_x * (u*u_i + v*v_i)[0])  # should be added, see HE-tensor
            xx[_u_i-1, _v_i-1] = _xx
            yy[_u_i-1, _v_i-1] = _yy
            zz[_u_i-1, _v_i-1] = _zz
            xy[_u_i-1, _v_i-1] = _xy
            xz[_u_i-1, _v_i-1] = _xz
            yx[_u_i-1, _v_i-1] = _yx
            yz[_u_i-1, _v_i-1] = _yz
            zx[_u_i-1, _v_i-1] = _zx
            zy[_u_i-1, _v_i-1] = _zy
            
    # return np.sum(xx), np.sum(yy), np.sum(zz), \
    #        np.sum(xy), np.sum(xz), np.sum(yx), \
    #        np.sum(yz), np.sum(zx), np.sum(zy)
    
    ## calc. mean of moving average of tail of series to dampen oscillations
    xx = np.mean(moving_average(np.cumsum(xx.flatten()), n=N_u*N_v)[2*N_u*N_v:-1])
    yy = np.mean(moving_average(np.cumsum(yy.flatten()), n=N_u*N_v)[2*N_u*N_v:-1])
    zz = np.mean(moving_average(np.cumsum(zz.flatten()), n=N_u*N_v)[2*N_u*N_v:-1])
    xy = np.mean(moving_average(np.cumsum(xy.flatten()), n=N_u*N_v)[2*N_u*N_v:-1])
    xz = np.mean(moving_average(np.cumsum(xz.flatten()), n=N_u*N_v)[2*N_u*N_v:-1])
    yx = np.mean(moving_average(np.cumsum(yx.flatten()), n=N_u*N_v)[2*N_u*N_v:-1])
    yz = np.mean(moving_average(np.cumsum(yz.flatten()), n=N_u*N_v)[2*N_u*N_v:-1])
    zx = np.mean(moving_average(np.cumsum(zx.flatten()), n=N_u*N_v)[2*N_u*N_v:-1])
    zy = np.mean(moving_average(np.cumsum(zy.flatten()), n=N_u*N_v)[2*N_u*N_v:-1])
    
    return xx, yy, zz, xy, xz, yx, yz, zx, zy


@numba.njit(cache=True)
def Gtot_periodic_123(R1, R2, wavelength, 
                      eps1=1.0+0j, eps2=1.0+0j, eps3=1.0+0j, spacing=5000, 
                      k_x=0.0, N_u=0, N_v=0, 
                      u=np.array([0., 0., 0.]), v=np.array([0., 0., 0.])):
    ## ----- free space term
    xx, yy, zz, xy, xz, yx, yz, zx, zy = G0_periodic_123(R1, R2, wavelength, 
                                eps1, eps2, eps3, spacing, k_x, N_u, N_v, u, v)
    
    ## ----- surface term
    xxs,yys,zzs,xys,xzs,yxs,yzs,zxs,zys = Gs_periodic_123(R1, R2, wavelength, 
                                eps1, eps2, eps3, spacing, k_x, N_u, N_v, u, v)

    return xx + xxs, yy + yys, zz + zzs, \
           xy + xys, xz + xzs, yx + yxs, \
           yz + yzs, zx + zxs, zy + zys


@numba.njit(cache=True)
def G_HE_periodic(R1, R2, wavelength, 
                    eps1=1.0+0j, eps2=1.0+0j, eps3=1.0+0j, spacing=5000, 
                    k_x=0.0, N_u=0, N_v=0, 
                    u=np.array([0., 0., 0.]), v=np.array([0., 0., 0.])):
    xx = np.zeros((N_u*2 + 1, N_v*2 + 1), dtype=np.complex128)   # np.cumsum suffers from roudoff errors --> 128bit complex
    yy = np.zeros((N_u*2 + 1, N_v*2 + 1), dtype=np.complex128)
    zz = np.zeros((N_u*2 + 1, N_v*2 + 1), dtype=np.complex128)
    xy = np.zeros((N_u*2 + 1, N_v*2 + 1), dtype=np.complex128)
    xz = np.zeros((N_u*2 + 1, N_v*2 + 1), dtype=np.complex128)
    yx = np.zeros((N_u*2 + 1, N_v*2 + 1), dtype=np.complex128)
    yz = np.zeros((N_u*2 + 1, N_v*2 + 1), dtype=np.complex128)
    zx = np.zeros((N_u*2 + 1, N_v*2 + 1), dtype=np.complex128)
    zy = np.zeros((N_u*2 + 1, N_v*2 + 1), dtype=np.complex128)
    
        
    for _u_i in numba.prange(1, 2*(N_u+1)):
        u_i = (_u_i%2-0.5)*2 * _u_i//2
        for _v_i in numba.prange(1, 2*(N_v+1)):
            v_i = (_v_i%2-0.5)*2 * _v_i//2 
            _R1 = R1 + u*u_i + v*v_i     # position of emitter-copy from periodic cell [u_i, v_i]
            _xx, _yy, _zz, _xy, _xz, _yx, _yz, _zx, _zy = propagators.G_HE_123(
                    _R1, R2, wavelength, eps1, eps2, eps3, spacing)
            
            ## additional phase, use x-component of wave-vector --> incidence in XZ plane!
            exp_term_k_x = np.exp(1j* k_x * (u*u_i + v*v_i)[0])
            xx[_u_i-1, _v_i-1] = _xx * exp_term_k_x
            yy[_u_i-1, _v_i-1] = _yy * exp_term_k_x
            zz[_u_i-1, _v_i-1] = _zz * exp_term_k_x
            xy[_u_i-1, _v_i-1] = _xy * exp_term_k_x
            xz[_u_i-1, _v_i-1] = _xz * exp_term_k_x
            yx[_u_i-1, _v_i-1] = _yx * exp_term_k_x
            yz[_u_i-1, _v_i-1] = _yz * exp_term_k_x
            zx[_u_i-1, _v_i-1] = _zx * exp_term_k_x
            zy[_u_i-1, _v_i-1] = _zy * exp_term_k_x
    
    # return np.sum(xx), np.sum(yy), np.sum(zz), \
    #        np.sum(xy), np.sum(xz), np.sum(yx), \
    #        np.sum(yz), np.sum(zx), np.sum(zy)
    
    ## calc. mean of moving average of tail of series to dampen oscillations
    xx = np.mean(moving_average(np.cumsum(xx.flatten()), n=N_u*N_v)[2*N_u*N_v:-1])
    yy = np.mean(moving_average(np.cumsum(yy.flatten()), n=N_u*N_v)[2*N_u*N_v:-1])
    zz = np.mean(moving_average(np.cumsum(zz.flatten()), n=N_u*N_v)[2*N_u*N_v:-1])
    xy = np.mean(moving_average(np.cumsum(xy.flatten()), n=N_u*N_v)[2*N_u*N_v:-1])
    xz = np.mean(moving_average(np.cumsum(xz.flatten()), n=N_u*N_v)[2*N_u*N_v:-1])
    yx = np.mean(moving_average(np.cumsum(yx.flatten()), n=N_u*N_v)[2*N_u*N_v:-1])
    yz = np.mean(moving_average(np.cumsum(yz.flatten()), n=N_u*N_v)[2*N_u*N_v:-1])
    zx = np.mean(moving_average(np.cumsum(zx.flatten()), n=N_u*N_v)[2*N_u*N_v:-1])
    zy = np.mean(moving_average(np.cumsum(zy.flatten()), n=N_u*N_v)[2*N_u*N_v:-1])
    
    return xx, yy, zz, xy, xz, yx, yz, zx, zy
           


# @numba.njit(cache=True)
# def G_EE_perdiodic(R1, R2, wavelength, conf_dict):
#     """evaluate field of dipole emitter in 1-2-3 layer environment (NF approx.)
    
#     R1: dipole position
#     R2: evaluation position
#     """
#     k_x = np.float32(conf_dict['k_x'].real)
#     # eps1 = conf_dict['eps1']
#     eps2 = conf_dict['eps2']
#     # eps3 = conf_dict['eps3']
#     # spacing = np.float32(conf_dict['spacing'].real)
#     cutoff_u = np.int(conf_dict['cutoff_u'].real)
#     cutoff_v = np.int(conf_dict['cutoff_v'].real)
#     u = np.array([np.float32(conf_dict['ux'].real), 
#                   np.float32(conf_dict['uy'].real), 
#                   np.float32(conf_dict['uz'].real)])
#     v = np.array([np.float32(conf_dict['vx'].real), 
#                   np.float32(conf_dict['vy'].real), 
#                   np.float32(conf_dict['vz'].real)])
    
#     return _G0_periodic(R1, R2, wavelength, eps2, k_x, cutoff_u, cutoff_v, u, v)


# @numba.njit(cache=True)
# def G_HE_perdiodic(R1, R2, wavelength, conf_dict):
#     """evaluate field of dipole emitter in 1-2-3 layer environment (NF approx.)
    
#     R1: dipole position
#     R2: evaluation position
#     """
#     k_x = np.float32(conf_dict['k_x'].real)
#     # eps1 = conf_dict['eps1']
#     eps2 = conf_dict['eps2']
#     # eps3 = conf_dict['eps3']
#     # spacing = np.float32(conf_dict['spacing'].real)
#     cutoff_u = np.int(conf_dict['cutoff_u'].real)
#     cutoff_v = np.int(conf_dict['cutoff_v'].real)
#     u = np.array([np.float32(conf_dict['ux'].real), 
#                   np.float32(conf_dict['uy'].real), 
#                   np.float32(conf_dict['uz'].real)])
#     v = np.array([np.float32(conf_dict['vx'].real), 
#                   np.float32(conf_dict['vy'].real), 
#                   np.float32(conf_dict['vz'].real)])
    
#     return _G0_HE_periodic(R1, R2, wavelength, eps2, k_x, cutoff_u, cutoff_v, u, v)



### --- coupling matrix gen. non-retarded 
# =============================================================================
# multi-dp-propagation / coupling matrix generators non-retarded 3D
# =============================================================================
## --- multi-dipole field propagation
@numba.njit(parallel=True)
def greens_tensor_evaluation_periodic(dp_pos, r_probe, G_func, wavelength, conf_dict, M,
                                      selfterm=None, dist_div_G=None):
    k_x = np.float32(conf_dict['k_x'].real)
    
    eps1 = conf_dict['eps1']
    eps2 = conf_dict['eps2']
    eps3 = conf_dict['eps3']
    spacing = np.float32(conf_dict['spacing'].real)
    
    cutoff_u = np.int(conf_dict['cutoff_u'].real)
    cutoff_v = np.int(conf_dict['cutoff_v'].real)
    u = np.array([np.float32(conf_dict['ux'].real), 
                  np.float32(conf_dict['uy'].real), 
                  np.float32(conf_dict['uz'].real)])
    v = np.array([np.float32(conf_dict['vx'].real), 
                  np.float32(conf_dict['vy'].real), 
                  np.float32(conf_dict['vz'].real)])
    
    for i in numba.prange(len(dp_pos)):   # explicit parallel loop
        _pos = dp_pos[i]
        for j in range(len(r_probe)):
            _r = r_probe[j]
            xx, yy, zz, xy, xz, yx, yz, zx, zy = G_func(
                                        _pos, _r, wavelength, eps1, eps2, eps3, 
                                        spacing, k_x, cutoff_u, cutoff_v, u, v
                                        )
            ## return list of Greens tensors
            M[i,j,0,0], M[i,j,1,1], M[i,j,2,2] = xx, yy, zz
            M[i,j,1,0], M[i,j,2,0], M[i,j,0,1] = yx, zx, xy
            M[i,j,2,1], M[i,j,0,2], M[i,j,1,2] = zy, xz, yz

#%%
# =============================================================================
# Green's tensor evaluation functions
# =============================================================================
def _get_nr_processes():
    """return available processes
    
    see: 
    https://stackoverflow.com/questions/1006289/how-to-find-out-the-number-of-cpus-using-python
    """
    ## preffered method to get available processes (might fail on windows)
    try:
        import os
        return len(os.sched_getaffinity(0))
    except:
        pass
    
    ## if failed, try alternative using psutils
    try:
        import psutil
        return len(psutil.Process().cpu_affinity())
    except:
        pass
    
    ## fall back on multiprocessing value (if psutils not installed)
    import multiprocessing
    return multiprocessing.cpu_count()


@numba.njit(parallel=True)
def _eval_geo_positions_G0(geo, compare_array):
    for i in numba.prange(len(geo)):    # explicit parallel loop
        R2 = geo[i]       # "observer"
        for j in range(len(geo)):
            R1 = geo[j]   # emitter
            
            DX = R2[0] - R1[0]
            DY = R2[1] - R1[1]
            DZ = R2[2] - R1[2]
            
            compare_array[i,j] = [DX, DY, DZ, DZ]  # last DZ: dummy placeholder
    
@numba.njit(parallel=True)
def _eval_geo_positions_Gs(geo, compare_array):
    for i in numba.prange(len(geo)):    # explicit parallel loop
        R2 = geo[i]       # "observer"
        for j in range(len(geo)):
            R1 = geo[j]   # emitter
            
            DX = R2[0] - R1[0]
            DY = R2[1] - R1[1]
            DZsum = R2[2] + R1[2]
            
            compare_array[i,j] = [DX, DY, DZsum, DZsum]  # last DZsum: dummy placeholder

@numba.njit
def _reconstruct_tensors(M, tensor, index_grp):
    for j in index_grp:
        M[j] = tensor

def _integrate_g0_EE_periodic(args):
    DX,DY,DZ,_, wavelength, eps1, eps2, eps3, \
        spacing, k_x, cutoff_u, cutoff_v, ux,uy,uz, vx,vy,vz = args

    u = np.array([ux.real,uy.real,uz.real]).astype(np.float32)
    v = np.array([vx.real,vy.real,vz.real]).astype(np.float32)
    R1 = np.array([0,0,0], dtype=np.float32)
    R2 = np.array([DX.real, DY.real, DZ.real], dtype=np.float32)
    wavelength = wavelength.real
    k_x = k_x.real
    spacing = spacing.real
    cutoff_u = int(cutoff_u.real)
    cutoff_v = int(cutoff_v.real)
    
    if np.linalg.norm(R2) == 0:  # r=r' --> return 0
        xx, yy, zz, xy, xz, yx, yz, zx, zy = np.zeros(9, dtype=np.complex64)
    else:
        xx, yy, zz, xy, xz, yx, yz, zx, zy = G0_periodic_123(
                            R1, R2, wavelength, eps1, eps2, eps3, 
                            spacing, k_x, cutoff_u, cutoff_v, u, v
                            )
    SEE = np.array([[xx,xy,xz], [yx,yy,yz], [zx,zy,zz]], dtype=np.complex64)
    
    return SEE

def _integrate_gs_EE_periodic(args):
    DX,DY,DZ,_, wavelength, eps1, eps2, eps3, \
        spacing, k_x, cutoff_u, cutoff_v, ux,uy,uz, vx,vy,vz = args
        
    u = np.array([ux.real,uy.real,uz.real]).astype(np.float32)
    v = np.array([vx.real,vy.real,vz.real]).astype(np.float32)
    R1 = np.array([0,0,0], dtype=np.float32)
    R2 = np.array([DX.real, DY.real, DZ.real], dtype=np.float32)
    wavelength = wavelength.real
    k_x = k_x.real
    spacing = spacing.real
    cutoff_u = int(cutoff_u.real)
    cutoff_v = int(cutoff_v.real)
    
    if np.linalg.norm(R2) == 0:
        xx, yy, zz, xy, xz, yx, yz, zx, zy = np.zeros(9, dtype=np.complex64)
    else:
        xx, yy, zz, xy, xz, yx, yz, zx, zy = Gs_periodic_123(
                            R1, R2, wavelength, eps1, eps2, eps3, 
                            spacing, k_x, cutoff_u, cutoff_v, u, v
                            )
    SEEs = np.array([[xx,xy,xz], [yx,yy,yz], [zx,zy,zz]], dtype=np.complex64)
    
    return SEEs


def _integrate_g0_HE_periodic(args):
    DX,DY,DZ,_, wavelength, eps1, eps2, eps3, \
        spacing, k_x, cutoff_u, cutoff_v, ux,uy,uz, vx,vy,vz = args
        
    u = np.array([ux.real,uy.real,uz.real]).astype(np.float32)
    v = np.array([vx.real,vy.real,vz.real]).astype(np.float32)
    R1 = np.array([0,0,0], dtype=np.float32)
    R2 = np.array([DX.real, DY.real, DZ.real], dtype=np.float32)
    wavelength = wavelength.real
    k_x = k_x.real
    spacing = spacing.real
    cutoff_u = int(cutoff_u.real)
    cutoff_v = int(cutoff_v.real)
    
    if np.linalg.norm(R2) == 0:
        xx, yy, zz, xy, xz, yx, yz, zx, zy = np.zeros(9, dtype=np.complex64)
    else:
        xx, yy, zz, xy, xz, yx, yz, zx, zy = G_HE_periodic(
                            R1, R2, wavelength, eps1, eps2, eps3, 
                            spacing, k_x, cutoff_u, cutoff_v, u, v
                            )
    
    SHE = np.array([[xx,xy,xz], [yx,yy,yz], [zx,zy,zz]], dtype=np.complex64)
    return SHE





def t_sbs_G0_periodic(geo, wavelength, conf_dict, 
                      func_eval_identical_tensors=_eval_geo_positions_G0,
                      func_integrate_gs=_integrate_g0_EE_periodic,
                      verbose=True):
    
    eps1 = conf_dict['eps1']
    eps2 = conf_dict['eps2']
    eps3 = conf_dict['eps3']
    spacing = np.float32(conf_dict['spacing'].real)
    
    cutoff_u = int(conf_dict['cutoff_u'].real)
    cutoff_v = int(conf_dict['cutoff_v'].real)
    u = np.array([np.float32(conf_dict['ux'].real), 
                  np.float32(conf_dict['uy'].real), 
                  np.float32(conf_dict['uz'].real)])
    v = np.array([np.float32(conf_dict['vx'].real), 
                  np.float32(conf_dict['vy'].real), 
                  np.float32(conf_dict['vz'].real)])
    
    k_x = np.float32(conf_dict['k_x'].real)
    
    
    ## --- determine unique tensors in coupling matrix
    t0 = time.time()
    compare_array = np.zeros([len(geo), len(geo), 4], dtype=np.float32)
    func_eval_identical_tensors(geo, compare_array)
    compare_array = np.reshape(compare_array, (-1,4))
    if verbose: 
        t1 = time.time()
        print('identification of identical tensors: {:.2f}s'.format(t1-t0))
    
    
    ## --- sort indices by identical tensors
    idx_sort = np.argsort(compare_array.view('f4,f4,f4,f4'), axis=0, order=['f0', 'f1', 'f2'])
    sorted_compare_array = compare_array[idx_sort]
    if verbose: 
        t2 = time.time()
        print('sorting:                             {:.2f}s'.format(t2-t1))
    
        
    ## --- indices of identical tensors in coupling matrix
    unique_arr, idx_start, count = np.unique(sorted_compare_array, axis=0, 
                                             return_counts=True, return_index=True)
    
    ## splits the indices of identical tensors into separate arrays
    index_groups = np.split(idx_sort, idx_start[1:])
    if verbose: 
        t3 = time.time()
        print('indexing of unique tensors:          {:.2f}s'.format(t3-t2))
    
    
    ## --- construct coupling matrix
    ## calculate tensors with multiprocessing
    t0 = time.time()
    ## number of parallel processes
    if int(conf_dict['n_cpu'].real)==-1:
        N_cpu = _get_nr_processes()
    else:
        N_cpu = int(conf_dict['n_cpu'].real)
    
    args = np.ones((len(unique_arr), 14), dtype=np.complex64) * \
           np.array([wavelength, eps1, eps2, eps3, \
                     spacing, k_x, cutoff_u, cutoff_v, *u, *v], dtype=np.complex64)
    argslist = np.concatenate([np.squeeze(unique_arr), args], axis=1)
    
    with multiprocessing.Pool(N_cpu) as p:
        tensor_arr = p.map(func_integrate_gs, argslist)
    if verbose:
        t4 = time.time()
        print('calculating {: >6} periodic tensors: {:.2f}s (working on {} processes)'.format(len(unique_arr), t4-t3, N_cpu))
    
    # ## for testing: non-multiporcessing, sequential
    # tensor_arr = []
    # for arg in argslist:
    #     _G = func_integrate_gs(arg)
    #     tensor_arr.append(_G)
    
    ## --- fill coupling matrix
    M = np.zeros((len(geo)*len(geo), 3, 3), dtype=np.complex64)
    
    for i_G, idx_unique in enumerate(index_groups):
        _reconstruct_tensors(M, tensor_arr[i_G], idx_unique[:,0])
    M = np.reshape(M, [len(geo), len(geo), 3, 3]).swapaxes(0, 1)
    if verbose: 
        t5 = time.time()
        print('reconstruction of coupling matrix:   {:.2f}s'.format(t5-t4))
    
    return M



# @numba.njit(parallel=True, cache=True)
def t_sbs_selfterms_only(geo, wavelength, selfterms, conf_dict, M):
    for i in numba.prange(len(geo)):    # explicit parallel loop
        for j in range(len(geo)):
            if i==j:
                ## self term
                M[i,j] = selfterms[j]


@numba.njit(parallel=True, cache=True)
def _construct_coupled_dipole_system_EE(M0, Mself, Ms, alpha, M_sbs):
    for i in numba.prange(len(M0)):    # explicit parallel loop
        for j in range(len(M0[0])):
            ## invertible matrix:  delta_ij*1 - G[i,j] * alpha[j]
            # M_sbs[3*i:3*i+3, 3*j:3*j+3] = Ms[i,j]    # testing
            _M = M0[i,j] + Mself[i,j] + Ms[i,j]
            M_sbs[3*i:3*i+3, 3*j:3*j+3] = -1 * np.dot(_M, alpha[j])
            if i==j:
                M_sbs[3*i:3*i+3, 3*j:3*j+3] += np.identity(3)


@numba.njit(parallel=True, cache=True)
def _construct_coupled_dipole_system_HE(M0, Mself, Ms, alpha, M_sbs):
    for i in numba.prange(len(M0)):    # explicit parallel loop
        for j in range(len(M0[0])):
            ## invertible matrix:  - G[i,j] * alpha[j]
            _M = M0[i,j] + Mself[i,j] + Ms[i,j]
            M_sbs[3*i:3*i+3, 3*j:3*j+3] = -1 * np.dot(_M, alpha[j])


## !!!!!!!!!!!! MERGE THE FOLLOWING INTO PERIODIC CODE
# =============================================================================
# the actual coupling matrix generator functions
# =============================================================================
def t_sbs_EE_123_quasistatic_periodic(geo, wavelength, selfterms, alpha, conf_dict, M):
    M0 = np.zeros((len(geo), len(geo), 3, 3), dtype=np.complex64)
    Ms = np.zeros((len(geo), len(geo), 3, 3), dtype=np.complex64)
    Mself = np.zeros((len(geo), len(geo), 3, 3), dtype=np.complex64)
    Msbs = np.zeros((len(geo)*3, len(geo)*3), dtype=np.complex64)

    
    M0 = t_sbs_G0_periodic(geo, wavelength, conf_dict, 
                           func_eval_identical_tensors=_eval_geo_positions_G0,
                           func_integrate_gs=_integrate_g0_EE_periodic,
                           verbose=True)
    if conf_dict['eps1'] != conf_dict['eps2'] or conf_dict['eps2'] != conf_dict['eps3']:
        Ms = t_sbs_G0_periodic(geo, wavelength, conf_dict, 
                                func_eval_identical_tensors=_eval_geo_positions_Gs,
                                func_integrate_gs=_integrate_g0_EE_periodic,
                                verbose=True)
    t_sbs_selfterms_only(geo, wavelength, selfterms, conf_dict, Mself)
    
    _construct_coupled_dipole_system_EE(M0, Mself, Ms, alpha, Msbs)
    M[...] = Msbs    # subsitute M in-place
    

def t_sbs_HE_123_quasistatic_periodic(geo, wavelength, selfterms, alpha, conf_dict, M):
    M0 = np.zeros((len(geo), len(geo), 3, 3), dtype=np.complex64)
    Mself = np.zeros((len(geo), len(geo), 3, 3), dtype=np.complex64)
    Msbs = np.zeros((len(geo)*3, len(geo)*3), dtype=np.complex64)
    
    ## quasistatic approx.: surface contribution to G_HE = 0 
    Ms = np.zeros((len(geo), len(geo), 3, 3), dtype=np.complex64)
    
    M0 = t_sbs_G0_periodic(geo, wavelength, conf_dict, 
                           func_eval_identical_tensors=_eval_geo_positions_G0,
                           func_integrate_gs=_integrate_g0_EE_periodic,
                           verbose=True)
    t_sbs_selfterms_only(geo, wavelength, selfterms, conf_dict, Mself)
    
    _construct_coupled_dipole_system_HE(M0, Mself, Ms, alpha, Msbs)
    M[...] = Msbs    # subsitute M in-place
    
    





# #%%
# ## !!!!!! OLD, 'slow' PART
# @numba.njit(parallel=True, cache=True)
# def t_sbs_EE_123_quasistatic_periodic(geo, wavelength, selfterms, alpha, conf_dict, M):
#     k_x = np.float32(conf_dict['k_x'].real)
    
#     eps1 = conf_dict['eps1']
#     eps2 = conf_dict['eps2']
#     eps3 = conf_dict['eps3']
#     spacing = np.float32(conf_dict['spacing'].real)
    
#     cutoff_u = np.int(conf_dict['cutoff_u'].real)
#     cutoff_v = np.int(conf_dict['cutoff_v'].real)
#     u = np.array([np.float32(conf_dict['ux'].real), 
#                   np.float32(conf_dict['uy'].real), 
#                   np.float32(conf_dict['uz'].real)])
#     v = np.array([np.float32(conf_dict['vx'].real), 
#                   np.float32(conf_dict['vy'].real), 
#                   np.float32(conf_dict['vz'].real)])
    
#     for i in numba.prange(len(geo)):    # explicit parallel loop
#         R2 = geo[i]       # "observer"
#         for j in numba.prange(len(geo)):
#             R1 = geo[j]   # emitter
#             aj = alpha[j]
#             st = selfterms[j]
#             ## --- vacuum dyad
#             if i==j:
#                 ## self term
#                 xx, yy, zz = st[0,0], st[1,1], st[2,2]
#                 xy, xz, yx = st[0,1], st[0,2], st[1,0]
#                 yz, zx, zy = st[1,2], st[2,0], st[2,1]
#             else:
#                 xx, yy, zz, xy, xz, yx, yz, zx, zy = G0_periodic_123(
#                                         R1, R2, wavelength, eps1, eps2, eps3, 
#                                         spacing, k_x, cutoff_u, cutoff_v, u, v
#                                         )
            
#             ## --- 1-2-3 surface dyad (non retarded NF approximation)
#             if eps1!=eps2 or eps2!=eps3:
#                 xxs,yys,zzs,xys,xzs,yxs,yzs,zxs,zys = Gs_periodic_123(
#                                         R1, R2, wavelength, eps1, eps2, eps3, 
#                                         spacing, k_x, cutoff_u, cutoff_v, u, v
#                                         )
#                 ## combined dyad
#                 xx, yy, zz, xy, xz, yx, yz, zx, zy = xx+xxs, yy+yys, zz+zzs, \
#                                                       xy+xys, xz+xzs, yx+yxs, \
#                                                       yz+yzs, zx+zxs, zy+zys
            
#             ## return invertible matrix:  delta_ij*1 - G[i,j] * alpha[j]
#             M[3*i+0, 3*j+0] = -1*(xx*aj[0,0] + xy*aj[1,0] + xz*aj[2,0])
#             M[3*i+1, 3*j+1] = -1*(yx*aj[0,1] + yy*aj[1,1] + yz*aj[2,1])
#             M[3*i+2, 3*j+2] = -1*(zx*aj[0,2] + zy*aj[1,2] + zz*aj[2,2])
#             M[3*i+0, 3*j+1] = -1*(xx*aj[0,1] + xy*aj[1,1] + xz*aj[2,1])
#             M[3*i+0, 3*j+2] = -1*(xx*aj[0,2] + xy*aj[1,2] + xz*aj[2,2])
#             M[3*i+1, 3*j+0] = -1*(yx*aj[0,0] + yy*aj[1,0] + yz*aj[2,0])
#             M[3*i+1, 3*j+2] = -1*(yx*aj[0,2] + yy*aj[1,2] + yz*aj[2,2])
#             M[3*i+2, 3*j+0] = -1*(zx*aj[0,0] + zy*aj[1,0] + zz*aj[2,0])
#             M[3*i+2, 3*j+1] = -1*(zx*aj[0,1] + zy*aj[1,1] + zz*aj[2,1])
#             if i==j:
#                 M[3*i+0, 3*j+0] += 1
#                 M[3*i+1, 3*j+1] += 1
#                 M[3*i+2, 3*j+2] += 1


# @numba.njit(parallel=True, cache=True)
# def t_sbs_HE_123_quasistatic_periodic(geo, wavelength, selfterms, alpha, conf_dict, M):
#     k_x = np.float32(conf_dict['k_x'].real)
    
#     eps1 = conf_dict['eps1']
#     eps2 = conf_dict['eps2']
#     eps3 = conf_dict['eps3']
#     spacing = np.float32(conf_dict['spacing'].real)
    
#     cutoff_u = np.int(conf_dict['cutoff_u'].real)
#     cutoff_v = np.int(conf_dict['cutoff_v'].real)
#     u = np.array([np.float32(conf_dict['ux'].real), 
#                   np.float32(conf_dict['uy'].real), 
#                   np.float32(conf_dict['uz'].real)])
#     v = np.array([np.float32(conf_dict['vx'].real), 
#                   np.float32(conf_dict['vy'].real), 
#                   np.float32(conf_dict['vz'].real)])
    
#     for i in numba.prange(len(geo)):    # explicit parallel loop
#         R2 = geo[i]        # "observer"
#         st = selfterms[i]
#         for j in numba.prange(len(geo)):
#             R1 = geo[j]    # emitter
#             aj = alpha[j]
#             ## --- vacuum dyad
#             if i==j:
#                 ## self term
#                 xx, yy, zz = st[0,0], st[1,1], st[2,2]
#                 xy, xz, yx = st[0,1], st[0,2], st[1,0]
#                 yz, zx, zy = st[1,2], st[2,0], st[2,1]
#             else:
#                 xx, yy, zz, xy, xz, yx, yz, zx, zy = G_HE_periodic(
#                                         R1, R2, wavelength, eps1, eps2, eps3, 
#                                         spacing, k_x, cutoff_u, cutoff_v, u, v
#                                         )
            
#             ## return: G[i,j] * alpha[j]
#             ## --- magnetic-electric part
#             M[3*i+0, 3*j+0] = -1*(xx*aj[0,0] + xy*aj[1,0] + xz*aj[2,0])
#             M[3*i+1, 3*j+1] = -1*(yx*aj[0,1] + yy*aj[1,1] + yz*aj[2,1])
#             M[3*i+2, 3*j+2] = -1*(zx*aj[0,2] + zy*aj[1,2] + zz*aj[2,2])
#             M[3*i+0, 3*j+1] = -1*(xx*aj[0,1] + xy*aj[1,1] + xz*aj[2,1])
#             M[3*i+0, 3*j+2] = -1*(xx*aj[0,2] + xy*aj[1,2] + xz*aj[2,2])
#             M[3*i+1, 3*j+0] = -1*(yx*aj[0,0] + yy*aj[1,0] + yz*aj[2,0])
#             M[3*i+1, 3*j+2] = -1*(yx*aj[0,2] + yy*aj[1,2] + yz*aj[2,2])
#             M[3*i+2, 3*j+0] = -1*(zx*aj[0,0] + zy*aj[1,0] + zz*aj[2,0])
#             M[3*i+2, 3*j+1] = -1*(zx*aj[0,1] + zy*aj[1,1] + zz*aj[2,1])


### --- dyad class 3D non-retarded, 1D or 2D periodic
class DyadsQuasistaticPeriodic123(propagators.DyadsBaseClass):
    __name__ = "Quasistatic 3D '1-2-3' Green's tensors with periodicity"
    
    def __init__(self, n1=None, n2=None, n3=None, spacing=5000, 
                 u=np.array([0,0,0]), v=np.array([0,0,0]), 
                 cutoff_u=10, cutoff_v=10, 
                 radiative_correction=False,
                 n_cpu=-1):
        """ 
        u or v: period vectors
        set np.array([0,0,0]) for no periodicity in this dimension
        
        incident wavevector must be in XZ plane
        
        """
        super().__init__()
        
        self.u = u.astype(self.dtypef)
        self.v = v.astype(self.dtypef)
        
        self.cutoff_u = cutoff_u
        self.cutoff_v = cutoff_v
        if np.linalg.norm(u)==0: 
            self.cutoff_u = 0
        if np.linalg.norm(v)==0: 
            self.cutoff_v = 0
            
        ## Dyads
        self.G_EE = Gtot_periodic_123
        self.G_HE = G_HE_periodic
        self.G_EE_ff = Gtot_periodic_123    # using full propagator here for the moment
        
        ## evaluate propagator routine
        self.eval_G = greens_tensor_evaluation_periodic
        
        ## coupling matrix constructor routines
        self.tsbs_EE = t_sbs_EE_123_quasistatic_periodic
        self.tsbs_HE = t_sbs_HE_123_quasistatic_periodic
        
        ## environment definition
        ## set ref. index values or material class of environment layers
        from pyGDM2 import materials
        if isinstance(n1, (int, float, complex)) and not isinstance(n1, bool):
            self.n1_material = materials.dummy(n1)
        else:
            self.n1_material = n1
        
        n2 = n2 or n1     # if None, use `n1`
        if isinstance(n2, (int, float, complex)) and not isinstance(n2, bool):
            from pyGDM2 import materials
            self.n2_material = materials.dummy(n2)
        else:
            self.n2_material = n2
            
        n3 = n3 or n2     # if None, use `n2`
        if isinstance(n3, (int, float, complex)) and not isinstance(n3, bool):
            from pyGDM2 import materials
            self.n3_material = materials.dummy(n3)
        else:
            self.n3_material = n3
        
        self.spacing = spacing
        self.radiative_correction = radiative_correction
    
        self.n_cpu = n_cpu
        
    
    def __repr__(self, verbose=False):
        """description about simulation environment defined by set of dyads
        """
        out_str =  ' ------ environment -------'
        out_str += '\n ' + self.__name__
        out_str += '\n\n '
        out_str += 'peridicity: U={}, V={}\n '.format(self.u, self.v)
        out_str += '\n' + '   n3 = {}  <-- top'.format(self.n3_material.__name__)
        out_str += '\n' + '   n2 = {}  <-- structure zone (height "spacing" = {}nm)'.format(
                        self.n2_material.__name__, self.spacing)
        out_str += '\n' + '   n1 = {}  <-- substrate'.format(self.n1_material.__name__)
        return out_str

    
    def getConfigDictG(self, wavelength, struct, efield):
        if 'theta_inc' in efield.kwargs_permutations[0].keys():
            inc_angle = np.pi * efield.kwargs_permutations[0]['theta_inc'] / 180.0
        elif 'inc_angle' in efield.kwargs_permutations[0].keys():
            inc_angle = np.pi * efield.kwargs_permutations[0]['inc_angle'] / 180.0
        elif 'kSign' in efield.kwargs_permutations[0].keys():
            if efield.kwargs_permutations[0]['kSign'] == 1:
                inc_angle = 0.0    # bottom incidence
            else:
                inc_angle = np.pi  # top incidence
        else:
                inc_angle = np.pi  # top incidence
        
        
        ## all data need to be same dtype, must be cast to correct type inside numba functions
        conf_dict = numba.typed.Dict.empty(key_type=numba.types.unicode_type,
                                           value_type=numba.types.complex64)
        
        conf_dict['eps1'] = np.complex64(self.n1_material.epsilon(wavelength))
        conf_dict['eps2'] = np.complex64(self.n2_material.epsilon(wavelength))
        conf_dict['eps3'] = np.complex64(self.n3_material.epsilon(wavelength))
        conf_dict['spacing'] = np.complex64(self.spacing)
        conf_dict['ux'] = np.complex64(self.u[0])
        conf_dict['uy'] = np.complex64(self.u[1])
        conf_dict['uz'] = np.complex64(self.u[2])
        conf_dict['vx'] = np.complex64(self.v[0])
        conf_dict['vy'] = np.complex64(self.v[1])
        conf_dict['vz'] = np.complex64(self.v[2])
        conf_dict['cutoff_u'] = np.complex64(self.cutoff_u)
        conf_dict['cutoff_v'] = np.complex64(self.cutoff_v)
        
        conf_dict['n_cpu'] = np.complex64(self.n_cpu)
        
        n2 = (self.n2_material.epsilon(wavelength)**0.5)
        k_x = np.sin(inc_angle) * 2*np.pi * np.sqrt(n2**2) / wavelength
        conf_dict['k_x'] = np.complex64(k_x)
        
        ## return a numba typed dictionary of "complex64" type,
        ## can be used to pass configuration to the green's functions
        return conf_dict
    
    
    def exceptionHandling(self, struct, efield):
        """Exception handling / consistency and compatibility check
        
        check if structure and incident field generator are compatible

        Parameters
        ----------
        struct : :class:`.structures.struct`
            instance of structure class
        efield : :class:`.fields.efield`
            instance of incident field class

        Returns
        -------
        bool : True if struct and field are compatible, False if they don't fit the tensors

        """
        if efield.field_generator.__name__ not in ['plane_wave', 'planewave', 'evanescent_planewave']:
            raise Exception("periodic structures only work with plane wave illumination. " +
                            "Please use 'plane_wave', 'planewave' or 'evanescent_planewave' field generator!")
        
        all_inc_angles = []
        for k in efield.kwargs_permutations:
            if 'theta_inc' in k.keys():
                all_inc_angles.append(k['theta_inc'])
            if 'inc_plane' in k.keys():
                if k['inc_plane'] == 'yz':
                    raise Exception("'yz' plane of incidence is not supported by periodic structures. please use 'xz' incidence plane.")
        if len(np.unique(all_inc_angles)) > 1:
            raise Exception("For technical reasons periodic simulations can treat only a single incident angle. " + 
                            "Please run multiple separate simulations.")
        
        return True
    
    
    def getEnvironmentIndices(self, wavelength, geo):
        """get environment permittivity for `wavelength` at each meshpoint"""
        self.n1 = self.n1_material.epsilon(wavelength)**0.5
        self.n2 = self.n2_material.epsilon(wavelength)**0.5
        self.n3 = self.n3_material.epsilon(wavelength)**0.5
        
        ## environment epsilon at every meshpoint
        eps_env = np.zeros(len(geo), dtype=self.dtypec)
        eps_env[geo.T[2].min() > self.spacing] = self.n3_material.epsilon(wavelength)
        eps_env[0 <= geo.T[2].min() <= self.spacing] = self.n2_material.epsilon(wavelength)
        eps_env[geo.T[2].min() < 0] = self.n1_material.epsilon(wavelength)
        
        return eps_env
        
        
    def getSelfTermEE(self, wavelength, struct):
        eps_env = self.getEnvironmentIndices(wavelength, struct.geometry)
        struct.setWavelength(wavelength)
        
        k0 = 2.0*np.pi / float(wavelength)
        
        if struct.normalization == 0:
            cnorm = np.zeros(len(eps_env))
        else:
            norm_nonrad = -4.0 * np.pi * struct.normalization / (3.0 * struct.step**3 * eps_env)
            
            if self.radiative_correction:
                norm_rad = 1j * 2.0 * struct.normalization * (k0**3)/3.0 * np.ones(len(norm_nonrad))
                cnorm = norm_nonrad + norm_rad
            else:
                cnorm = norm_nonrad
        
        self_term_tensors_EE = np.zeros([len(norm_nonrad), 3, 3], dtype=self.dtypec)
        self_term_tensors_EE[:,0,0] = cnorm
        self_term_tensors_EE[:,1,1] = cnorm
        self_term_tensors_EE[:,2,2] = cnorm
        
        return self_term_tensors_EE
        
    
    def getSelfTermHE(self, wavelength, struct):
        eps_env = self.getEnvironmentIndices(wavelength, struct.geometry)
        struct.setWavelength(wavelength)
        
        self_term_tensors_HE = np.zeros([len(eps_env), 3, 3], dtype=self.dtypec)
        
        return self_term_tensors_HE
        
        
    def getPolarizabilityTensor(self, wavelength, struct):
        eps_env = self.getEnvironmentIndices(wavelength, struct.geometry)
        struct.setWavelength(wavelength)
        normalization = struct.normalization
        eps = struct.epsilon_tensor 
        
        vcell_norm = struct.step**3 / float(normalization)
        
        eps_env_tensor = np.zeros(eps.shape, dtype=self.dtypec)
        eps_env_tensor[:,0,0] = eps_env
        eps_env_tensor[:,1,1] = eps_env
        eps_env_tensor[:,2,2] = eps_env
        
        ## --- isotropic polarizability
        alphatensor = np.asfortranarray((eps - eps_env_tensor) * 
                                      vcell_norm / (4.0 * np.pi), dtype=self.dtypec)
        
        return alphatensor



#%% test
if __name__ == '__main__':
    from threadpoolctl import threadpool_limits
    from pyGDM2 import structures
    from pyGDM2 import materials
    from pyGDM2 import fields

    from pyGDM2 import core as core_old
    from pyGDM2 import core_py as core
    from pyGDM2 import visu
    from pyGDM2 import tools
    from pyGDM2 import linear

    from pyGDM2 import propagators_periodic_slow
    # from periodic_propagators import G_123_quasistatic_periodic


    from pyGDM2 import linear
    
    
    threadpool_limits(limits=4, user_api='blas')




    ## --------------- Setup structure
    mesh = 'cube'
    step = 25.0

    ## block 1: gold
    geom1 = structures.rect_wire(step, L=10,H=3,W=3, mesh=mesh)
    geom1 = structures.rect_wire(step, L=20,H=4,W=10, mesh=mesh)
    mat1 = len(geom1)*[materials.gold()]
    # mat1 = len(geom1)*[materials.silver()]
    mat1 = len(geom1)*[materials.dummy(3.5)]

    geom1.T[2] += 10

    geometry = geom1
    material = mat1 


    geometry = structures.center_struct(geometry)

    struct = structures.struct(step, geometry, material)

    ## incident field
    # field_generator = fields.planewave
    # kwargs = dict(theta=0)

    field_generator = fields.evanescent_planewave
    field_generator = fields.plane_wave
    kwargs = dict(E_s=0.3, E_p=1, inc_angle=25)


    wavelengths = [600]
    efield = fields.efield(field_generator, wavelengths=wavelengths, kwargs=kwargs)

    print("N_dp:", len(geometry))


    ## simulation initialization
    ## --- isolated structure
    n1 = 1.0
    n2 = 1.0
    dyads_single = propagators.DyadsQuasistatic123(n1=n1, n2=n2, spacing=1E9)
    sim1 = core.simulation(struct, efield, dyads_single)
    sim1.scatter(method='cupy')

    ## --- dyads: periodic
    cutoff=30
    I_nf_2 = []
    I_nf_3 = []
    cutofflist = np.arange(1,20,2)
    if 1:
    # for cutoff in cutofflist:
        print(cutoff)
        
        P = 800
        
        ## 1D periodic
        dyads_periodic_3 = propagators_periodic_slow.DyadsQuasistaticPeriodic123(u=np.array([80, 10, 0]), cutoff_u=cutoff, n1=n1, n2=n2, spacing=1E9)
        dyads_periodic_3 = propagators_periodic_slow.DyadsQuasistaticPeriodic123(
            u=np.array([P, 0, 0]), cutoff_u=cutoff, 
            v=np.array([0, P, 0]), cutoff_v=cutoff, 
            n1=n1, spacing=1E9)
        sim2 = core.simulation(struct, efield, dyads=dyads_periodic_3)
    
        ## new implementation 
        dyads_periodic_3_f = DyadsQuasistaticPeriodic123(u=np.array([80, 10, 0]), cutoff_u=cutoff, n1=n1, n2=n2, spacing=1E9)
        dyads_periodic_3_f = DyadsQuasistaticPeriodic123(
            u=np.array([P, 0, 0]), cutoff_u=cutoff, 
            v=np.array([0, P, 0]), cutoff_v=cutoff,
            n1=n1, spacing=1E9, n_cpu=-1)
        sim3 = core.simulation(struct, efield, dyads=dyads_periodic_3_f)
        # dyads_periodic_81 = propagators.G_123_quasistatic_periodic(u=np.array([1000, 0, 0]), cutoff_u=40)
        # sim3 = core.simulation(struct, efield, dyads=dyads_periodic_81)
    
        
    
        # visu.structure(sim1)
        ##%%
        # sim2.scatter(method='cupy')
        sim3.scatter(method='cupy')
        
        ##%%
        import matplotlib.pyplot as plt
        plt.figure(figsize=(15,5))
        plt.subplot(131)
        visu.vectorfield_by_fieldindex(sim1, 0, show=0)
        plt.subplot(132)
        visu.vectorfield_by_fieldindex(sim2, 0, show=0)
        plt.subplot(133)
        visu.vectorfield_by_fieldindex(sim3, 0, show=0)
        plt.show()
        
        r_probe = tools.generate_NF_map(-100, 100, 21, 0, 0, 1, 200)
        print ('calc NF, sim2...')
        Es, Et, Bs, Bt = linear.nearfield(sim2, 0, r_probe)
        I2=np.sum(np.abs(Et.T[3:]), axis=0)
        print ('calc NF, sim3...')
        Es, Et, Bs, Bt = linear.nearfield(sim3, 0, r_probe)
        I3=np.sum(np.abs(Et.T[3:]), axis=0)
        
        plt.plot(I2)
        plt.plot(I3)
        
        I_nf_2.append(I2)
        I_nf_3.append(I3)

#%%
    I_nf_2 = np.array(I_nf_2)
    I_nf_3 = np.array(I_nf_3)
    
    plt.subplot(131)
    plt.imshow(I_nf_2)
    plt.colorbar()
    plt.subplot(132)
    plt.imshow(I_nf_3)
    plt.colorbar()
    plt.subplot(133)
    plt.imshow((I_nf_3-I_nf_2)/I_nf_3, cmap='bwr')
    plt.colorbar()
    plt.show()
    
    Es, Et, Bs, Bt = linear.nearfield(sim1, 0, r_probe)
    I1=np.sum(np.abs(Et.T[3:]), axis=0)
    plt.plot(I1)
    plt.show()
    #%% test convergence
    


    x = 31.
    y = 51.
    z = 15.
    
    wavelength = 550.
    eps1= eps2 = eps3 = complex(1)
    spacing = 10000.
    k_x = 0.0
    
    u=np.array([0., 400, 0])
    v=np.array([400, 0., 0])
    # v=np.array([0, 0, 0])
    
    
    
    Gtest = []
    Gtest2 = []
    for i in range(1, 101):
        
        cutoff_u = cutoff_v = i
        if np.linalg.norm(v) == 0:
            cutoff_v=0
        
        
        R1 = np.array([0,0,0])
        R2 = np.array([x,y,z])
        xx, yy, zz, xy, xz, yx, yz, zx, zy = G0_periodic_123(
                        R1, R2, wavelength, eps1, eps2, eps3, 
                        spacing, k_x, cutoff_u, cutoff_v, u, v
                        )
        _G = np.array([[xx,xy,xz], [yx,yy,yz], [zx,zy,zz]], dtype=np.complex64)
        
        xx, yy, zz, xy, xz, yx, yz, zx, zy = G0_periodic_123_direct_sum(
                        R1, R2, wavelength, eps1, eps2, eps3, 
                        spacing, k_x, cutoff_u, cutoff_v, u, v
                        )
        _G2 = np.array([[xx,xy,xz], [yx,yy,yz], [zx,zy,zz]], dtype=np.complex64)

        Gtest.append(_G)
        Gtest2.append(_G2)
        
        
    
    Gtest = np.array(Gtest)
    Gtest2 = np.array(Gtest2)
    # Gtest = np.abs(Gtest) / np.linalg.norm(np.abs(Gtest[10:]), axis=(1,2)).max()
    # Gtest2 = np.abs(Gtest2) / np.linalg.norm(np.abs(Gtest2[10:]), axis=(1,2)).max()
    
    
    idx = [0,1]
    # mv_avg = moving_average(Gtest[:,idx[0],idx[1]], n=n_mvavg)
    # plt.plot(mv_avg[:])
    plt.plot(Gtest[1:,idx[0],idx[1]].real, color='C0', label='moving avg.')
    plt.plot(Gtest2[1:,idx[0],idx[1]].real, color='C1', label='simple sum')
    plt.axhline(np.mean(Gtest[-10:, idx[0],idx[1]].real), dashes=[3,3], color='C0', lw=1, label='last 10 average')
    plt.axhline(np.mean(Gtest2[-10:, idx[0],idx[1]].real), dashes=[3,3], color='C1', lw=1, label='last 10 average')
    # plt.ylim(-0.5,0.5)
    plt.legend()
    plt.xlabel('cutoff period')
    plt.ylabel('Re(Gxy)')
    plt.show()
    #%% test 2
    ### --- 3D periodic Dyads - until now homogeneous environment only, normal incidence only
    @numba.njit(parallel=True, cache=True)
    def G0_periodic_123cumsum(R1, R2, wavelength, 
                        eps1=1.0+0j, eps2=1.0+0j, eps3=1.0+0j, spacing=5000, 
                        k_x=0.0, N_u=0, N_v=0, 
                        u=np.array([0., 0., 0.]), v=np.array([0., 0., 0.])):
        xx = np.zeros((N_u*2 + 1, N_v*2 + 1), dtype=np.complex128)
        yy = np.zeros((N_u*2 + 1, N_v*2 + 1), dtype=np.complex128)
        zz = np.zeros((N_u*2 + 1, N_v*2 + 1), dtype=np.complex128)
        xy = np.zeros((N_u*2 + 1, N_v*2 + 1), dtype=np.complex128)
        xz = np.zeros((N_u*2 + 1, N_v*2 + 1), dtype=np.complex128)
        yx = np.zeros((N_u*2 + 1, N_v*2 + 1), dtype=np.complex128)
        yz = np.zeros((N_u*2 + 1, N_v*2 + 1), dtype=np.complex128)
        zx = np.zeros((N_u*2 + 1, N_v*2 + 1), dtype=np.complex128)
        zy = np.zeros((N_u*2 + 1, N_v*2 + 1), dtype=np.complex128)
        
        for _u_i in numba.prange(1, 2*(N_u+1)):
            u_i = (_u_i%2-0.5)*2 * _u_i//2
            for _v_i in numba.prange(1, 2*(N_v+1)):
                v_i = (_v_i%2-0.5)*2 * _v_i//2 
                _R1 = R1 + u*u_i + v*v_i     # position of emitter-copy from periodic cell [u_i, v_i]
                _xx, _yy, _zz, _xy, _xz, _yx, _yz, _zx, _zy = propagators.G0_EE_123(
                        _R1, R2, wavelength, eps1, eps2, eps3, spacing)
                xx[_u_i-1, _v_i-1] = _xx
                yy[_u_i-1, _v_i-1] = _yy
                zz[_u_i-1, _v_i-1] = _zz
                xy[_u_i-1, _v_i-1] = _xy
                xz[_u_i-1, _v_i-1] = _xz
                yx[_u_i-1, _v_i-1] = _yx
                yz[_u_i-1, _v_i-1] = _yz
                zx[_u_i-1, _v_i-1] = _zx
                zy[_u_i-1, _v_i-1] = _zy
        
        ## calc. mean of moving average of tail of series to dampen oscillations
        # xx = np.mean(moving_average(xx.flatten(), n=N_u*N_v)[2*N_u*N_v:-1])
        # yy = np.mean(moving_average(yy.flatten(), n=N_u*N_v)[2*N_u*N_v:-1])
        # zz = np.mean(moving_average(zz.flatten(), n=N_u*N_v)[2*N_u*N_v:-1])
        # xy = np.mean(moving_average(xy.flatten(), n=N_u*N_v)[2*N_u*N_v:-1])
        # xz = np.mean(moving_average(xz.flatten(), n=N_u*N_v)[2*N_u*N_v:-1])
        # yx = np.mean(moving_average(yx.flatten(), n=N_u*N_v)[2*N_u*N_v:-1])
        # yz = np.mean(moving_average(yz.flatten(), n=N_u*N_v)[2*N_u*N_v:-1])
        # zx = np.mean(moving_average(zx.flatten(), n=N_u*N_v)[2*N_u*N_v:-1])
        # zy = np.mean(moving_average(zy.flatten(), n=N_u*N_v)[2*N_u*N_v:-1])
        
        return xx, yy, zz, xy, xz, yx, yz, zx, zy
        # return np.cumsum(xx), np.cumsum(yy), np.cumsum(zz), \
        #         np.cumsum(xy), np.cumsum(xz), np.cumsum(yx), \
        #         np.cumsum(yz), np.cumsum(zx), np.cumsum(zy)
               
           
    u=np.array([0., 600, 0])
    v=np.array([500, 0., 0])
    n_mvavg = 10
    i0_sample, i1_sample = 10,25
        
    cutoff_u = cutoff_v = 50
    t0=time.time()
    xx, yy, zz, xy, xz, yx, yz, zx, zy = G0_periodic_123cumsum(
                    R1, R2, wavelength, eps1, eps2, eps3, 
                    spacing, k_x, cutoff_u, cutoff_v, u, v
                    )
    print(time.time()-t0)
    
    # test = zx
    # plt.plot(np.cumsum(test.flatten()))
    
    # csum = moving_average(np.cumsum(test.flatten()), n=cutoff_u*cutoff_v)
    # plt.plot(csum)
    # plt.plot(moving_average(test.flatten(), n=cutoff_u*cutoff_v)[10:])
    # plt.axhline(0, color='k')
    # plt.axhline(np.mean(csum[2*cutoff_u*cutoff_v:-1]), color='C0', dashes=[3,3])
    # plt.axvline(2*cutoff_u*cutoff_v, color='k')
    # plt.ylim(-1E-8, 1E-8)
    
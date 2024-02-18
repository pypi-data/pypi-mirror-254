# -*- coding: utf-8 -*-
"""
Created on Sun Apr 3 10:31:42 2022

@author: Clement Majorel

Free space Green's tensors for electric and magnetic dipole and quadrupoles 
"""
import numpy as np
import math
import cmath

## --- free space propagator dipole
def G0_Ep(R1, R2, wavelength, eps):
    """electric field emitted by electric dipole
    R1: dipole position
    R2: evaluation position
    """
    Dx = R2[0] - R1[0]
    Dy = R2[1] - R1[1]
    Dz = R2[2] - R1[2]
    lR = math.sqrt(Dx**2 + Dy**2 + Dz**2)
    
    k = 2*np.pi / wavelength
    cn = cmath.sqrt(eps)
    ck0 = 1j * k * cn
    k2 = k*k*eps
    
    r25 = math.pow((Dx*Dx+Dy*Dy+Dz*Dz), 2.5)
    r2 = math.pow((Dx*Dx+Dy*Dy+Dz*Dz), 2.0)
    r15 = math.pow((Dx*Dx+Dy*Dy+Dz*Dz), 1.5)
    
#!C-------------------------------------------------------------------
    T1XX = -1*(Dy*Dy+Dz*Dz) / r15
    T2XX = (2*Dx*Dx-Dy*Dy-Dz*Dz) / r2
    T3XX = (2*Dx*Dx-Dy*Dy-Dz*Dz) / r25
#!C-------------------------------------------------------------------
    T1XY = Dx*Dy / r15
    T2XY = 3*Dx*Dy / r2
    T3XY = 3*Dx*Dy / r25
#!C-------------------------------------------------------------------
    T1XZ = Dx*Dz / r15
    T2XZ = 3*Dx*Dz / r2
    T3XZ = 3*Dx*Dz / r25
#!C-------------------------------------------------------------------
    T1YY = -(Dx*Dx+Dz*Dz) / r15
    T2YY = (2*Dy*Dy-Dx*Dx-Dz*Dz) / r2
    T3YY = (2*Dy*Dy-Dx*Dx-Dz*Dz) / r25
#!C-------------------------------------------------------------------
    T1YZ = Dy*Dz / r15
    T2YZ = 3*Dy*Dz / r2
    T3YZ = 3*Dy*Dz / r25
#!C------------------------------------------------------------------
    T1ZZ = -(Dx*Dx+Dy*Dy) / r15
    T2ZZ = (2*Dz*Dz-Dx*Dx-Dy*Dy) / r2
    T3ZZ = (2*Dz*Dz-Dx*Dx-Dy*Dy) / r25
    
    CFEXP = cmath.exp(1j*k*cn*lR)
    
    
    ## setting up the tensor
    xx = CFEXP*(T3XX - ck0*T2XX - k2*T1XX) / eps
    yy = CFEXP*(T3YY - ck0*T2YY - k2*T1YY) / eps
    zz = CFEXP*(T3ZZ - ck0*T2ZZ - k2*T1ZZ) / eps
    
    xy = CFEXP*(T3XY - ck0*T2XY - k2*T1XY) / eps
    xz = CFEXP*(T3XZ - ck0*T2XZ - k2*T1XZ) / eps
    
    yz = CFEXP*(T3YZ - ck0*T2YZ - k2*T1YZ) / eps
        
    yx = xy
    zx = xz
    zy = yz
    
    return xx, yy, zz, xy, xz, yx, yz, zx, zy

def G0_Hm(R1, R2, wavelength, eps):
    """magnetic field emitted by magnetic dipole
    R1: dipole position
    R2: evaluation position
    """
    return G0_Ep(R1, R2, wavelength, eps)




def G0_Hp(R1, R2, wavelength, eps):
    """magnetic field emitted by electric dipole
    R1: dipole position
    R2: evaluation position
    """
    # eps: environment index
    Dx = R2[0] - R1[0]
    Dy = R2[1] - R1[1]
    Dz = R2[2] - R1[2]
    lR2 = (Dx**2 + Dy**2 + Dz**2)
    
    k0 = 2*np.pi / wavelength
    k02n = cmath.sqrt(eps) * k0**2
#-----------------------------------------------------------------
    T2XY = Dz/lR2
    T3XY = Dz/lR2**1.5
#-----------------------------------------------------------------
    T2XZ = -Dy/lR2
    T3XZ = -Dy/lR2**1.5
#-----------------------------------------------------------------
    T2YZ = Dx/lR2
    T3YZ = Dx/lR2**1.5
#-----------------------------------------------------------------
    CFEXP = -1*cmath.exp(1j*k0*cmath.sqrt(eps)*math.sqrt(lR2))
    
    xx = 0
    yy = 0
    zz = 0
    
    xy = CFEXP * (1j*k0*T3XY + k02n*T2XY)
    xz = CFEXP * (1j*k0*T3XZ + k02n*T2XZ)
    yz = CFEXP * (1j*k0*T3YZ + k02n*T2YZ)

    yx = -xy
    zx = -xz
    zy = -yz
    
    return xx, yy, zz, xy, xz, yx, yz, zx, zy



def G0_Em(R1, R2, wavelength, eps):
    return -1*np.array(G0_Hp(R1, R2, wavelength, eps))

    


# =============================================================================
# Quadrupole propagator 
# =============================================================================
## --- free space propagator electric quadrupole
def G0_Eqe(R1, R2, wavelength, eps):
    """electric field emitted by electric quadrupole
    R1: dipole position
    R2: evaluation position
    """
    Dx = R2[0] - R1[0]
    Dy = R2[1] - R1[1]
    Dz = R2[2] - R1[2]
    lR = math.sqrt(Dx**2 + Dy**2 + Dz**2)
    
    k = 2*np.pi / wavelength
    cn = cmath.sqrt(eps)
    ck0 = 1j * k * cn
    k2 = k*k*eps
    
    r3 = math.pow((Dx*Dx+Dy*Dy+Dz*Dz), 3)
    r25 = math.pow((Dx*Dx+Dy*Dy+Dz*Dz), 2.5)
    r2 = math.pow((Dx*Dx+Dy*Dy+Dz*Dz), 2.0)
    r15 = math.pow((Dx*Dx+Dy*Dy+Dz*Dz), 1.5)
    
#!C-------------------------------------------------------------------
    T1XX = -1*(Dy*Dy+Dz*Dz) / r15
    T2XX = (3*Dx*Dx-3*Dy*Dy-3*Dz*Dz) / r2
    T3XX = (9*Dx*Dx-6*Dy*Dy-6*Dz*Dz) / r25
    T4XX = (9*Dx*Dx-6*Dy*Dy-6*Dz*Dz) / r3
#!C-------------------------------------------------------------------
    T1XY = Dx*Dy / r15
    T2XY = 6*Dx*Dy / r2
    T3XY = 15*Dx*Dy / r25
    T4XY = 15*Dx*Dy / r3
#!C-------------------------------------------------------------------
    T1XZ = Dx*Dz / r15
    T2XZ = 6*Dx*Dz / r2
    T3XZ = 15*Dx*Dz / r25
    T4XZ = 15*Dx*Dz / r3
#!C-------------------------------------------------------------------
    T1YY = -(Dx*Dx+Dz*Dz) / r15
    T2YY = (3*Dy*Dy-3*Dx*Dx-3*Dz*Dz) / r2
    T3YY = (9*Dy*Dy-6*Dx*Dx-6*Dz*Dz) / r25
    T4YY = (9*Dy*Dy-6*Dx*Dx-6*Dz*Dz) / r3
#!C-------------------------------------------------------------------
    T1YZ = Dy*Dz / r15
    T2YZ = 6*Dy*Dz / r2
    T3YZ = 15*Dy*Dz / r25
    T4YZ = 15*Dy*Dz / r3
#!C------------------------------------------------------------------
    T1ZZ = -(Dx*Dx+Dy*Dy) / r15
    T2ZZ = (3*Dz*Dz-3*Dx*Dx-3*Dy*Dy) / r2
    T3ZZ = (9*Dz*Dz-6*Dx*Dx-6*Dy*Dy) / r25
    T4ZZ = (9*Dz*Dz-6*Dx*Dx-6*Dy*Dy) / r3
    
    CFEXP = cmath.exp(1j*k*cn*lR)
    
    
    ## setting up the tensor
    xx = CFEXP*(T4XX - ck0*T3XX - k2*T2XX + ck0*k2*T1XX) / (6*eps)
    yy = CFEXP*(T4YY - ck0*T3YY - k2*T2YY + ck0*k2*T1YY) / (6*eps)
    zz = CFEXP*(T4ZZ - ck0*T3ZZ - k2*T2ZZ + ck0*k2*T1ZZ) / (6*eps)
    
    xy = CFEXP*(T4XY - ck0*T3XY - k2*T2XY + ck0*k2*T1XY) / (6*eps)
    xz = CFEXP*(T4XZ - ck0*T3XZ - k2*T2XZ + ck0*k2*T1XZ) / (6*eps)
    
    yz = CFEXP*(T4YZ - ck0*T3YZ - k2*T2YZ + ck0*k2*T1YZ) / (6*eps)
        
    yx = xy
    zx = xz
    zy = yz
    
    return xx, yy, zz, xy, xz, yx, yz, zx, zy


def G0_Hqe(R1, R2, wavelength, eps):
    """magnetic field emitted by electric quadrupole
    R1: dipole position
    R2: evaluation position
    """
    # eps: environment index
    Dx = R2[0] - R1[0]
    Dy = R2[1] - R1[1]
    Dz = R2[2] - R1[2]
    lR2 = (Dx**2 + Dy**2 + Dz**2)
    
    k0 = 2*np.pi / wavelength
    k02n = cmath.sqrt(eps) * k0**2
    k2 = eps * k0**2
#-----------------------------------------------------------------
    T2XY = -Dz/lR2
    T3XY = -Dz/lR2**1.5
    T4XY = -Dz/lR2**2
#-----------------------------------------------------------------
    T2XZ = Dy/lR2
    T3XZ = Dy/lR2**1.5
    T4XZ = Dy/lR2**2
#-----------------------------------------------------------------
    T2YZ = -Dx/lR2
    T3YZ = -Dx/lR2**1.5
    T4YZ = -Dx/lR2**2
#-----------------------------------------------------------------
    CFEXP = cmath.exp(1j*k0*cmath.sqrt(eps)*math.sqrt(lR2))
    
    xx = 0
    yy = 0
    zz = 0
    
    xy = CFEXP * (-1j*k0*k2*T2XY + 3*k02n*T3XY + 3j*k0*T4XY) / 6
    xz = CFEXP * (-1j*k0*k2*T2XZ + 3*k02n*T3XZ + 3j*k0*T4XZ) / 6
    yz = CFEXP * (-1j*k0*k2*T2YZ + 3*k02n*T3YZ + 3j*k0*T4YZ) / 6

    yx = -xy
    zx = -xz
    zy = -yz
    
    return xx, yy, zz, xy, xz, yx, yz, zx, zy


def G0_Eqm(R1, R2, wavelength, eps):
    """electric field emitted by magnetic quadrupole
    R1: dipole position
    R2: evaluation position
    """
    return -1*np.array(G0_Hqe(R1, R2, wavelength, eps))


def G0_Hqm(R1, R2, wavelength, eps):
    """magnetic field emitted by magnetic quadrupole
    R1: dipole position
    R2: evaluation position
    """
    return np.array(G0_Eqe(R1, R2, wavelength, eps))



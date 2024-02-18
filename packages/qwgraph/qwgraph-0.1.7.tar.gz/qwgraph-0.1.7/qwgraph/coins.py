import numpy as np
from math import pi 

def generalized_coin(theta, phi, lbd):
	return np.array([[np.cos(theta) , -np.exp(1j*lbd)*np.sin(theta)],
		[np.exp(1j*lbd)*np.sin(theta) , np.exp(1j*(lbd+phi))*np.cos(theta)]],dtype=complex)

def phase_shift(phi):
	return np.array([
		[1,0],
		[0,np.exp(1j*phi)]],dtype=complex)

###############################################
##                 Pauli Gates               ##
###############################################
I = np.array([[1,0],[0,1]],dtype=complex) # Identity
X = np.array([[0,1],[1,0]],dtype=complex) # X pauli matrix
Z = np.array([[1,0],[0,-1]],dtype=complex) # Z pauli matrix


###############################################
##                Common Gates               ##
###############################################
H = np.array([[1,1],[1,-1]],dtype=complex)/np.sqrt(2) # Hadamard
S = np.array([[1,0],[0,1j]],dtype=complex)
T = np.array([[1,0],[0,np.exp(1j*pi/4)]],dtype=complex)
Cx = np.array([[1,1j],[1j,1]],dtype=complex)/np.sqrt(2)
Cy = np.array([[1,-1j],[-1j,1]],dtype=complex)/np.sqrt(2)


import numpy as np

def update_finite(G,L,U,chi_max,site,Nsites):
	d = U[site].shape[0]
	#site indices
	if site==(Nsites-1):
		return
		A=site; B=0;
	else:
		A = site; B = site+1
	
	#construct Theta
	
	theta=np.tensordot(np.diag(L[A-1,:]),G[A,:,:,:],axes=(1,1))
	#after fixing index A, G becomes G[d,chi,chi]
	#note that matrix theta is now theta=array(chi,d,chi)
	theta=np.tensordot(theta,np.diag(L[A,:]),axes=(2,0))
	theta=np.tensordot(theta,G[B,:,:,:],axes=(2,1))
	theta=np.tensordot(theta,np.diag(L[B,:]),(3,0))
	
	# Apply U
	theta = np.tensordot(theta,U[site][:,:,:,:],axes=([1,2],[0,1]));

	# SVD
	theta = np.reshape(np.transpose(theta,(2,0,3,1)),(d*chi_max,d*chi_max));
	X, Y, Z = np.linalg.svd(theta); Z = Z.T

	# Truncate and normalize the Schmidt values
	L[A,0:chi_max]=Y[0:chi_max]/np.sqrt(sum(Y[0:chi_max]**2))

	error = sum(Y[chi_max:]**2)/sum(Y**2)

	#print("error test", sum(Y**2))
	
	#Truncate X tensor and reshape it
	X=np.reshape(X[0:d*chi_max,0:chi_max],(d,chi_max,chi_max))
	#Get G from X.
	G[A,:,:,:]=np.transpose(np.tensordot(np.diag(L[A-1,:]**(-1)),X,axes=(1,1)),(1,0,2))

	Z=np.transpose(np.reshape(Z[0:d*chi_max,0:chi_max],(d,chi_max,chi_max)),(0,2,1))
	G[B,:,:,:]=np.tensordot(Z,np.diag(L[B,:]**(-1)),axes=(2,0))
	
	return error

def entanglement_entropy(L,Nsites):
	" Returns the half chain entanglement entropy "
	S=[]
	ibond=int(Nsites/2+1)
	x = L[ibond] ** 2
	S.append(-np.inner(np.log(x.real),x.real))
	return(S)

def bond_expectation_value(G,L,Op,Nsites):
	#" Expectation value for a bond operator "
	E=[]
	B=[]
	for site in range(0, Nsites):
		B.append(np.tensordot(G[site],np.diag(L[site]),axes=(2,0)))
	
	for ibond in range(0,Nsites-1):
		BB = np.tensordot(B[ibond],B[ibond+1],axes=(2,1))
		sBB = np.tensordot(np.diag(L[ibond-1]),BB,axes=(1,1))
		C = np.tensordot(sBB,Op,axes=([1,2],[2,3]))
		sBB=np.conj(sBB)
		E.append(np.squeeze(np.tensordot(sBB,C,axes=([0,3,1,2],[0,1,2,3]))).item())
	return E

def site_expectation_value(G,L,Op,Nsites):
	#" Expectation value for a site operator "
	E=[]
	B=[]
	for site in range(0,Nsites):
		B.append(np.tensordot(G[site],np.diag(L[site]),axes=(2,0)));
		
	for isite in range(0,Nsites):
		sB = np.tensordot(np.diag(L[isite-1]),B[isite],axes=(1,1))+0.j

		Norm = np.sum(sB * np.conj(sB))

		C = np.tensordot(sB,Op,axes=(1,0))
		sB=sB.conj()
		E.append(np.squeeze(np.tensordot(sB,C,axes=([0,1,2],[0,2,1]))).item()/Norm)


	return(E)
	
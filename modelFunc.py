import numpy as np

def u_exact(xin, yin, zin, lam=1):
    ux = np.sin(2*np.pi*yin)*(-1+np.cos(2*xin*np.pi)) + 1/(1+lam)*np.sin(np.pi*xin)*np.sin(np.pi*yin)
    uy = np.sin(2*np.pi*xin)*(1-np.cos(2*yin*np.pi)) + 1/(1+lam)*np.sin(np.pi*xin)*np.sin(np.pi*yin)
    uz = 0.0
    return (ux, uy, uz)

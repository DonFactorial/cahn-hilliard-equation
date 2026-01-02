import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

def rhsfunc(t,yfvec,D,gamma,K,n):
    yfvec = yfvec[:yfvec.size//2]+1j*yfvec[yfvec.size//2:]
    yf = yfvec.reshape((n,n),order='F')
    y = np.fft.ifft2(yf)
    c = D*-K*(np.fft.fft2(y**3-y-gamma*np.fft.ifft2(-K*yf)))
    c = c.reshape(n**2,order='F')
    return np.concatenate((np.real(c),np.imag(c)))

# Model parameters
D = 0.5
gamma = 0.1

# Simulation parameters
L = 20
tspan = np.linspace(0,50,150)
n = 2**6
x = np.linspace(-L/2,L/2,n+1)
x = x[:-1]
y = x
X, Y = np.meshgrid(x,y)

# Initial condition
c0 = np.random.rand(n,n)
c0 = np.tanh(10*(c0-0.5))
c0 = np.fft.fft2(c0).reshape(n**2,order='F')
c0 = np.concatenate((np.real(c0),np.imag(c0)))

# Set up domain in Fourier space
kx = (2*np.pi/L)*np.concatenate((np.arange(0, n//2), np.arange(-n//2, 0)))
kx[0] = 10**-6
ky = kx
KX, KY = np.meshgrid(kx, ky)
K = KX**2 + KY**2
Kvec = K.reshape(n**2, order='F')

# Solve in Fourier space
t_start = time.perf_counter()
sol = integrate.solve_ivp(rhsfunc, (tspan[0], tspan[-1]), y0=c0, t_eval=tspan, args=(D,gamma,K,n))
t_end = time.perf_counter()
print(f"Time: {t_end-t_start}")

# Make animation with solution
fig, ax = plt.subplots(1,2, width_ratios=[0.95, 0.05])
ax[0].set_title(f"Periodic B.C., $D={D}$, $\\gamma={gamma}$")
ims = []
for i in range(sol.t.size):
    s = sol.y[:,i]
    s = s[:s.size//2]+1j*s[s.size//2:]
    im = ax[0].imshow(np.real(np.fft.ifft2(s.reshape((n,n), order='F'))), cmap=plt.colormaps["RdBu"], animated=True)
    if i==0:
        im = ax[0].imshow(np.real(np.fft.ifft2(s.reshape((n,n), order='F'))), cmap=plt.colormaps["RdBu"])
    ax[0].axis("off")
    fig.colorbar(mappable=im, cax=ax[1])
    ims.append([im])
    
ani = animation.ArtistAnimation(fig, ims, interval=100, blit=True, repeat_delay=1000)
ani.save('CahnHilliard.gif')
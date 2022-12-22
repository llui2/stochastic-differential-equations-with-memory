# Stochastic differential equations with memory #

import numpy as np

# Parameters
N = 5 # Persistent Brownian walkers
L = 2 # Box size
D = 10 # Diffusion constant

dt = 0.001 # Time step
T = 1 # Total evolution time
n_step = int(T/dt) # Total nubmber of time steps

tau = 1 # Correlation time

# Walkers positions
x = np.zeros((N, n_step))+L/2
y = np.zeros((N, n_step))+L/2

# Walkers positions with periodic boundary conditions
x_PBC = np.zeros((N, n_step))+L/2
y_PBC = np.zeros((N, n_step))+L/2

# Non-Markovian noise
xi_x = np.zeros((N, n_step))
xi_y = np.zeros((N, n_step))

# Initial conditions for the non-Markovian noise that verify the autocorrelation function
xi_x[:,0] = np.sqrt(D/tau)
xi_y[:,0] = np.sqrt(D/tau)

# Calculate the trajectories
for i in range(n_step):
       # Calulate the non-markovian noise
       xi_x[:,i] = (1-dt/tau)*xi_x[:,i-1] + np.sqrt(2*D/tau**2)*np.sqrt(dt)*np.random.randn(N)
       xi_y[:,i] = (1-dt/tau)*xi_y[:,i-1] + np.sqrt(2*D/tau**2)*np.sqrt(dt)*np.random.randn(N)

       # Update the positions
       x[:,i] = x[:,i-1] + xi_x[:,i]*dt
       y[:,i] = y[:,i-1] + xi_y[:,i]*dt

       # Periodic boundary conditions
       x_PBC[:,i] = np.mod(x[:,i], L)
       y_PBC[:,i] = np.mod(y[:,i], L)

# Save the trajectories
f = open('data_1.dat', 'w')
for i in range(N):
       for j in range(n_step):
              f.write(f"{x[i,j]} {y[i,j]} \n")
       f.write(f"\n \n")

f.close()

import os
os.system(f"gnuplot -e N={N} -e L={L} figure_1.gnu")
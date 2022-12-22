# Stochastic differential equations with memory #

import numpy as np

# Parameters
N = 1000 # Persistent Brownian walkers
L = 100 # Box size
D = 10 # Diffusion constant

dt = 0.01 # Time step
T = 100 # Total evolution tim

n_step = int(T/dt) # Total nubmber of time steps

tau = 100 # Correlation time

# Walkers positions
x = np.zeros((N, n_step))
y = np.zeros((N, n_step))

# Walkers positions with periodic boundary conditions
x_PBC = np.zeros((N, n_step))
y_PBC = np.zeros((N, n_step))

# Non-Markovian noise
xi_x = np.zeros((N, n_step))
xi_y = np.zeros((N, n_step))

# Initial conditions for the non-Markovian noise that verify the autocorrelation function
xi_x[:,0] = np.sqrt(D/tau)
xi_y[:,0] = np.sqrt(D/tau)

# Calculate the trajectories
for i in range(1,n_step):
       # Calulate the non-markovian noise
       xi_x[:,i] = (1-dt/tau)*xi_x[:,i-1] + np.sqrt(2*D/tau**2)*np.sqrt(dt)*np.random.randn(N)
       xi_y[:,i] = (1-dt/tau)*xi_y[:,i-1] + np.sqrt(2*D/tau**2)*np.sqrt(dt)*np.random.randn(N)

       # Update the positions
       x[:,i] = x[:,i-1] + xi_x[:,i]*dt
       y[:,i] = y[:,i-1] + xi_y[:,i]*dt
       
       # Periodic boundary conditions
       x_PBC[:,i] = np.mod(x[:,i], L)
       y_PBC[:,i] = np.mod(y[:,i], L)


# Compute the correlation function \sum_{i=1}^N \langle xi_i(t) xi_i(0) \rangle / N
correlation = np.zeros(n_step)
for i in range(n_step):
       correlation[i] = np.mean(xi_x[:,i]*xi_x[:,0] + xi_y[:,i]*xi_y[:,0])

# Compute the theoretical correlation function
correlation_theory = np.zeros(n_step)
for i in range(n_step):
       correlation_theory[i] = np.exp(-i*dt/tau)*2*D/tau


# Save the Mean Square Displacement 
f = open('data_3.dat', 'w')
for i in range(n_step):
       f.write(f"{i*dt} {correlation[i]} {correlation_theory[i]} \n")
f.close()

import os
os.system(f"gnuplot -e tau={tau} figure_3.gnu")

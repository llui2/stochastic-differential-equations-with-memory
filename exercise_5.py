# Stochastic differential equations with memory #

import numpy as np

# Parameters
N = 1000 # Persistent Brownian walkers
L = 100 # Box size
D = 10 # Diffusion constant

dt = 0.01 # Time step
T = 1000 # Total evolution tim

n_step = int(T/dt) # Total nubmber of time steps

corre_times = [1,3,10,30,100] # Correlation times

F = 1e-2 # Force value

f = open('data_5.dat', 'w')
f = open('data_5.dat', 'a')

for tau in corre_times:
       
       print(f"tau = {tau}")

       # Walkers positions
       x = np.zeros((N, n_step))+L/2
       y = np.zeros((N, n_step))+L/2

       # epsilon value array
       e_x = 2*np.random.randint(2, size=N)-1

       # Walkers positions with periodic boundary conditions
       x_PBC = np.zeros((N, n_step))+L/2
       y_PBC = np.zeros((N, n_step))+L/2

       # Non-Markovian noise
       xi_x = np.zeros((N, n_step))
       xi_y = np.zeros((N, n_step))

       # Initial conditions for the non-Markovian noise that verify the autocorrelation function
       xi_x[:,0] = np.sqrt(D/tau)*(2*np.random.randint(2, size=N)-1)
       xi_y[:,0] = np.sqrt(D/tau)*(2*np.random.randint(2, size=N)-1)

       # Calculate the trajectories
       for i in range(1,n_step):
              # Calulate the non-markovian noise
              xi_x[:,i] = (1-dt/tau)*xi_x[:,i-1] + np.sqrt(2*D/tau**2)*np.sqrt(dt)*np.random.randn(N)
              xi_y[:,i] = (1-dt/tau)*xi_y[:,i-1] + np.sqrt(2*D/tau**2)*np.sqrt(dt)*np.random.randn(N)

              # Update the positions
              x[:,i] = x[:,i-1] + xi_x[:,i]*dt + F*e_x*dt
              y[:,i] = y[:,i-1] + xi_y[:,i]*dt
              
              # Periodic boundary conditions
              x_PBC[:,i] = np.mod(x[:,i], L)
              y_PBC[:,i] = np.mod(y[:,i], L)

       # Compute the mean square displacement of the x component
       MSD_x = np.zeros(n_step)
       for i in range(n_step):
              MSD_x[i] = np.mean((x[:,i]-x[:,0])**2)

       # Compute the displacement of the x component
       d_x = np.zeros(n_step)
       for i in range(n_step):
              d_x[i] = abs(np.mean(e_x*(x[:,i]-x[:,0])))

       mu = d_x[n_step-1]/(F*T)
       Dif = MSD_x[n_step-1]/(2*T)

       # Save the Mean Square Displacement 
       f.write(f"{tau} {mu} {Dif} \n")

f.close()
       
import os
os.system(f"gnuplot figure_6.gnu")

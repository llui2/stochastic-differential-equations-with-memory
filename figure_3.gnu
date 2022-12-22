set key top right 
set title ""
set xlabel ""
set ylabel "" 

set key left

plot   "data_3.dat" u 1:2 w lines lw 2 t "Simulation",\
       "data_3.dat" u 1:3 w lines lw 2 t "Theory"
       
pause -1
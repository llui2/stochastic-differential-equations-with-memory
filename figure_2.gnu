set key top right 
set title ""
set xlabel ""
set ylabel "" 

set key left

set logscale 
set format x "10^{%T}"
set format y "10^{%T}"

plot   "data_2.dat" u 1:2 w lines lw 2 lc "red" t "Simulation",\
       "data_2.dat" u 1:3 w lines lw 1 dt 2 lc "blue" t "Theory"
       
pause -1
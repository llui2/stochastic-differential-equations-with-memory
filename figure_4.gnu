set key top right 
set title "MSD_x"
set xlabel ""
set ylabel "" 

set key bottom right

set logscale
set format x "10^{%T}"
set format y "10^{%T}"

#set yrange [1e-2:]

f = '0 0.001 0.01 0.1 1'

plot for [n=0:4] "data_4.dat" i n u 1:2 w lines lw 2 t sprintf("f = ".word(f,n+1))
       
pause -1
set key top right 
set title ""
set xlabel ""
set ylabel "" 

set key right top

set logscale
set format x "10^{%T}"
set format y "10^{%T}"

set yrange [1e-1:1e2]

plot "data_5.dat" u 1:3 w linespoints lw 2 pt 2 t "D", "data_5.dat" u 1:(abs($2)) w linespoints lw 2 pt 2 t "mu"
           
pause -1
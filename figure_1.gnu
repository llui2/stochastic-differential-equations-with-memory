set size ratio -1

set key top right 
set title ""
set xlabel ""
set ylabel "" 

set xrange [0:L]
set yrange [0:L]

plot for [j=0:N] "data_1.dat" i j u 1:2 w lines notitle
pause -1
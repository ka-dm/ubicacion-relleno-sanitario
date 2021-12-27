% parametros
int: n; % tamaño de la region
int: m; % cantidad de ciudades
array[int,int] of int: ciudades;
int: tam =  length(ciudades);

% variables 
var int: x;
var int: y;

% restricciones (constraints)
constraint x >= 0;
constraint y >= 0;
constraint x <= n;
constraint y <= n;

% d(P,C) = |x2-x1|+|y2-y1| donde P y C son coordenadas cartesianas
% el objetivo es min(d)

% objetivo
var int: retsult = sum([(abs(x - ciudades[i,1]) + abs(y - ciudades[i,2]))| i in 1..m]);
solve minimize retsult;

output [
  "Solution: ", show(retsult),"\n",
  "P(", show(x),",",show(y), ")\n",
  ];

%output["tam = ",  show(tam), " ", show(x)];
%output[ show(ciudades[i,1])++" " | i in 1..m];
% Parametros
int: n; % tamaño de la region
int: m; % cantidad de ciudades
array[1..m,1..2] of int: ciudades;

% Variables 
var int: f;
var int: x;
var int: y;
 
% Restricciones
constraint x >= 0;
constraint y >= 0;
constraint x <= n;
constraint y <= n;
constraint forall (i in 1..m) (ciudades[i,1] != x /\ ciudades[i,2] != y); 

% Declacion de funciones
function var int: valAbs(var int: x) =
          abs(x);
          
function var int: manhattan(var int: x1, var int: y1, 
                              var int: x2, var int: y2) =
          abs(x2 - x1) + abs(y2 - y1);
          
% Objetivo
array[int] of var int: dist = [manhattan(x,y,ciudades[i,1],ciudades[i,2]) | i in 1..m];
constraint f = min(dist);
solve maximize f;

output [
 % "Solucion: ", show(dist),"\n",
  "P(", show(x),",",show(y), ")\n",
  %"Rango = ", show(rango),"\n",
  "F = ", show(f),"\n",
  ];
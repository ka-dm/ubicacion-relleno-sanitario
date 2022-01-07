% Parametros
int: n; % tamaño de la region
int: m; % cantidad de ciudades
array[1..m,1..2] of int: ciudades;

% Variables 
var int: f; % funcion objetivo 
var int: W;
var int: Z;

array[int] of var int: P = [(W - ciudades[i,1]) | i in 1..m];
array[int] of var int: J = [(Z - ciudades[i,2]) | i in 1..m];

constraint forall (i in 1..m) (P[i] + W >= ciudades[i,1]); 
constraint forall (i in 1..m) (-P[i] + W <= ciudades[i,1]); 
constraint forall (i in 1..m) (J[i] + Z >= ciudades[i,2]); 
constraint forall (i in 1..m) (-J[i] + Z <= ciudades[i,2]); 
constraint W >= 0;
constraint Z >= 0;
constraint forall (i in 1..m) (P[i] >= 0); 
constraint forall (i in 1..m) (J[i] >= 0); 

constraint forall (i in 1..m) (ciudades[i,1] != W /\ ciudades[i,2] != Z); 

constraint f = sum(i in 1..m)(P[i] + J[i]);
solve minimize f;

output ["Solucion: ", show(f),"\n","P(", show(W),",",show(Z), ")\n",];
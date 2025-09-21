(*exercice 1*)
let rec sum_chiffres(n:int) : int = if (n <= 0) then 0 
else ((n mod 10) + sum_chiffres(n/10));;

(sum_chiffres 125);;

let rec nb_chiffres(n:int) : int = 
  if(n<=0) then 0 
  else 1+(nb_chiffres (n/10));;


(nb_chiffres 102);;

(*exercice 2*)
let rec less_divider (i:int) (n:int) : int =
  if i == n then 0
  else if (n mod i)==0 then i
  else if n ==1 then 0
  else (less_divider (i+1) (n));;

(less_divider 2 19);; 
(less_divider 5 21);;
(less_divider 7 21);;
(less_divider 9 21);;
(less_divider 2 1);;

(* question 2 : Le type de la fonction less_divider est int->int*)

let prime (n:int) : bool =
  if n ==1 then false
  else if ((less_divider 2 n)==0) then true
  else false ;;

(prime 1);;
(prime 21);;
(prime 19);;

let rec next_prime(n :int) : int = 
  if (prime n) then n // n est premier
  else next_prime(n+1);;

(next_prime 0);;
(next_prime 15);;

(*cette fonction terminera toujours *)

(*exercice 3*)

(* question 1*)
(* un langage de programmtion fonctionnelle est un langage qui ne stocke pas de mémoire 
   contrairement aux langages impératifs comme python ou le C *)

# let x = 2 + 3 ;; (* definition de x *)
(* val x : int = 5 *)
# let y = x + 4 ;; (* definition de y *)
(* val y : int = 9 *)
# x * y ;;  
(* - : int = 45 *)
# x * z ;;  (* z n'est pas defini *)
(*Error: Unbound value z *)
# let x = 6;; (* modification de x *)
(* val x : int = 6 *)
# x ;; (* print x *)
(* - : int = 6 *)
# y ;; (* print y *)
(* - : int = 9 *)

# "bon" ^ "jour" ;; (* moyen de concatenation pour char *)

(* Définition d’une fonction : *)

let f (x : tx ) : tr = ef

(* f : nom de la fonction
x : paramètre de la fonction
tx : type du paramètre de la fonction
ef : corps de la fonction
tr : type du résultat de la fonction
    -> type de l’expression ef lorsque le type de x est tx
tx → tr est le type de la fonction f *)

(* Exemple page 14 *)
# let succ (x : int) : int = x+1;;
# (succ 8);;
(* - : int = 9 *)
(* definition de y *)
# let y = 4;;
val y : int = 4
# (succ (y+2));;
- : int = 7
# let z = (succ(y+5));;
val z : int = 10

(* fonction conditionnelle if a then b else char *)

(* exemple : valeur absolue d’un entier relatif *)
let abs (x : int) : int = if x > 0 then x else - x
# (abs (-2));;
- : int = 2

(* en OCaml, pas de boucles ni de while, on utilise la récursivité
   ne pas oublier le "rec" au début de la fonction 
   exemple : factorielle d’un entier naturel *)

let rec fact (n : int) : int = 
    if n = 0 then 1 else (fact (n - 1)) * n

# (fact 3);;
- : int = 6

(* (fact 3)
= if 3=0 then 1 else (fact (3-1))*3 = (fact 2) ∗ 3
= (if 2=0 then 1 else (fact (2-1))*2)*3 = ((fact 1) ∗ 2) ∗ 3
= ((if 1=0 then 1 else (fact (1-1))*1)*2)*3 = (((fact 0) ∗ 1) ∗ 2) ∗ 3
= ((if 0=0 then 1 else (fact (0-1))*1)*2)*3 = ((1 ∗ 1) ∗ 2) ∗ 3 = 6 *)

(* exemple : suite de Fibonacci F0 = 0 F1 = 1 Fn = Fn−1 + Fn−2 (pour n ≥ 2) *)
let rec fibo (n : int) : int =
if n = 0 then 0
            else if n = 1 then 1
                else (fibo (n-1)) + (fibo (n-2))
# (fibo 6);;
- : int = 8

(* l'ordre des parenthèses est primordial *)

let op (x : int) : int = -x;;

#(op (op 3));;
- : int = 3

#op 3 + 8 = 5

#op (8+3) = 11

(* VALEUR TEMPORAIRE*)

#let x = 3;;

#let x = x+2 in x+3;;

# let z = x + 3 in 2 * z;; 
- : int = 16
# z;;
Error: Unbound value z (* z est une valeur temporaire donc n'existe plus *)
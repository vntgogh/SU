(*exercice 1*)


let rec bin_to_int (i : int list) : int =
    match i with
    | 0 :: [] -> 0
    | [] -> raise "erreur"
    | h :: t -> h+2*(bin_to_int t)

let rec int_to_bin (i : int) : int list = 
    if i<2 then [i]
    else 
        (i mod 2) :: (int_to_bin i)

let rec comp_bin (l : int list) (n : int) : int list =
    if n < (List.length l) then raise "Invalid argument comp_bin";;
    if n = (List.length l) then l;;
    else
        match l with
        | [] -> 0 :: (comp_bin l (n-1))
        | h :: t -> (comp_bin l (n-1)) :: 0

(*exercice 2*)

let rec range_inter (a:int) (b:int) : int list=
    if a>b then []
    else a ::(range_inter (a+1) b)


let genere_list (n:int) ; int list =
    if n<2 then [] else (range_inter 2 n);;


let rec elimine (l : int list) (n : int) : int list =
    if n<2 then l
    else 
        match l with
        | [] -> []
        | h :: t -> (h mod n != 0) :: (elimine t n)


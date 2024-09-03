type 'a htree =
| Leaf of int * 'a
| Branch of int * 'a htree * 'a htree

let rec huff_tab (t:'a htree) : (('a * (int list)) list)=
  match t with
  |Leaf(_,y)-> [y, []]
  |Branch(_,g,d) -> (List.map (fun (x,y) -> (x,0:: y)) (huff_tab g)) @ (List.map (fun (x,y) -> (x,1:: y)) (huff_tab d))

let code (m : 'a list) (c : ('a * (int list)) list) : int list=
  

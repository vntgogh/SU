class Pile:
    """Classe dÃ©finissant une structure de pile."""
    def __init__(self):
        self.contenu = []

    def est_vide(self):
        """Renvoie le boolÃ©en True si la pile est vide, False sinon."""
        return self.contenu == []

    def empiler(self, v):
        """Place l'Ã©lÃ©ment v au sommet de la pile"""
        self.contenu.append(v)

    def depiler(self):
        """
        Retire et renvoie lâ€™Ã©lÃ©ment placÃ© au sommet de la pile,
        si la pile nâ€™est pas vide.
        """
        if not self.est_vide():
            return self.contenu.pop()


def eval_expression(tab):
    p = Pile()
    for element in tab:
        if element != '+' and element != '*': #pourquoi and et pas or??????
            p.empiler(element)
        else:
            if element == '+':
                resultat = p.depiler() + p.depiler()
            else:
                resultat = p.depiler()*p.depiler()
            p.empiler(resultat)
    return p.depiler()
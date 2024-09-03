class BinaryTreeCode:
    def __init__(self, racine):
        self.racine = None
        self.left = None
        self.right= None

    """def insert(abr, y ):
        while abr != None:
            x = abr.racine
            if y.key < x.key:
                abr= x.leftChild
            else:
                abr= x.righChild
        if y.key < x.key:
            y= x.leftChild
        else:
            y = x.rightChild"""

    def prefixe(abr,x):
        if abr != None:
            x= abr.racine
            print(x.key)
            prefixe(x.left)
            prefixe(x.right)

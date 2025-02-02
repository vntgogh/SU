"""
Ensemble de fonctions dédiées au tas utilisé pour stocker les positions de chaque étudiant pour un master i 
"""

def put(heap, value):
    """Ajoute une valeur au tas."""
    heap.append(value)
    moveup(heap, len(heap) - 1)

def pop(heap):
    """Retire et retourne la plus grande valeur du tas."""
    if not heap:
        raise IndexError("Le tas est vide.")
    # Échanger la racine avec le dernier élément
    echange(heap, 0, len(heap) - 1)
    # Retirer la racine
    max_value = heap.pop()
    # Réorganiser le tas
    movedown(heap, 0) #Le dernier élement est en haut du tas on doit le ramener en bas
    return max_value

def valracine(heap):
    """Retourne la plus grande valeur sans la retirer."""
    if not heap:
        raise IndexError("Le tas est vide.")
    return heap[0]

def moveup(heap, index):
    """Remonte un élément pour rétablir la propriété de tas."""
    parent_index = (index - 1) // 2
    while index > 0 and heap[index] > heap[parent_index]: # Tant que le fils est plus grand que le parent on monte le fils
        echange(heap, index, parent_index)
        index = parent_index
        parent_index = (index - 1) // 2

def movedown(heap, index):
    """Descend un élément pour rétablir la propriété de tas."""
    size = len(heap)
    while True: #Tant que le fils gauche ou le fils droit est plus grand que la valeur courante on fait descendre la valeur courant dans le tas
        largest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child < size and heap[left_child] > heap[largest]:
            largest = left_child
        if right_child < size and heap[right_child] > heap[largest]:
            largest = right_child

        if largest == index:
            break
        echange(heap, index, largest)
        index = largest

def echange(heap, i, j):
    """Échange deux éléments dans le tableau."""
    heap[i], heap[j] = heap[j], heap[i]
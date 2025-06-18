import numpy as np

def box(beads):
    beads = np.array(beads)
    return round(sum((beads**3)*(4/3)*np.pi), 4)

print(box([1, 5, 9, 11]))
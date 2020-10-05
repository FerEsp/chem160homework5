def molemass(sequence):
    Z = ["H", "C", "N", "O", "P", "S", "K", "F"]
    mass= [1.0079, 12.0107, 14.0067, 15.9994, 30.9738, 32.0660, 39.0983, 18.9984]
    element = dict(zip(Z, mass))
    M_mass=0
    for i in range(len(sequence)):
        M_mass+= element[sequence[i]]
    return M_mass
    


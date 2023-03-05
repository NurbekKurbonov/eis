def tilID(tillar,til):
    tilID=0
    for i in tillar:
        if i.nomi==til:
            tilID=i.id
    
    return tilID
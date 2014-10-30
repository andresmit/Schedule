t= 0
valjund = []
counter = 0
ps = []
def SJF(x):
    global valjund
    global ps
    ps = x[:]
    global t
    global sobivad
    while True:
        if ps or sobivad:
    
            print(ps)
            
            sobivad, uusaeg = sobiv(ps, t)
            print(sobivad)
            SJFSobivVäljundisse(sobivad[0], t)
        else:
            break
    keskm_ooteaeg = round(kogu_ooteaeg / len(x), 2)
    return valjund, keskm_ooteaeg

# tagastab lühima esimese protsessi ja liigutab vajadusel aega
def sobiv(x, t):
    global ps
    väljund = []
    for p in sorted(x):
        saabumine = p[0]
        kestus = p[1]
        while saabumine > t:
            t+=1
        else:
            väljund.append(p)
            ps.remove(p)
            break
    väljund.sort(key=lambda x: int(x[1]))
    return väljund, t

def kontrolliTühjaAjakulu(t, uusaeg):
    global valjund
    if uusaeg - t > 0:
        valjund.append([" ", uusaeg-t])
        return
    else:
        return

def SJFSobivVäljundisse(sobiv, t):
    global valjund
    global counter
    saabumine = sobiv[0]
    kestus = sobiv[1]

    if saabumine < t:
        kogu_ooteaeg += t - saabumine
                # vÃ¤ljundlisti kirjutatakse protsess koos nime ja kestusega
    valjund.append(["P" + str(counter), kestus])
    t += kestus
    counter += 1

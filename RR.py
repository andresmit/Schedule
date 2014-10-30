#ROUND ROBIN funktsioonide ja global muutujatega

ootavad = []
valjund = []
t = 0
ajakvant = 1
kogu_ooteaeg = 0
def RR(jarjend):
    global ps
    ps = jarjend[:]
    jarjendipikkus = len(jarjend)
    global t
    global ootavad
    global ajakvant
    global valjund
    global kogu_ooteaeg
    kogu_ooteaeg = 0
    valjund = []
    ps = idJärjestaRR(ps)
    ootavad = []
    t = 0
    ajakvant = 1
    while True:
        leiaSobivaidRR(ps, t)
        if ps and not ootavad:
            valjund.append([" ", järgmineTööaeg(ps)-t])
            t+=järgmineTööaeg(ps)
        elif ootavad and not ps:
            while ootavad:
                if len(ootavad) == 1:
                    valjund.append(["P"+str(ootavad[0][2]), ootavad[0][1]])
                    break
                salvestaVäljundisseRR(ootavad[0])
            break
        elif ootavad and ps:
            if len(ootavad) == 1:
                if (järgmineTööaeg(ps)-t)<ootavad[0][1]:
                    valjund.append(["P"+str(ootavad[0][2]), järgmineTööaeg(ps)-t])
                    ootavad[0][1] -= järgmineTööaeg(ps)-t
                else:
                    valjund.append(["P"+str(ootavad[0][2]), ootavad[0][1]])
                    ootavad = []

            else:
                salvestaVäljundisseRR(ootavad[0])
                continue

        else:
            break
    keskm_ooteaeg = round(kogu_ooteaeg / jarjendipikkus, 2)        
    return (valjund, keskm_ooteaeg)
    



def järgmineTööaeg(ps):
    return ps[0][0]
def idJärjestaRR(ps):
    ps.sort(key=lambda x: int(x[0]))
    for i in range(len(ps)):
        ps[i].append(i)
    return ps
    
def leiaSobivaidRR(ps, t):
    global ootavad
    for p in ps:
        t_in = p[0]
        if t>=t_in:
            ootavad.insert(0, p)
            ps.remove(p)
        return ps
    return None

def salvestaVäljundisseRR(sobiv):
    global valjund
    global t
    global ajakvant
    global kogu_ooteaeg
    global ootavad
    p_id = sobiv[2]
    p_tööaeg = sobiv[1]
    p_saabumine = sobiv[0]
    if p_tööaeg > ajakvant:
        valjund.append(["P" + str(p_id), ajakvant])
        ootavad.remove(sobiv)
        ootavad.append([t, p_tööaeg-ajakvant, p_id])
        t += ajakvant
        kogu_ooteaeg += t - p_saabumine
    else:
        valjund.append(["P" + str(p_id), p_tööaeg])
        kogu_ooteaeg += t - p_saabumine
        ootavad.remove(sobiv)
        t+=p_tööaeg


"""
ps = [
    [1, 2],
    [0, 5],
    [1, 4]
    
]
ps.sort(key=lambda x: int(x[0]))

for i in range(len(ps)):
    ps[i].append(i)

print(ps)
ps_waiting = []

cpu_ready_at = 0
curr_proc_runtime = None
ajakvant =1
# ajatsükkel

for t in range(1, 150):
    
    # cpu_ready_at on esimene ajapunkt, kus protsessor 
    # vaba on, st ühtki protsessi enam ei jookse, saab 
    # käima panna uue protsessi
    
        for p in ps:
            t_in = p[0]
            if t<=t_in:
                ps_waiting.append(p)
                ps.remove.(p)

    if (ps_waiting[0][0] <= t):
        min_sum = 0
        proc_to_run = None
        
        # kui eelnevalt mingi protsess käis, siis lisatakse 
        # see käesoleva ajapunktiga tagasi ootel protsesside
        # listi

        if (curr_proc_runtime is not None):
            ps_waiting.append([t, curr_proc_runtime-ajakvant])
        
        # tsükkel üle kõigi ootel protsesside, leia vähim 
        # t_entry + t_runtime, see protsess pannakse 
        # käima


        while ps:





    


        for p in ps_waiting:
            t_in = p[0]
            t_run = p[1]
            pid = p[2]
            if (t_in + t_run < min_sum):
                min_sum = t_in + t_run
                proc_to_run = [t_in, t_run, pid]
                curr_proc_runtime = t_run
        
        # eemalda leitud protsess ootel protsesside listist, 
        # salvesta aeg millal käivitatav protsess lõpetanud 
        # on, st CPU on jälle vaba
        if t_run =< 0:
            
            ps_waiting.remove(proc_to_run)
            cpu_ready_at = t + curr_proc_runtime
        else:
            break
        
        # debug

        print("--- t ==", t)
        print("running\t\t", proc_to_run, "( wait + runtime ==", min_sum, ")")
        print("procs waiting\t", ps_waiting)
        """

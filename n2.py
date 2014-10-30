from itertools import cycle
from itertools import repeat
j=[1,2,2,3,4,5,5]
q=j
läbitudaeg=0
for i in repeat(j):
    print("i=",i)
    q.remove(i)
    i = i-1
    q.append(i)
    print("q=",q)
    
#for i in len(list(j)):
    
#töölist, kus saabumine > läbitud aeg.
#if len töölist > 1:

def SJF(jarjend):
    sobivad = []
    väljund = []
    aeg = -1
    counter = 0
    while True:
        aeg +=1
        #sobivate protsesside lisamine "readyqueue"-sse
        for p in sorted jarjend:
            saabumine = jarjend[p][0]
            estus = jarjend[p][1]
             if saabumine =< aeg:
                 sobivad.add(protsess)
                 jarjend.remove(p)
            

             elif saabumine>aeg and sobivad tühi:
                 väljund add tühik
             el

        sobivad.sort(key
        väljund.append(sobivad[0])
        sobivad.remove(sobivad[0])
        counter +=1
        aeg += aeg + kestus
def RR(järjend):
    proc_käivad = []
    väljund = []
    aeg = -1
    ajakvant = 1
    counter = 0
    while True:
        aeg +=1
        #sobivate protsesside lisamine "readyqueue"-sse
        for p in sorted jarjend:
            saabumine = jarjend[p][0]
            estus = jarjend[p][1]
             if saabumine =< aeg:
                 proc_käivad.add(protsess)
                 jarjend.remove(p)
            

"""
def SJF(jarjend):
    järjend sorditakse teise elemendi järgi nii et esimene element jääb paika
    siis kontrollitakse kas läbitud ajaga on lisandunud mõni element, mis oleks
    lühem
    valjund = []
    counter = 1
    jarg = 0
    kogu_ooteaeg = 0
    s1 = sorted(jarjend, key = lambda x: (x[0], x[1]))
    for i in range(len(s1)):

        if saabumine > jarg:
            valjund.append([" ", saabumine-jarg])
* CPU scheduler picks the process from the circular/ready queue ,
set a timer to interrupt it after 1 time slice    / quantum
and dispatches it .

def RR(järjend):
    järjekorra1
    j = järjend
    protsessiq= []
    temp = []
    for i in range(len(j)):
        kestus = j[i][0]
        if kestus > 0:
            if kestus <= ajakvant:
                väljund.append(item)
              >  Process will leave the CPU after the completion
              >  CPU will proceed with the next process in
              the ready queue / circular queue .

        else:
            if kestus => ajakvant:
                kestus - ajakvant

    else If process has burst time longer than 1 time slice/quantum
            
             >  Timer will be stopped . It cause interruption to the OS .
             >   Executed process is then placed at the tail of the
             circular / ready  querue by applying  the context                   switch
             >  CPU scheduler then proceeds by selecting the
             next process in the ready queue .      


sisend = [[0,3],[0,2],[2,2]]
BurstTimes = sisend[::2]
ArrivalTimes = sisend[1::2]
print(sisend[:2])
s = sorted(sisend[:2], key = lambda x: (x[0], x[1]))

print(s)"""
##print(ArrivalTimes)

##väljund = sorted(sisend, key=lambda x: int(x[1]))
##print(väljund)


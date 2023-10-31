import os
from random import randrange
import pickle
non=input("antre yon psedo pou jwet la fol pa gen espas  \n").lower()
print(type(non))
base={}
if not os.path.exists('my_object.txt'):
    with open('my_object.txt', 'wb') as f: 
        pickle.dump(base, f)
else:
    with open('my_object.txt', 'rb') as f: 
        base=pickle.load( f)

b='n'
while(b!='k'):
    nonbpc=randrange(0,100)
    chans=3
    while chans!=0: 
        n=int(input("antre nonb wap chwazi nan intèval 0 a 100\n"))
        while( n>100 or n<0):
            n=input("erè antre nonb lan entèval 0 a 100\n")
        
        if(n==nonbpc):
            print("BRAVO !! ")
            
            if non in base :
                verif=base[non]
                print("ansyen sko ase :",verif)
                base[non]=chans*30+verif
                print("nouvo sko a ase :",base[non],"peze k siw ap kanpe si non nenpot")
                with open('my_object.txt', 'ab') as f: 
                    pickle.dump(base, f)
               

            else:
                base[non]=chans*30
                print("nouvo sko a ase :",base[non],"peze k siw ap kanpe si non nenpot")
                with open('my_object.txt', 'ab') as f: 
                    pickle.dump(base, f)
            break
        if(n!=nonbpc):
            chans-=1
            if(n>nonbpc):
                print("ou pèdi ou rete",chans,"chans  epi nonb ou chwazi a pigro ke sak soti a")   
            else:
                print("ou pèdi ou rete",chans,"chans epi nonb ou chwazi a pi piti ke sak soti a")
    with open('my_object.pickle', 'rb')as f:
     base = pickle.load(f)
    print(base)
    if chans==0:            
        print("se ",nonbpc," ki te soti ou pa jwenn li peze k siw ap kanpe si non nenpot")
    b=input().lower()
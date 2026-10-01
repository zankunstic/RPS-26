igre = ['K','Š','K','P','Š','P','K','K']

def izračunajZmage(igre:list) -> list:
    zmage=[]
    for i in range(0,len(igre),2):
        print(i,i+1)
        prvi=igre[i]
        drugi=igre[i+1]
        odg = kdozmaga(prvi,drugi)
        zmage.append(odg)
    return(zmage)
def kdozmaga(prvi:str,drugi:str) -> int:
    if prvi==drugi:
        return 0
    if prvi=='K'and drugi=='Š':
        return 1
    if prvi=='K'and drugi=='P':
        return 2
    if prvi=='P'and drugi=='Š':
        return 2
    if prvi=='P'and drugi=='K':
        return 1
    if prvi=='Š'and drugi=='K':
        return 2
    if prvi=='Š'and drugi=='P':
        return 1

def izdelaj_stat(zmage:list)->list:
    st_prvi=0
    st_drugi=0
    izenačeno=0
    for elemnt in zmage:
        if elemnt ==1:
            st_prvi+=1
        elif elemnt ==2:
            st_drugi+=1
        else:
            izenačeno+=1
    return(f"prvi je zmagal: {st_prvi}-krat, drugi je zmagal {st_drugi}-krat  in izenačeno je bilo {izenačeno}-krat")
    


import requests





izračunajZmage(igre)  
print(izračunajZmage(igre) 
print(izdelaj_stat(izračunajZmage(igre) ))
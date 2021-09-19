import os,time
from pokemondata import *
from random import randint

probdict = {100: [1, 1], 95: [19, 20], 85: [17, 20], 90: [9, 10], 80: [4, 5], 70: [7, 10], 30: [3, 10], 33: [33, 100], 10: [1, 10], 12.5: [1, 8]}
pw,cw=0,0
def strlist(a):
    if a=='':return ['','']
    l=['','']
    for i in range(len(a)):
        if a[i].isalpha():l[0]+=a[i]
        elif a[i].isnumeric():l[1]+=a[i]
    l[1]=int(l[1])
    return l
def PokeAdvan(p,x):
    c={'Fire':0,'Grass':1,'Water':2}
    p,x=c[p],c[x]
    if (p-x== -1) or (p-x== 2): return 1
    elif (p-x== 1) or (p-x== -2): return -1
    else:return 0
def lifeBar(a,b):return '|'+'_'*int(round((a/b * 20),0))+'|'
pb,cb=[None,None],[None,None]
pf,cf=0,0
print("Pokemon Battle By - Prakhar")
pokemonList=["Charizard","Infernape","Magmortar","Venusaur","Leafeon","Decidueye","Blastoise","Gyarados","Greninja"]
pokedataList=[Charizard,Infernape,Magmortar,Venusaur,Leafeon,Decidueye,Blastoise,Gyarados,Greninja]

pl=[None,None,None,"NOW"]
m=4
while(pl[0]==pl[1] or pl[0]==pl[2])or pl[1]==pl[2]:
    for i in range(3):pl[i] = pokemonList[randint(0,8)]
curP,curC = None,None
cp=[None,None,None,"NOW"]
while(cp[0]==cp[1] or cp[0]==cp[2])or cp[1]==cp[2]:
    for i in range(3):cp[i] = pokemonList[randint(0,8)]
for z in range(1,4):
    m=4
    if z==1:
        print("Your Partners -\n0. "+pl[0]+"\n1. "+pl[1]+"\n2. "+pl[2])
        while m>2:
            m=int(input("\nChoose your Pokemon for Battle "+str(z)+" - "))
        pl[-1] = pl[m]
        print(pl[-1]+", I choose You.")
        cp[-1]=cp[randint(0,2)]
        time.sleep(1)
    elif z==2:
        print("Your Partners -\n0. "+pl[0]+"\n1. "+pl[1])
        while m>1:
            m=int(input("\nChoose your Pokemon for Battle "+str(z)+" - "))
        pl[-1] = pl[m]
        print(pl[-1]+", I choose You.")
        cp[-1]=cp[randint(0,1)]
        time.sleep(1)
    else:
        pl[-1] = pl[0]
        cp[-1] = cp[0]
        print(pl[-1]+", I choose You.")
        time.sleep(1)
    print("Your Rival choose, "+cp[-1]+'\n')
    time.sleep(1)
    for i in range(len(pokemonList)):
        if pl[-1] == pokemonList[i]:curP = dict(pokedataList[i])
    for i in range(len(pokemonList)):
        if cp[-1] == pokemonList[i]:curC = dict(pokedataList[i])

    tA = PokeAdvan(curP["Type"],curC["Type"])
    if tA==0:
        print("Both Pokemon are of same Type.")
    elif tA==1:
        for i in range(4):
            if int(curP["Moves"][i][1])!=0:curP["Moves"][i][1]+=5
        print("Your Pokemon has a Type Advantage.")
    else:
        for i in range(4):
            if int(curC["Moves"][i][1]!=0):curC["Moves"][i][1]+=5
        print("Your Pokemon has a Type Disadvantage.")
    time.sleep(1)
    while True:
        os.system('cls')
        a="\n\nCPU - "+cp[-1]+'('+curC["Type"]+')'+" - "+lifeBar(curC["HP_Cur"],curC["HP"])+"("+str(curC["HP_Cur"])+"/"+str(curC["HP"])+")\n\nPLY - "+pl[-1]+'('+curP["Type"]+')'+" - "+lifeBar(curP["HP_Cur"],curP["HP"])+"("+str(curP["HP_Cur"])+"/"+str(curP["HP"])+""")

Moves -
0. """+curP["Moves"][0][0]+" - P  - "+str(curP["Moves"][0][1])+", A  - "+str(curP["Moves"][0][2])+"%, PP - "+str(curP["Moves"][0][3])+" times "+curP["Moves"][0][4]+"""
1. """+curP["Moves"][1][0]+" - P  - "+str(curP["Moves"][1][1])+", A  - "+str(curP["Moves"][1][2])+"%, PP - "+str(curP["Moves"][1][3])+" times "+curP["Moves"][1][4]+"""
2. """+curP["Moves"][2][0]+" - P  - "+str(curP["Moves"][2][1])+", A  - "+str(curP["Moves"][2][2])+"%, PP - "+str(curP["Moves"][2][3])+" times "+curP["Moves"][2][4]+"""
3. """+curP["Moves"][3][0]+" - P  - "+str(curP["Moves"][3][1])+", A  - "+str(curP["Moves"][3][2])+"%, PP - "+str(curP["Moves"][3][3])+" times "+curP["Moves"][3][4]
        print(a,end='\n')
        while True:
            pMove=4
            while pMove>3:pMove=int(input('\nYour Attack - '))
            if curP["Moves"][pMove][3]==0:
                print('This Attack cannot be used more.',end='\n')
                continue
            else:break
        if curP['speed']>curC['speed']:
            temp = probdict[curP["Moves"][pMove][2]]
            if randint(1,temp[1])<=temp[0]:
                temp=strlist(curP["Moves"][pMove][4])
                if 'ritical' in temp[0]:
                    temp=probdict[temp[1]/10]
                    if randint(1,temp[1])<=temp[0]:
                        print('Critical Hit By '+pl[-1])
                        curC["HP_Cur"] -= 30
                        time.sleep(1)
                elif 'ecoil' in temp[0]:
                    print(pl[-1]+' suffered, Recoil Damage')
                    curP["HP_Cur"] -= 30
                    time.sleep(1)
                elif 'urned' in temp[0]:
                    temp=probdict[temp[1]]
                    if randint(1,temp[1])<=temp[0]:
                        cb=[1,randint(2,3)]
                        if cb[0]<=cb[1] and cb[0]!=0:
                            cb[0]+=1
                            if cb[0]==cb[1]:cb=[None,None]
                            print(pl[-1]+"'s Attack, caused a burn to "+cp[-1])
                            curC["HP_Cur"] -= 20
                        time.sleep(1)
                elif 'linch' in temp[0]:
                    temp=probdict[temp[1]]
                    if randint(1,temp[1])<=temp[0]:
                        cf=1
                        time.sleep(1)
                if curP["Moves"][pMove][1]!=0 and curP["Moves"][pMove][1]!=0.4:
                    if curP["Moves"][pMove][1]>0 and curP["Moves"][pMove][1]<1:
                        curC["HP_Cur"] -= int(curP["Moves"][pMove][1]*curC["HP"])
                        curP["Moves"][pMove][3]-=1
                    else:
                        curC["HP_Cur"]-=curP["Moves"][pMove][1]
                        curP["Moves"][pMove][3]-=1
                elif curP["Moves"][pMove][1]==0.4:
                    curC["HP_Cur"] -= int((curC["HP"]*40)/100)
                    curP["Moves"][pMove][3]-=1
                elif curP["Moves"][pMove][1]==0 and curP["HP_Cur"]>0:
                    curP["HP_Cur"] += int((curP["HP"]*33)/100)
                    curP["Moves"][pMove][3]-=1
                print('Your Attack - '+curP["Moves"][pMove][0])
            else:
                print("YOUR POKEMON'S ATTACK MISSED!!!")
                curP["Moves"][pMove][3]-=1
            time.sleep(1)
            if cf==0:
                cpMove = randint(0,3)
                temp = probdict[curC["Moves"][cpMove][2]]
                if randint(1,temp[1])<=temp[0]:
                    temp=strlist(curC["Moves"][cpMove][4])
                    if 'ritical' in temp[0]:
                        temp=probdict[temp[1]/10]
                        if randint(1,temp[1])<=temp[0]:
                            print('Critical Hit By '+cp[-1])
                            curP["HP_Cur"] -= 30
                            time.sleep(1)
                    elif 'ecoil' in temp[0]:
                        print(cp[-1]+' suffered, Recoil Damage')
                        curC["HP_Cur"] -= 30
                        time.sleep(1)
                    elif 'urned' in temp[0]:
                        temp=probdict[temp[1]]
                        if randint(1,temp[1])<=temp[0]:
                            pb=[1,randint(2,3)]
                            if pb[0]<=pb[1] and pb[0]!=0:
                                pb[0]+=1
                                if pb[0]==pb[1]:pb=[None,None]
                                print(pb[-1]+"'s Attack, caused a burn to "+pb[-1])
                                curP["HP_Cur"] -= 20
                            time.sleep(1)
                    if curC["HP_Cur"]>=0:print(cp[-1]+' used '+curC["Moves"][cpMove][0])
                    if (curC["Moves"][cpMove][1]!=0 and curC["HP_Cur"]>=0)and curC["Moves"][cpMove][1]!=0.4:
                        if curC["Moves"][cpMove][1]>0 and curC["Moves"][cpMove][1]<1:
                            curP["HP_Cur"] -= int(curC["Moves"][cpMove][1]*curP["HP"])
                            curC["Moves"][cpMove][3]-=1
                        else:
                            curP["HP_Cur"]-=curC["Moves"][cpMove][1]
                            curC["Moves"][cpMove][3]-=1
                    elif curC["Moves"][cpMove][1]==0.4:
                        curP["HP_Cur"] -= int((curP["HP"]*40)/100)
                        curC["Moves"][cpMove][3]-=1
                    elif curC["Moves"][cpMove][1]==0 and curC["HP_Cur"]>0:
                        curC["HP_Cur"] += int((curC["HP"]*33)/100)
                        curC["Moves"][cpMove][3]-=1
                else:
                    print("RIVAL POKEMON'S ATTACK MISSED!!!")
                    curC["Moves"][cpMove][3]-=1
                time.sleep(1)
            else:
                cf=0
                print(pl[-1]+"'s Attack, flinched "+cp[-1])
        else:
            cpMove = randint(0,3)
            temp = probdict[curC["Moves"][cpMove][2]]
            if randint(1,temp[1])<=temp[0]:
                temp=strlist(curC["Moves"][pMove][4])
                if 'ritical' in temp[0]:
                    temp=probdict[temp[1]/10]
                    if randint(1,temp[1])<=temp[0]:
                        print('Critical Hit By '+cp[-1])
                        curP["HP_Cur"] -= 30
                        time.sleep(1)
                elif 'ecoil' in temp[0]:
                    print(cp[-1]+' suffered, Recoil Damage')
                    curC["HP_Cur"] -= 30
                    time.sleep(1)
                elif 'linch' in temp[0]:
                    temp=probdict[temp[1]]
                    if randint(1,temp[1])<=temp[0]:
                        pf=1
                        time.sleep(1)
                elif 'urned' in temp[0]:
                    temp=probdict[temp[1]]
                    if randint(1,temp[1])<=temp[0]:
                        pb=[1,randint(2,3)]
                        if pb[0]<=pb[1] and pb[0]!=0:
                            pb[0]+=1
                            if pb[0]==pb[1]:pb=[None,None]
                            print(pb[-1]+"'s Attack, caused a burn to "+pb[-1])
                            curP["HP_Cur"] -= 20
                        time.sleep(1)
                if curC["HP_Cur"]>=0:print(cp[-1]+' used '+curC["Moves"][cpMove][0])
                if (curC["Moves"][cpMove][1]!=0 and curC["HP_Cur"]>=0)and curC["Moves"][cpMove][1]!=0.4:
                    if curC["Moves"][cpMove][1]>0 and curC["Moves"][cpMove][1]<1:
                        curP["HP_Cur"] -= int(curC["Moves"][cpMove][1]*curP["HP"])
                        curC["Moves"][cpMove][3]-=1
                    else:
                        curP["HP_Cur"]-=curC["Moves"][cpMove][1]
                        curC["Moves"][cpMove][3]-=1
                elif curC["Moves"][cpMove][1]==0.4:
                    curP["HP_Cur"] -= int((curP["HP"]*40)/100)
                    curC["Moves"][cpMove][3]-=1
                elif curC["Moves"][cpMove][1]==0 and curC["HP_Cur"]>0:
                    curC["HP_Cur"] += int((curC["HP"]*33)/100)
                    curC["Moves"][cpMove][3]-=1
            else:
                print("RIVAL POKEMON'S ATTACK MISSED!!!")
                curC["Moves"][cpMove][3]-=1
            time.sleep(1)
            if pf==0:
                temp = probdict[curP["Moves"][pMove][2]]
                if randint(1,temp[1])<=temp[0]:
                    temp=strlist(curP["Moves"][pMove][4])
                    if 'ritical' in temp[0]:
                        temp=probdict[temp[1]/10]
                        if randint(1,temp[1])<=temp[0]:
                            print('Critical Hit By '+pl[-1])
                            curC["HP_Cur"] -= 30
                            time.sleep(1)
                    elif 'ecoil' in temp[0]:
                        print(pl[-1]+' suffered, Recoil Damage')
                        curP["HP_Cur"] -= 30
                        time.sleep(1)
                    elif 'urned' in temp[0]:
                        temp=probdict[temp[1]]
                        if randint(1,temp[1])<=temp[0]:
                            cb=[1,randint(2,3)]
                            if cb[0]<=cb[1] and cb[0]!=0:
                                cb[0]+=1
                                if cb[0]==cb[1]:cb=[None,None]
                                print(pl[-1]+"'s Attack, caused a burn to "+cp[-1])
                                curC["HP_Cur"] -= 20
                            time.sleep(1)
                    if (curP["Moves"][pMove][1]!=0 and curP["HP_Cur"]>=0)and curP["Moves"][pMove][1]!=0.4:
                        if curP["Moves"][pMove][1]>0 and curP["Moves"][pMove][1]<1:
                            curC["HP_Cur"] -= int(curP["Moves"][pMove][1]*curC["HP"])
                            curP["Moves"][pMove][3]-=1
                        else:
                            curC["HP_Cur"]-=curP["Moves"][pMove][1]
                            curP["Moves"][pMove][3]-=1
                    elif curP["Moves"][pMove][1]==0.4:
                        curC["HP_Cur"] -= int((curC["HP"]*40)/100)
                        curP["Moves"][pMove][3]-=1
                    elif curP["Moves"][pMove][1]==0 and curP["HP_Cur"]>0:
                        curP["HP_Cur"] += int((curP["HP"]*33)/100)
                        curP["Moves"][pMove][3]-=1
                    if curP["HP_Cur"]>=0:print('Your Attack - '+curP["Moves"][pMove][0])
                else:
                    print("YOUR POKEMON'S ATTACK MISSED!!!")
                    curP["Moves"][pMove][3]-=1
                time.sleep(1)
            else:
                pf=0
                print(cp[-1]+"'s Attack, flinched "+pl[-1])

        if curP["HP_Cur"]<=0:
            pl.remove(pl[-1])
            cp.remove(cp[-1])
            pl[-1]="NOW"
            break
        elif curC["HP_Cur"]<=0:
            cp.remove(cp[-1])
            pl.remove(pl[-1])
            cp[-1]="NOW"
            break

    if pl[-1]=="NOW":
        cp[-1]="NOW"
        print("\nYour Rival WON Battle "+str(z)+".")
        cw+=1
    elif cp[-1]=="NOW":
        pl[-1]="NOW"
        print("\nYou WON Battle "+str(z)+".")
        pw+=1
    time.sleep(1)
    os.system('cls')


if pw>cw:print("WINNER - PLAYER\nCongratulations, You are now 1 step closer to become\nTHE BEST POKEMON TRAINER")
else:print("WINNER - COMPUTER\nHey PLAYER, that was a close Battle, Better Luck Next Time")
input()

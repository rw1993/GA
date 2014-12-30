from func import f
import UserString
import random
class a_anser:
    def __init__(self,x1,x2):
        self.x1=x1
        self.x2=x2
        self.str1=UserString.MutableString('{0:07b}'.format(x1))
        self.str2=UserString.MutableString('{0:07b}'.format(x2))
        self.value=f(x1,x2)
        self.count=-1


range1=[0,127]
range2=[0,127]
bestanser=None
limit=0
#init init_ansers
#set the number of ansers in a group
number_of_group=10
group=[]
#random choose number_of_group ansers in range
for i in range(0,10):
    x1=random.randint(range1[0],range1[1])
    x2=random.randint(range2[0],range2[1])
    anser=a_anser(x1,x2)
    group.append(anser)
while True:
    sumvalue=0.0
    for a in group:
        sumvalue+=a.value


    #sort group by value
    group.sort(cmp=None,key=lambda x:x.value,reverse=True)
     
    if bestanser is None:
        bestanser=group[0]
    else:
        if bestanser.value<group[0].value:
            bestanser=group[0]
        else:
            limit+=1
            if limit>40:
                break
    print bestanser.value
    print bestanser.x1,bestanser.x2


    parents=[]
    for a in group:
        count=int((a.value/sumvalue)*10) 
        a.count=count
        for i in range(0,count):
            parents.append(a)

    while len(parents)<10:
        for a in group:
            if a.count<=0:
                a.count=1
                parents.append(a)
                break
    newgroup=[]
    random.shuffle(parents)#random the list
    while len(parents)>0:
        #choose mother and father
        mother=parents[0]
        father=parents[1]
        parents.remove(father)
        parents.remove(mother)

        #random location
        locate=random.randint(0,13)
        tmp1=UserString.MutableString(str(mother.str1))
        tmp2=UserString.MutableString(str(mother.str2))
        tmp3=UserString.MutableString(str(father.str1))
        tmp4=UserString.MutableString(str(father.str2))
        if locate<=6:
            tmp1[locate]=father.str1[locate]
            tmp3[locate]=mother.str1[locate]
            new_anser1=a_anser(int(str(tmp1),2),mother.x2)
            new_anser2=a_anser(int(str(tmp3),2),father.x2)
        else:
            locate=locate-7
            tmp2[locate]=father.str2[locate]
            tmp4[locate]=mother.str2[locate]
            new_anser1=a_anser(mother.x1,int(str(tmp2),2))
            new_anser2=a_anser(mother.x2,int(str(tmp4),2))
        newgroup.append(new_anser1)
        newgroup.append(new_anser2)

    group=newgroup


print bestanser.value
print bestanser.x1,bestanser.x2
        


    























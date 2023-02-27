
class nisbiy_meyor():
    # nisbiy me'yorni aniqlash

    def nisbiy_meyor(his,unversal_birlik):
        
        ist=[]
        mahsulot=[]
        for i in his.h_item.all():
            ist.append(i.ist)
            for j in i.uzat.all():
                mahsulot.append(j.qiymat*j.resurs.hajm.qiymati)
        
        davr=[]
        for i in his.h_item.all():
            davr.append(i.vaqt)
        davr=sorted(set(davr))

        malumot={}
        for i in davr:
            lst=[]
            for j in ist:
                for k in j.all():
                    if i==k.vaqt:
                        lst.append(k)
            malumot[i]=lst

        yigindi=[]
        for k,v in malumot.items():
            summa=0
            for i in v:
                if unversal_birlik=='tshy':
                    ub=i.resurs.resurs.tshy
                elif unversal_birlik=='tne':
                    ub=i.resurs.resurs.tne
                elif unversal_birlik=='gj':
                    ub=i.resurs.resurs.gj
                elif unversal_birlik=='gkal':
                    ub=i.resurs.resurs.gkal                

                summa+=float(i.qiymat)*float(i.resurs.hajm.qiymati)*float(ub)
            yigindi.append(summa)
        
        #nisbiy meyor    
        nisbiy_meyor={}
        for i in range(len(davr)):
            nb=yigindi[i]/mahsulot[i]
            nisbiy_meyor[davr[i].strftime("%m/%Y")]='{0:.2f}'.format(float(nb))        
        return nisbiy_meyor
    
    def plan_nisbiy_meyor(his,unversal_birlik):
        
        ist=[]
        mahsulot=[]
        for i in his.h_itemp.all():
            ist.append(i.ist)
            for j in i.uzat.all():
                mahsulot.append(j.qiymat*j.resurs.hajm.qiymati)
        
        davr=[]
        for i in his.h_item.all():
            davr.append(i.vaqt)
        davr=sorted(set(davr))

        malumot={}
        for i in davr:
            lst=[]
            for j in ist:
                for k in j.all():
                    if i==k.vaqt:
                        lst.append(k)
            malumot[i]=lst

        yigindi=[]
        for k,v in malumot.items():
            summa=0
            for i in v:
                if unversal_birlik=='tshy':
                    ub=i.resurs.resurs.tshy
                elif unversal_birlik=='tne':
                    ub=i.resurs.resurs.tne
                elif unversal_birlik=='gj':
                    ub=i.resurs.resurs.gj
                elif unversal_birlik=='gkal':
                    ub=i.resurs.resurs.gkal                

                summa+=float(i.qiymat)*float(i.resurs.hajm.qiymati)*float(ub)
            yigindi.append(summa)
        
        #nisbiy meyor    
        nisbiy_meyor={}
        for i in range(len(davr)):
            nb=yigindi[i]/mahsulot[i]
            nisbiy_meyor[davr[i].strftime("%m/%Y")]='{0:.2f}'.format(float(nb))        
        return nisbiy_meyor
    
    def sb_plan_fakt(his_plan, his_fakt, unversal_birlik):
        plan=nisbiy_meyor.nisbiy_meyor(his_plan, unversal_birlik)
        fakt=nisbiy_meyor.nisbiy_meyor(his_fakt, unversal_birlik)

        pf={}
        c=0
        for k in plan.keys():
            lst=[]
            lst.append(plan[c], fakt[c])
            pf[k]=lst
        return pf
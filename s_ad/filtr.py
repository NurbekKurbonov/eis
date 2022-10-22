
        if iftum_fqr!="0":
        for i in fqr.filter(iftum=IFTUM(iftum_fqr)):     
            if filtr_faqir.objects.filter(owner=request.user, fqr=allfaqir(i.id)).first():        
                pass                
            else:
                if dbibt_fqr=="0" and thst_fqr=="0":
                    filtr_faqir.objects.create(owner=request.user, 
                                            fqr=allfaqir.objects.get(pk=i.id))
                else:
                    if dbibt_fqr=="0":
                        if i.thst_id==int(thst_fqr):
                            filtr_faqir.objects.create(owner=request.user, 
                                                fqr=allfaqir.objects.get(pk=i.id))
                        else: 
                            pass
                    if thst_fqr=="0":
                        if i.dbibt_id==int(dbibt_fqr):
                            filtr_faqir.objects.create(owner=request.user, 
                                                fqr=allfaqir.objects.get(pk=i.id))
                        else: 
                            pass
                    else:
                        if i.thst_id==int(thst_fqr) and i.dbibt_id==int(dbibt_fqr):
                                filtr_faqir.objects.create(owner=request.user, 
                                                fqr=allfaqir.objects.get(pk=i.id))
                           
                        
    
    if dbibt_fqr!="0":
        for i in fqr.filter(dbibt=DBIBT(dbibt_fqr)):     
            if filtr_faqir.objects.filter(owner=request.user, fqr=allfaqir(i.id)).first():        
                pass                
            else:
                if iftum_fqr=="0" and thst_fqr=="0":
                    filtr_faqir.objects.create(owner=request.user, 
                                            fqr=allfaqir.objects.get(pk=i.id))
                else:
                    if iftum_fqr=="0":
                        if i.thst.id==int(thst_fqr):
                            filtr_faqir.objects.create(owner=request.user, 
                                                fqr=allfaqir.objects.get(pk=i.id))
                        else: 
                            pass
                    if thst_fqr=="0":
                        if i.iftum.id==int(iftum_fqr):
                            filtr_faqir.objects.create(owner=request.user, 
                                                fqr=allfaqir.objects.get(pk=i.id))
                        else: 
                            pass
                    else:
                        if i.thst_id==int(thst_fqr) and i.iftum_id==int(iftum_fqr):
                                filtr_faqir.objects.create(owner=request.user, 
                                                fqr=allfaqir.objects.get(pk=i.id))                
    if thst_fqr!="0":
        for i in fqr.filter(thst=THST(thst_fqr)):     
            if filtr_faqir.objects.filter(owner=request.user, fqr=allfaqir(i.id)).first():        
                pass                
            else:
                if iftum_fqr=="0" and dbibt_fqr=="0":
                    filtr_faqir.objects.create(owner=request.user, 
                                            fqr=allfaqir.objects.get(pk=i.id))
                else:
                    if iftum_fqr=="0":
                        if i.dbibt.id==int(dbibt_fqr):
                            filtr_faqir.objects.create(owner=request.user, 
                                                fqr=allfaqir.objects.get(pk=i.id))
                        else: 
                            pass
                    if dbibt_fqr=="0":
                        if i.iftum.id==int(iftum_fqr):
                            filtr_faqir.objects.create(owner=request.user, 
                                                fqr=allfaqir.objects.get(pk=i.id))
                        else: 
                            pass  
                    else:
                        if i.iftum_id==int(iftum_fqr) and i.dbibt_id==int(dbibt_fqr):
                                filtr_faqir.objects.create(owner=request.user, 
                                                fqr=allfaqir.objects.get(pk=i.id))
    
from django import template

from ..models import Tarjimon, jumla, Til

register=template.Library()

def tilID(til):
    tillar=Til.objects.all()
    tilID=0
    for i in tillar:
        if i.nomi==til:
            tilID=i.id    
    return tilID

@register.simple_tag
def tarjimon(soz, til):
    if til=="O'zbek":
        tarjimasi=soz
    else:
        x=0
        for i in Tarjimon.objects.all():
            if i.nomi.nomi==soz:
                for j in i.tarjimasi.all():
                    if j.til.id==tilID(til):
                        tarjimasi=j.nomi
                        x+=1
        if x==0:
            tarjimasi=str(soz)+" "+str(til)+" ga tarjima qilinmagan"


    return tarjimasi

@register.simple_tag
def tillar():
    til=Til.objects.all()  
    return til


@register.simple_tag
def asosiytil(til):
    for i in Til.objects.all():
        if i.nomi==til:
            asosiytil=i
    
    
    return asosiytil


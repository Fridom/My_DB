from django.db import models


class Type(models.Model):
    type = models.CharField(max_length=50)

class NameEquip(models.Model):
    name = models.CharField(max_length=30)
    type = models.ForeignKey(Type)

class Auditors(models.Model):
    build = models.CharField(max_length=10)
    number = models.IntegerField(default=411)


class EqList(models.Model):
    name = models.ForeignKey(NameEquip)
    date_buy = models.DateField(auto_now=True)
    characters = models.CharField(max_length=5000)
    condition_inf = models.CharField(max_length=5000)

class Locati(models.Model):
    id_equip = models.ForeignKey(EqList)
    id_auditor = models.ForeignKey(Auditors)
    date_loc = models.DateField(auto_now=True)


#from example.models import Type, NameEquip, Auditors, EqList, Loc
#from django.utils import timezone
#Type.objects.create(type = 'My_type')
#NameEquip.objects.create(name='My_equip_name',type = Type.objects.all()[0])
#Auditors.objects.create(number=411, build='ULK')
#EqList.objects.create(name = NameEquip.objects.filter(id=1)[0], date_buy = timezone.now(), characters = 'My_Characters', condition_inf = 'My_condition')
#Locati.objects.create(id_equip=EqList.objects.all()[0], id_auditor=Auditors.objects.all()[0], date_loc= timezone.now())


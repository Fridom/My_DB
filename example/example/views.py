# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView, View
from django.shortcuts import redirect
from models import Type, NameEquip, Auditors, EqList, Locati
from django.contrib import admin

class TypeView(View):
    template_name = "index.html"

    def post(self, *args, **kwargs):
        type_value = self.request.POST['type']
        Type.objects.create(type=type_value)
        return redirect('/')

class NameView(View):
    template_name = "index.html"

    def post(self, *args, **kwargs):
        name_value = self.request.POST['name']
        type_id_value = self.request.POST['type_id']
        NameEquip.objects.create(name=name_value,type=Type.objects.filter(id=int(type_id_value))[0])
        return redirect('/')

class AuditoriesView(View):
    template_name = "index.html"

    def post(self, *args, **kwargs):
        number_value = self.request.POST['number']
        build_value = self.request.POST['build']
        Auditors.objects.create(number=int(number_value), build=build_value)
        return redirect('/')

class EquipView(View):
    template_name = "index.html"

    def post(self, *args, **kwargs):
        name_value = self.request.POST['name_id']
        date_buy_value = self.request.POST['date_buy']
        characters_value = self.request.POST['characters']
        condition_inf_value = self.request.POST['condition_inf']
        EqList.objects.create(name=NameEquip.objects.filter(id=int(name_value))[0], date_buy=date_buy_value, characters=characters_value, condition_inf=condition_inf_value)
        return redirect('/')

class LocationView(View):
    template_name = "index.html"

    def post(self, *args, **kwargs):
        id_equip_value = self.request.POST['id_equip']
        id_auditor_value = self.request.POST['id_auditor']
        date_loc_value = self.request.POST['date_loc']
        Locati.objects.create(id_equip=EqList.objects.filter(id=int(id_equip_value))[0], id_auditor=Auditors.objects.filter(id=int(id_auditor_value))[0], date_loc=date_loc_value)
        return redirect('/')


type_list = Type.objects.all()
name_equip_list = NameEquip.objects.all()
auditors_list = Auditors.objects.all()
equip_list = EqList.objects.all()
location_list = Locati.objects.all()



class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(
            {
                'type': type_list,
                'name_equip': name_equip_list,
                'auditors': auditors_list,
                'equip': equip_list,
                'location': location_list
            }
        )
        return context
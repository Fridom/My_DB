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


class LocationView(View):
    template_name = "index.html"

    def post(self, *args, **kwargs):




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
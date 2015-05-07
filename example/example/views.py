# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
from models import Type, NameEquip, Auditors, EqList, Locati
from django.contrib import admin

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
from django.conf.urls import patterns, url

from django.contrib import admin

from views import IndexView, TypeView, NameView, AuditoriesView, EquipView, LocationView, DeleteType, DeleteName

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'example.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', IndexView.as_view()),
   url(r'^type', TypeView.as_view()),
   url(r'^name', NameView.as_view()),
   url(r'^auditories', AuditoriesView.as_view()),
   url(r'^equip', EquipView.as_view()),
   url(r'^location', LocationView.as_view()),
   url(r'^delete_type', DeleteType.as_view()),
   url(r'^delete_name', DeleteName.as_view()),

    )
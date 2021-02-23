from django.conf.urls import url, include
from . import views
from django.contrib import admin
from django.views.generic import TemplateView
from django.template import Template
from webexample.views import * ##basic_one

#urlpatterns = [
#url(r'^', basic_one),
#url(r'^1/', views.template_two),
#url(r'^2/', views.template_three)]

#from . import views
#from django.contrib import admin
#from django.views.generic import TemplateView
#from django.template import Template
#from django.conf.urls import url views. three

urlpatterns = [
url(r'^/1', basic_one),
url(r'^/2', template_two),
url(r'^/3', template_three)
]


#urlpatterns = [
#url(r'^/', basic_one),
#url(r'webexample/1/', views.template_two),
#url(r'webexample/2/', views.template_three)
#]

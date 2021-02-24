from django.conf.urls import url, include
from . import views
from django.contrib import admin
from django.views.generic import TemplateView
from django.template import Template
from webexample.views import *

urlpatterns = [
url(r'^/1', basic_one),
url(r'^/2', template_two),
url(r'^/3', template_three)
]

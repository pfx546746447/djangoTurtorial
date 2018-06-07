from django.conf.urls import url
from django.contrib import admin
from django.views.generic import ListView, DetailView

from .views import *
from .models import *

urlpatterns = [
    # url(r'^$', index, name='index'),
    # url(r'^(?P<poll_id>\d+)$', detail, name='detail'),
    # url(r'^(?P<poll_id>\d+)/vote/$', vote, name='vote'),
    url(r'^$', ListView.as_view(queryset=Poll.objects.order_by('-pub_date')[:5],
                                context_object_name='polls',
                                template_name='polls/index.html'), name='index'),
    url(r'^(?P<pk>\d+)/$', DetailView.as_view(model=Poll,
                                              template_name='polls/detail.html'), name='detail'),
    url(r'^(?P<poll_id>\d+)/vote/$', vote, name='vote'),

]

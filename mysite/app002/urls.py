from django.conf.urls import url

from . import views

app_name = 'app002'
urlpatterns = [
   
    url(r'^a/([0-9]{2})/$', views.num1),
    url(r'^a/([0-9]{2})/([0-9]{2})/$', views.num2),
    url(r'^a/([0-9]{2})/([0-9]{2})/([0-9]{2})/$', views.num3),
   
   
   
   
    url(r'^$', views.index, name='index'),
    # url(r'^19$', views.index19, name='index19'),
    # url(r'^13$', views.index13, name='index13'),
    # url(r'^8$', views.index08, name='index08'),
    url(r'^me/', views.me, name='me'),
    
    # 範例
    # url(r'^style19/', views.style19, name='style19'),這會觸發任何  style19/XXX
    # url(r'^style19/$', views.style19, name='style19'),
    #   url(r'^item009/(?P<item001_id>[_A-Za-z0-9-\#\\+]+)', views.item009detail, name='item009detail'), #item001/123 後面有東西都好
    # url(r'^form/(?P<num>[0-9]+)', views.form, name='form'), #item001/123 後面有東西都好
    url(r'^form/(?P<num>[0-9]+)', views.form, name='form'), #item001/123 後面有東西都好
    
    url(r'^num1/(?P<num1>[0-9]+)/$', views.num1, name='num1'), 
    url(r'^num2/(?P<num1>[0-9]+)/(?P<num2>[0-9]+)/$', views.num2, name='num2'), 
    url(r'^num3/(?P<num1>[0-9]+)/(?P<num2>[0-9]+)/(?P<num3>[0-9]+)', views.num3, name='num3'), 
    
    url(r'(?P<num1>[0-9]+)/(?P<num2>[0-9]+)/(?P<num3>[0-9]+)$', views.num3, name='num3'), 
    url(r'(?P<num1>[0-9]+)/(?P<num2>[0-9]+)/$', views.num2, name='num2'), 
    url(r'(?P<num1>[0-9]+)/$', views.num1, name='num1'), 
   
]

from django.conf.urls import url

from . import views

app_name = 'app001'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^19$', views.index19, name='index19'),
    url(r'^13$', views.index13, name='index13'),
    url(r'^8$', views.index08, name='index08'),
    url(r'^me/', views.me, name='me'),
    
    # 範例
    # url(r'^style19/', views.style19, name='style19'),這會觸發任何  style19/XXX
    # url(r'^style19/$', views.style19, name='style19'),
   

]

from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'polls'

urlpatterns= [
    #path('admin/', admin.site.urls),
    #polls/
    path('', views.index,name = 'index'),
    #polls/#
    path('<int:question_id>/', views.detail, name='detail'),
    #polls/#/result/
    path('<int:question_id>/result/', views.results, name = 'results'),
    #polls/#/vote
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
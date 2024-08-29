from django.urls import path
from .views import RegisterView,LoginView
from . import views

app_name = 'users'
urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('activate/<str:uid>/<str:token>',views.UserActivateView.as_view(), name ='activate'),
]
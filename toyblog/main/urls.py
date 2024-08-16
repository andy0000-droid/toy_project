from django.contrib import admin
from django.urls import path, include
from . import views as main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls'))
]

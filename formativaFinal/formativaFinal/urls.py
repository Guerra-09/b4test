from django.contrib import admin
from django.urls import path
from elecciones import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.form, name="form"),
    path('form', views.formMessage, name="formMessage"),

    path('votes/', views.votes, name="votes"),
    path('voteDone/', views.voteMessage, name="voteDone"),

    path('results/', views.results, name="results"),
]

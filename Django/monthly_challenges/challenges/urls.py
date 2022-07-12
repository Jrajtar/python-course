from django.urls import URLPattern, path

from . import views

urlpatterns = [
    path("",views.index,name= "index"),
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name= "month-challenge")
    
]

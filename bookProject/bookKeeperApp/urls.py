from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name="index"),
    path("all/",views.all,name="all"),
    path('addbook/',views.addBook,name="addBook"),
    path("past2018/", views.past2018, name="past2018"),

]
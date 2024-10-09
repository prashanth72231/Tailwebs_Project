from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('', views.index, name='home'),
    path('add/',views.add,name="add"),
    path("addrec/",views.addrec,name="addrec"),
    path('update/<int:id>/',views.update,name="update"),
    path('update/uprec/<int:id>/',views.uprec,name="uprec"),
    path('delete/<int:id>/',views.delete,name="delete"),    
]

from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('manage_donors/',views.manage_donors,name="manage_donors"),
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutPage,name="logout"),



    path('add_donor/',views.add_donor,name="add_donor"),
    path('delete_donor/<str:pk>/',views.delete_donor,name="delete_donor"),
    path('update_donor/<str:pk>/',views.update_donor,name="update_donor"),
  
    path('delete_ok/<str:pk>/',views.delete_ok,name="delete_ok"),

    

]

from django.urls import path
from auth_app import views
urlpatterns = [
    path('login/',views.sign_in,name='login'),
    path('logout/',views.sign_out,name='logout'),
    path('register/',views.register,name='register')


]

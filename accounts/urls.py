from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_attempt, name='login_attempt'),
    path('register', views.register_attempt, name='register_attempt'),
    path('otp', views.otp, name='otp'),

]
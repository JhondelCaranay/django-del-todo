from django.urls import path
from .views import login_user, register, logout_user, activate_user


urlpatterns = [
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('logout-user/', logout_user, name='logout-user'),
    path('activate-user/<uidb64>/<token>/',
         activate_user, name='activate-user'),
]

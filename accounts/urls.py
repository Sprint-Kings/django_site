from django.urls import path

from accounts.views import LoginView, SignUpView
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView, name='login'),
    path('signup/', SignUpView, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
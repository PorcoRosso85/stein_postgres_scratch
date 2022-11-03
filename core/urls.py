from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('signup/', views.signup, name='signup'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    # //TODO loginbutton should take us to rooms, but now it takes us to 'account...' page
    path('logout/', LogoutView.as_view(), name='logout'),
]

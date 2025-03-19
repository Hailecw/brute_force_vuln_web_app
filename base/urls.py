from django.urls import path
from .views import VulnLoginView,HomeView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("login/",VulnLoginView.as_view(),name="login"),
    path("",HomeView.as_view(),name="home"),
    path("logout/",LogoutView.as_view(template_name="logout.html"),name="logout")

]

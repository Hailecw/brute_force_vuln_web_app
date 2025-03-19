from django.shortcuts import render
from django.db import connection
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User


class VulnLoginView(LoginView):
    template_name =  "login.html"
    redirect_authenticated_user =True
    def get_success_url(self):
        return reverse_lazy("home")

class HomeView(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = "SELECT * FROM auth_user"
        with connection.cursor() as cursor:
            cursor.execute(query)
            users = cursor.fetchall()
            data = []
            for item in users:
                user = {}
                user["id"] = item[0]
                user["username"] = item[4]
                user["email"] = item[6]
                data.append(user)
        context["data"] = data
        return context
    def post(self,*args, **kwargs):
        search = self.request.POST.get("search")
        search = self.request.POST.get("search")
        query = f"SELECT * FROM auth_user WHERE username LIKE '%{search}%'"
        print(query)
        with connection.cursor() as cursor:
            cursor.execute(query)
            users = cursor.fetchall()
            data = []
            for item in users:
                user = {}
                user["id"] = item[0]
                user["username"] = item[4]
                user["email"] = item[6]
                data.append(user)
            print(data)
        return render(self.request,"home.html",{"data":data})

        


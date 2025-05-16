"""point_experts_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sistema_escolar_api.views import bootstrap
from sistema_escolar_api.views import users
from sistema_escolar_api.views import auth
from sistema_escolar_api.views import events

urlpatterns = [
    #Version
        path('bootstrap/version', bootstrap.VersionView.as_view()),
    #Create Admin
        path('admin/', users.AdminView.as_view()),
    #Admin Data
        path('lista-admins/', users.AdminAll.as_view()),
    #Edit Admin
        path('admins-edit/', users.AdminsViewEdit.as_view()),
    #Create Alumno
        path('alumnos/', users.AlumnoView.as_view()),
    #Edit Alumno
        path('alumnos-edit/', users.AlumnoViewEdit.as_view()),
    #Create Maestro
        path('maestros/', users.MaestrosView.as_view()),
    #Edit Maestro
        path('maestros-edit/', users.MaestrosViewEdit.as_view()),
    #Maestro Data
        path('lista-maestros/', users.MaestrosAll.as_view()),
    #Lista Data
        path('lista-alumnos/', users.AlumnosAll.as_view()),
    #Login
        path('token/', auth.CustomAuthToken.as_view()),
    #Logout
        path('logout/', auth.Logout.as_view()),
    # Ruta para registrar (crear) un evento
        path('eventos/', events.EventoView.as_view()),
    # (Opcional) Ruta para editar un evento
        path('eventos-edit/', events.EventoViewEdit.as_view()),
    #Lista de eventos
        path('lista-eventos/', events.EventoView.as_view()),

]

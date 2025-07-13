from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("logout/", views.logout_view, name="logout"),
    path("dashboard/", views.dashboard_redirect, name="dashboard_redirect"),
    path("dashboard/doctor/", views.doctor_dashboard, name="doctor_dashboard"),
    path(
        "dashboard/radiologist/",
        views.radiologist_dashboard,
        name="radiologist_dashboard",
    ),
    path("dashboard/patient/", views.patient_dashboard, name="patient_dashboard"),
]

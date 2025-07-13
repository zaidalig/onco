from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("logout/", views.logout_view, name="logout"),
    path("dashboard/", views.dashboard_redirect, name="dashboard_redirect"),
    path("dashboard/admin/", views.admin_dashboard, name="admin_dashboard"),
    path("dashboard/doctor/", views.doctor_dashboard, name="doctor_dashboard"),
    path(
        "dashboard/radiologist/",
        views.radiologist_dashboard,
        name="radiologist_dashboard",
    ),
    path("dashboard/patient/", views.patient_dashboard, name="patient_dashboard"),
    path('admin/doctors/', views.admin_doctors_view, name='admin_doctors'),
    path('admin/radiologists/', views.admin_radiologists_view, name='admin_radiologists'),
    path('admin/patients/', views.admin_patients_view, name='admin_patients'),
    path('admin/reports/', views.admin_reports_view, name='admin_reports'),
    path('admin/user/toggle/<int:user_id>/', views.toggle_user_status, name='toggle_user_status'),

]

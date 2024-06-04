from django.urls import path
from admin_interface import views

urlpatterns = [
    # Другие URL-ы
    path('admin_sp/', views.admin_sp, name='admin_sp'),
    path('login/', views.login_view, name='login'),
]

from django.urls import path
from admin_interface import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin_sp/', views.admin_sp, name='admin_sp'),
    path('login/', views.login_view, name='login'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('admin_sp/add_category/', views.add_category, name='add_category'),
    path('admin_sp/edit_category/<int:category_id>/', views.edit_category, name='edit_category'),
    path('admin_sp/delete_category/<int:category_id>/', views.delete_category, name='delete_category'),
    path('admin_sp/add_service/', views.add_service, name='add_service'),
    path('admin_sp/edit_service/<int:service_id>/', views.edit_service, name='edit_service'),
    path('admin_sp/delete_service/<int:service_id>/', views.delete_service, name='delete_service'),
]

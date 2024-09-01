from django.urls import path
from admin_interface import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin_sp/', views.admin_sp, name='admin_sp'),
    path('login/', views.login_view, name='login'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'),
         name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),
    path('admin_sp/add_category/', views.add_category, name='add_category'),
    path('admin_sp/edit_category/<int:category_id>/', views.edit_category, name='edit_category'),
    path('admin_sp/delete_category/<int:category_id>/', views.delete_category, name='delete_category'),
    path('admin_sp/add_service/', views.add_service, name='add_service'),
    path('admin_sp/edit_service/<int:service_id>/', views.edit_service, name='edit_service'),
    path('admin_sp/delete_service/<int:service_id>/', views.delete_service, name='delete_service'),
    # Color URLs
    path('admin_sp/add_color/', views.add_color, name='add_color'),
    path('admin_sp/edit_color/<int:color_id>/', views.edit_color, name='edit_color'),
    path('admin_sp/delete_color/<int:color_id>/', views.delete_color, name='delete_color'),
    # ProductCategory URLs
    path('admin_sp/add_product_category/', views.add_product_category, name='add_product_category'),
    path('admin_sp/edit_product_category/<int:category_id>/', views.edit_product_category, name='edit_product_category'),
    path('admin_sp/delete_product_category/<int:category_id>/', views.delete_product_category, name='delete_product_category'),
    # Product URLs
    path('admin_sp/add_product/', views.add_product, name='add_product'),
    path('admin_sp/edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('admin_sp/delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    # ProductVariant URLs
    path('admin_sp/add_product_variant/', views.add_product_variant, name='add_product_variant'),
    path('admin_sp/edit_product_variant/<int:variant_id>/', views.edit_product_variant, name='edit_product_variant'),
    path('admin_sp/delete_product_variant/<int:variant_id>/', views.delete_product_variant, name='delete_product_variant'),
    # Adress URLs
    path('admin_sp/add_address/', views.add_adress, name='add_address'),
    path('admin_sp/edit_address/<int:adress_id>/', views.edit_adress, name='edit_address'),
    path('admin_sp/delete_address/<int:adress_id>/', views.delete_adress, name='delete_address'),
    # News URLs
    path('admin_sp/add_news/', views.add_news, name='add_news'),
    path('admin_sp/edit_news/<int:news_id>/', views.edit_news, name='edit_news'),
    path('admin_sp/delete_news/<int:news_id>/', views.delete_news, name='delete_news'),
]


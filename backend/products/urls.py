from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/', views.product_detail_view),
    path('<int:pk>/update/', views.product_update_view),
    path('<int:pk>/delete/', views.product_destroy_view),
    path('', views.product_list_create_view)
]
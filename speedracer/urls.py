from django.urls import path
from . import views
from Inventory import views as v1

urlpatterns = [
    path('', views.login, name="login"),
    path('home/', views.home, name="home"),

    path('products/', views.products, name='products'),

    path('inventory/', v1.list_item, name='inventory'),
    path('add/', v1.create_item, name='add_item'),
    path('update/<int:id>/', v1.update_item, name='update_item'),
    path('delete/<int:id>/', v1.delete_item, name='delete_item'),
    path('search_basic/', v1.search_basic, name='search_item'),
    path('search/', v1.search, name = 'search_item2'),
    path('manager/<str:pk_test>/', views.manager, name="manager"),

    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),



]

from django.urls import path

from index import views

urlpatterns = [
    path(' ', views.home, name = 'home'),
    path('author', views.author, name = 'author'),
    path('',views.list_sales, name = 'list_music'),
    path('new/',views.create_sales, name = 'add_music'),
    path('update/<int:id>/', views.update_sale, name = 'update_music'),
    path('delete/<int:id>/', views.delete_sale, name = 'delete_music'),
    path('search_basic/', views.search_basic, name = 'search_music'),
]

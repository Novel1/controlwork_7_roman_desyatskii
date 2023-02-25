from django.urls import path

from webapp import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('book/add/', views.add_view, name='add'),
    path('book/<int:pk>/update/', views.update_view, name='book_update'),
    path('book/<int:pk>/delete/', views.delete_view, name='book_delete'),
    path('book/<int:pk>/confirm_dalete/', views.confirm_delete, name='confirm_delete')
]
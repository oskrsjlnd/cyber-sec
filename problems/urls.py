from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('account/', views.account_view, name="account"),
    path('register/', views.register_view, name="register"),
    path('write/', views.write_view, name='write'),
    path('logout/', views.logout_view, name='logout'),
    path('show_entries/', views.show_entries_view, name='show entries'),
]
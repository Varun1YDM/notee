from django.urls import path

from . import views

urlpatterns = [

   path('', views.HomeView.as_view(), name='home'),
   path('login/', views.LoginView.as_view(), name='login'),
   path('register/', views.RegisterView.as_view(), name='register'),
   path('logout/', views.logout_view, name='logout'),
   path("user/",views.NotesView.as_view(),name="user"),
   path('update', views.UpdateView.as_view(), name='update'),
   path('delete', views.DeleteView.as_view(),name='delete'),
]


# path('', views.HomeView.as_view(), name='home'),
#     path('notes/', views.NotesView.as_view(), name='notes'),
#     path('update', views.UpdateView.as_view(), name='update'),
#     path('delete', views.DeleteView.as_view(),name='delete'),
    
#     path('login/', views.LoginView.as_view(), name='login'),
#     path('register/', views.RegisterView.as_view(), name='register'),
#     path('logout/', views.logout_view, name='logout'),


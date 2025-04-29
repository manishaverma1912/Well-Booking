from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('contact/', views.contact, name='contact'),
    path('profile/', views.profile, name='profile'),
    path('book-event/', views.book_event, name='book_event'),
    path('event/<int:pk>/', views.event_view, name='event_view'),
    path('event/<int:pk>/edit/', views.event_edit, name='event_edit'),
    path('event/<int:pk>/cancel/', views.event_cancel, name='event_cancel'),
    path('base/' , views.base ,name='base'),

]

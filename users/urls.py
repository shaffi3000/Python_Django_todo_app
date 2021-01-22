from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('complete/<todo_id>', views.completeTodo, name='complete'),
#     path('deletecomplete/', views.deleteComplete, name='deletecomplete'),

# ]


urlpatterns = [
    path('users/', views.index, name='users/index'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile')
]



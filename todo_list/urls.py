from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('complete/<todo_id>', views.completeTodo, name='complete'),
    path('deletecomplete/', views.deleteComplete, name='deletecomplete'),
    path('deleteall/', views.deleteAll, name='deleteall')
]
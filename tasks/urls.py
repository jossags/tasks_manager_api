from django.urls import path
from . import views

urlpatterns = [ #UserURLS
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    #URLTASK, GET, POST
    path('tasks/', views.task_list_create, name='task_list_create'),
    
    #GET-SEE, PUT-EDIT, DELETE
    path('tasks/<int:pk>/', views.task_detail, name='task_detail'),
]
from django.urls import path
from . import views



urlpatterns=[
    path('',views.user_form,name="user_insert"),#get and post for insert oper
    path('<int:id>/',views.user_form,name="user_update"),
    path('delete/<int:id>/',views.user_delete,name='user_delete'),
    path('list/',views.user_List,name="user_list"),
]
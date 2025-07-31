from django.urls import path
from . import views

urlpatterns = [
    path('', views.func_page, {'page':'login'}),
    path('login/', views.func_page, {'page':'login'}, name='login'),

    path('infor/', views.func_page, {'page':'infor'}, name='infor'),
    path('job/',views.func_page, {'page':'job'}, name='job'),
    path('manage/',views.func_page, {'page':'manage'}, name='manage'),

    path('asignWork/',views.asignWork),
    path('updateData/',views.updateData),

    path('logout/', views.func_page, {'page':'logout'}, name='logout')
]
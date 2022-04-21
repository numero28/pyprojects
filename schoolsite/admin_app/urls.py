from django.urls import path
from . import views

app_name = 'admin_app'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('next_stage/', views.administration, name='administration'),
    path('next_stage/another_one/', views.administration, name='administration')
]
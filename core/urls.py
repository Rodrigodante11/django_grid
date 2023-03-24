from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.view1, name="view1"),
    path('', views.view2, name="view2"),
    path('consulta_cep/<input_value>/', views.consulta_cep, name='consulta_cep'),
]
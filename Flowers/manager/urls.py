from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('type/<int:type_id>/', types, name='type_detail'),
    path('flower/<int:flower_id>/', flower, name='flower_detail'),
    path('type/add/', addType, name='addType'),
    path('flower/add/', addFlower, name='addFlower')
]
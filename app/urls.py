from django.urls import path
from .views import *

urlpatterns = [
    path('', crud_page),
    path('chart/', chart_page),

    path('create/', create),
    path('list/', list_items),
    path('update/<int:id>/', update),
    path('delete/<int:id>/', delete),
    path('report/', report),
    path('external/', external),
]


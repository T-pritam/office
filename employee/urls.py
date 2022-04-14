from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='home'),
    path('details', views.details,name='details'),
    path('add', views.add,name='add'),
    path('remove', views.remove,name='remove'),
    path('remove/<int:emp_id>', views.remove,name='remove'),
    path('search', views.search,name='search'),
]

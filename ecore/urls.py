from django.urls import path, include
from . views import item_list


app_name = 'ecore'

urlpatterns = [
	path('', item_list, name='item_list'),
]
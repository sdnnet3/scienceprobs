from django.urls import path
from . views import main, physics, ChemDetailView, ChemListView



app_name = 'tutorials'

urlpatterns = [
    path('', main, name='main'),
    path('genchem/', ChemListView.as_view(), name='chemList'),
    path('genchem/<str:slug>/', ChemDetailView.as_view(), name='chemDetail'),
    path('physics/', physics, name='physics'),
]

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from .models import Topic


# Create your views here.
def main(request):
	return HttpResponse("HttpResponse")

class ChemDetailView(DetailView):
	model = Topic
	# context_object_name = 'topic'
	queryset = Topic.objects.all()
	# template_name = 'tutorial/genchem.html'
	# ordering = ['-']

class ChemListView(ListView):
	model = Topic
	context_object_name = 'topic'
	queryset = Topic.objects.all()
	# template_name = 'tutorial/genchem_list.html'

# def genchem(request):
# 	context = {}
# 	return render(request, 'tutorial/genchem.html', context)

def physics(request):
	pass
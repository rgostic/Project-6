from random import randint

from django.shortcuts import render
from .models import Mineral
# Create your views here.
def index(request):
	minerals = Mineral.objects.all()
	return render(request, 'minerals/index.html', {"minerals": minerals})

def detail(request, mineral_id):
	mineral	= Mineral.objects.get(pk=mineral_id)
	return render(request, 'minerals/detail.html', {"mineral": mineral})

def random(request):
	cnt = Mineral.objects.count()	
	randomInd = randint(0, cnt)
	mineral = Mineral.objects.get(pk=randomInd)
	
	return render(request, 'minerals/detail.html', {"mineral": mineral})

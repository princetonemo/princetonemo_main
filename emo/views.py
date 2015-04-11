from django.shortcuts import render
from django.http import HttpResponse
from emo.models import UserProfile, Department

# Create your views here.
def index(request):
	if request.method == 'POST':
		print 'Received a search query'
		form = DepartmentSearchForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			print(data['query'])
		else
			print form.errors

	return HttpResponse('This will be the EMO homepage')


def department(request):

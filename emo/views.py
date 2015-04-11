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
			return department(request, data)
		else:
			print form.errors
	#else: # was a GET
	return render(request, 'emo/index.html')


def department(request, abbr):
	dep_list = Department.objects.filter(abbr=abbr)
	if dep_list: # valid department
		dep = dep_list[0]
		num_students = dep.num_students
		name = dep.name
	#else: # not a valid department

	return HttpResponse('The department you searched was ' + abbr)

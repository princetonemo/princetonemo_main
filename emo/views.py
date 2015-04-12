from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from emo.models import UserProfile, Department
from emo.forms import DepartmentSearchForm

# Create your views here.
def index(request):
	if request.method == 'POST':
		print 'Received a search query'
		form = DepartmentSearchForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			print(data['query'])
			return HttpResponseRedirect('/emo/' + data['query'].upper())
		else:
			print form.errors
	#else: # was a GET
	form = DepartmentSearchForm()
	context_dict = {'form': form}
	return render(request, 'emo/index.html', context_dict)


def department(request, abbr):
	if request.method == 'POST':
		print 'Received a search query'
		form = DepartmentSearchForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			print(data['query'])
			return HttpResponseRedirect('/emo/' + data['query'])
		else:
			print form.errors
			context_dict = {'abbr': abbr, 'form': form}
			return render(request, 'emo/no-dept.html', context_dict)
	else:
		form = DepartmentSearchForm() 
		dep_list = Department.objects.filter(abbr=abbr)
		if dep_list: # valid department
			dep = dep_list[0]
			context_dict = {'dep': dep, 'form': form}
			return render(request, 'emo/dept.html', context_dict)
		else: # not a valid department
			context_dict = {'abbr': abbr, 'form': form}
			return render(request, 'emo/no-dept.html', context_dict)

from django import forms

class DepartmentSearchForm(forms.Form):
	query = forms.CharField(help_text = "Search by Department", max_length=3)

	class Meta:
		fields = ('query',)
		exclude = ()
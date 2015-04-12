from django import forms

class DepartmentSearchForm(forms.Form):
	query = forms.CharField(max_length=3)

	class Meta:
		fields = ('query',)
		exclude = ()
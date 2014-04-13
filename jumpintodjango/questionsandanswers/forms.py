from django import forms

class QuestionForm(forms.Form):
	subject = forms.CharField(max_length=100, required=True)
	description = forms.CharField(widget=forms.Textarea, required=True)
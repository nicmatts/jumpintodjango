from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.utils import timezone

from questionsandanswers.models import Question
from questionsandanswers.forms import QuestionForm

def index(request):
	questions = Question.objects.all()
	return render_to_response('questionsandanswers/index.html', {'questions': questions})

def question_detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render_to_response('questionsandanswers/question_detail.html', {'question': question})

def question_create(request):
	if request.method == 'POST':
		form = QuestionForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/questions')	
	else:
		form = QuestionForm()
	return render_to_response('questionsandanswers/question_create.html', {'form': form}, context_instance=RequestContext(request))

def question_edit(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	if request.method=='POST':
		form = QuestionForm(request.POST, instance=question)
		if form.is_valid():
			form.save()
			return redirect('question_detail', question_id)
	else:
		form = QuestionForm(instance=question)
	return render_to_response('questionsandanswers/question_edit.html', {'form': form}, context_instance=RequestContext(request))
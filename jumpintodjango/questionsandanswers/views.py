from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from questionsandanswers.models import Question
from .forms import QuestionForm

def index(request):
	questions = Question.objects.all()
	return render_to_response('questionsandanswers/index.html', {'questions': questions})

def question_detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render_to_response('questionsandanswers/question_detail.html', {'question': question})

def question_create(request):
	form = QuestionForm()
	return render_to_response('questionsandanswers/question_create.html', {'form': form}, context_instance=RequestContext(request))
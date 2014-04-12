from django.contrib import admin
from questionsandanswers.models import Question, Answer
# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
	list_display = ('subject', 'description', 'publication_date',)

admin.site.register(Question, QuestionAdmin)
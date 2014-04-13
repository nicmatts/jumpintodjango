from django.contrib import admin
from questionsandanswers.models import Question, Answer
# Register your models here.
# class QuestionAdmin(admin.ModelAdmin):
# 	list_display = ('subject', 'description', 'publication_date',)

# class AnswerAdmin(admin.ModelAdmin):
# 	list_display = ('question', 'content', 'best_answer',)
class AnswerInline(admin.StackedInline):
	model = Answer
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	inlines = [AnswerInline]
	list_display = ('subject', 'publication_date', 'published_today')
	list_filter = ['publication_date']
	search_fields = ['subject']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
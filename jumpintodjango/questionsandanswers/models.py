from django.db import models

class Question(models.Model): 
	subject = models.CharField(max_length=200)
	description = models.TextField()
	publication_date = models.DateTimeField()

class Answer(models.Model):
	question = models.ForeignKey(Question)
	content = models.TextField()
	best_answer = models.BooleanField("preferred answer", default=False)

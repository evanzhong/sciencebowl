from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

class Topics(models.Model):
	comp = models.CharField(max_length=100)
	subject = models.CharField(max_length=100)
	subtopic = models.CharField(max_length=100)

class Author(models.Model):
	author_first = models.CharField(max_length=100)
	author_last = models.CharField(max_length=100)

class MultChoice(models.Model):
	w = models.CharField(max_length=100)
	x = models.CharField(max_length=100)
	y = models.CharField(max_length=100)
	z = models.CharField(max_length=100)
	correct = models.CharField(max_length=1, choices=("w","x","y","z"))

class Question(models.Model):
	subject = models.ForeignKey(Topics, on_delete=models.CASCADE)
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	date_written = models.DateTimeField('date created', auto_now_add=True) #maybe not correct
	date_last_mod = models.DateTimeField('date created', auto_now_add=True) #maybe not correct
	question_type = models.CharField(max_length=20)
	question_text = models.CharField(max_length=10000) # change max length?
	short_answer_answer_text = models.CharField(max_length=10000)
	mult_choice_choices = models.ForeignKey(MultChoice, on_delete=models.CASCADE)

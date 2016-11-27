from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

class Topics(models.Model):
	comp = models.CharField(max_length=100)
	subject = models.CharField(max_length=100)
	subtopic = models.CharField(max_length=100)
	category = models.CharField(max_length=100)

class Author(models.Model):
	name = models.CharField(max_length=100)
	set_number = models.CharField(max_length=4)

class Question(models.Model):
	subject = models.ForeignKey(Topics, on_delete=models.CASCADE)
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	date_written = models.DateTimeField('date created', auto_now_add=True) #maybe not correct
	date_last_mod = models.DateTimeField('date created', auto_now_add=True) #maybe not correct
	question_type = models.CharField(max_length=20)
	question_text = models.CharField(max_length=10000) # change max length?
	short_answer_answer_text = models.CharField(max_length=10000)
	w = models.CharField(max_length=100)
	x = models.CharField(max_length=100)
	y = models.CharField(max_length=100)
	z = models.CharField(max_length=100)
	correct = models.CharField(max_length=1)
	difficulty = models.IntegerField()
	
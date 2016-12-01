from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

class Question(models.Model):
	comp = models.CharField(max_length=100,default=None, blank=True, null=True) #Be consistant w/ either value "NSB" or "NOSB"
	subject = models.CharField(max_length=100, default=None, blank=True, null=True) #Andrew has a list of subjects (8 for NSB and 5 for NOSB)
	subtopic = models.CharField(max_length=100, default=None, blank=True, null=True) #This will be harder to keep consistant -> will need better system
	question_type = models.CharField(max_length=20, default=None, blank=True, null=True)
	question_text = models.CharField(max_length=10000, default=None, blank=True, null=True) # change max length?
	w = models.CharField(max_length=100, default=None, blank=True, null=True)
	x = models.CharField(max_length=100, default=None, blank=True, null=True)
	y = models.CharField(max_length=100, default=None, blank=True, null=True)
	z = models.CharField(max_length=100, default=None, blank=True, null=True)
	correct = models.CharField(max_length=1, default=None, blank=True, null=True)
	short_answer_answer_text = models.CharField(max_length=10000, default=None, blank=True, null=True)
	name = models.CharField(max_length=100, default=None, blank=True, null=True) #Author (First Last)
	set_number = models.CharField(max_length=4, default=None, blank=True, null=True) 
	difficulty = models.IntegerField(default=None, blank=True, null=True)
	category = models.CharField(max_length=100, default=None, blank=True, null=True)
	date_written = models.DateTimeField('date created', auto_now_add=True, blank=True, null=True) #maybe not correct
	date_last_mod = models.DateTimeField('date last modified', auto_now_add=True, blank=True, null=True) #maybe not correct

import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
	def __str__(self):
		return self.question_text

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

class Choice(models.Model):
	def __str__(self):
		return self.choice_text
	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

class Author(models.Model):
	def __str__(self):
		return self.first_name+" "+self.last_name
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	bio = models.TextField()
	tagline = models.CharField(max_length = 200)

class Player(models.Model):
	SPORT_CHOICES = (
		("NFL", "NFL"),
		("NBA","NBA")
		) 
	def __str__(self):
		return self.first_name+" "+self.middle_name+" "+self.last_name
	first_name = models.CharField(max_length=200)
	middle_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	position = models.CharField(max_length=200)
	sport = models.CharField(max_length=20, choices=SPORT_CHOICES)
	team = models.CharField(max_length=200)
	salary = models.IntegerField(default=0)
	#player.incident_set.all()
	#nationality = models.CharField(max_length=200)
	#years_active = models.IntegerField(default=0)
	#college = models.CharField(max_length=200)

class Accolade(models.Model):
	def __str__(self):
		return self.title
	title = models.CharField(max_length=200)
	accolade_text = models.TextField()
	player = models.ForeignKey(Player)

class Incident(models.Model):
	def __str__(self):
		return self.name
	name = models.CharField(max_length=200)
	crime = models.TextField()
	players = models.ManyToManyField(Player)
	pub_date = models.DateTimeField('date published')

class Update(models.Model):
	def __str__(self):
		return self.headline
	byline = models.CharField(max_length=200)
	headline = models.CharField(max_length=200)
	update_text = models.TextField()
	incident = models.ForeignKey(Incident)
	pub_date = models.DateTimeField('date published')


class Article(models.Model):
	def __str__(self):
		return self.headline
	headline = models.CharField(max_length=200)
	article_text = models.TextField()
	players = models.ManyToManyField(Player)
	incidents = models.ManyToManyField(Incident)
	bylines = models.ManyToManyField(Author)
	pub_date = models.DateTimeField('date published')

class Team(models.Model):
	SPORT_CHOICES = (
		("NFL", "NFL"),
		("NBA","NBA")
		)
	def __str__(self):
		return self.name
	name = models.CharField(max_length=200)
	




# class Incident(models.Model):
# 	title = models.CharField(max_length=200)
# 	players = models.ManyToManyField(Player)
# 	incident_text = models.CharField(max_length=200)

# class Update(models.Model):
# 	update = models.ForeignKey(Incident)


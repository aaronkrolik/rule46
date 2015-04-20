from django.shortcuts import render
from django.http import HttpResponse

from django.template import RequestContext, loader

from polls.models import Question, Player, Team, Incident
# Create your views here.

def index(request):
	latest_question_list = Question.objects.order_by("-pub_date")[:5]
	template = loader.get_template('index.html')
	context = RequestContext(request, {
		'latest_question_list': latest_question_list,
		})
	return HttpResponse(template.render(context))

def detail(request, question_id):
	return HttpResponse("you're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def player_lp(request):
	landing_dict = {}
	landing_dict["NFL"] = ["A","B","C","D"]
	landing_dict["NBA"] = ["E","F","G", "H"]
	template = loader.get_template("landing.html")
	context = RequestContext(request, {
			"landing_dict": landing_dict,
			"lp": "team",
		})
	return HttpResponse(template.render(context))

def player(request, player_id):
	player = Player.objects.all()[0]
	template = loader.get_template("player.html")
	context = RequestContext(request, {
		'player': player,
		})
	return HttpResponse(template.render(context))

def team(request, team_id):
	team = Team.objects.get(team_id=team_id)
	context = RequestContext(request, {
		'team': team,
		})
	return HttpResponse("player page %s." % team_id)

def incident(request, incident_id):
	incident = Player.objects.get(name=incident_id)
	context = RequestContext(request, {
		'incident': incident,
		})
	return HttpResponse("player page %s." % incident_id)
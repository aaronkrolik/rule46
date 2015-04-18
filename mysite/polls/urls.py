from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
     # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),

    url(r'^player/(?P<player_id>\d+)/$', views.player, name='player'),

	url(r'^incident/(?P<incident_id>\d+)/$', views.incident, name='incident'),

	url(r'^team/(?P<team_id>\d+)/$', views.team, name='team'),    

)
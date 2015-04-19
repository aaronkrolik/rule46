from django.contrib import admin
from polls.models import *
# Register your models here.

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	list_display = ("question_text",'pub_date','was_published_recently')
	fieldsets = [
	(None, {'fields':['question_text']}),
	('Date information',{'fields':['pub_date'],
						 'classes':['collapse']}),
	]
	inlines = [ChoiceInline]

class UpdateInline(admin.TabularInline):
	model = Update
	extra = 0

class IncidentAdmin(admin.ModelAdmin):
	list_display = ("name","crime")
	inlines = [UpdateInline]

class AccoladeInline(admin.TabularInline):
	model = Accolade
	extra = 0

class PlayerAdmin(admin.ModelAdmin):
	list_display = ("last_name","sport")
	list_filter = ['sport']
	inlines = [AccoladeInline]

class ArticleAdmin(admin.ModelAdmin):
	list_display = ("headline", "pub_date")


admin.site.register(Player, PlayerAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Incident, IncidentAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Author)
admin.site.register(Team)
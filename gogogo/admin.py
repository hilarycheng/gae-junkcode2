from django.contrib import admin
from django import forms
from ragendja.forms import *
from gogogo.models import Agency , Stop , Route

class AgencyAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'url', 'timezone', 'phone')
        }),

    )
    
    list_display = ('Agency_Name','url')	
    
    search_fields = ('name',)
    
    def Agency_Name(self,obj):
    	return u' | '.join(obj.name)

admin.site.register(Agency, AgencyAdmin)

class StopAdmin(admin.ModelAdmin):	
	search_fields = ('name',)
	
	list_display = ('name',)

admin.site.register(Stop, StopAdmin)

class RouteAdmin(admin.ModelAdmin):
	pass
	
admin.site.register(Route, RouteAdmin)

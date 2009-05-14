# -*- coding: utf-8 -*-
from google.appengine.ext import db
from ragendja.dbutils import KeyListProperty
from django import forms
from django.utils.safestring import mark_safe
from django.conf import settings
from TitledStringListProperty import TitledStringListProperty

class MLStringProperty(TitledStringListProperty):
	"""
		Multi-language string property
	"""
	def __init__ (self,*args,**kwargs):
		fields = []
		for f in settings.LANGUAGES:
			fields.append(f[1])
		
		super(MLStringProperty,self).__init__(fields,*args,**kwargs)

class Agency(db.Model):
	"""
		Public transportation agency
	"""
	name = MLStringProperty()
	
	url = db.StringProperty()
	
	timezone = db.StringProperty()
	
	phone = db.PhoneNumberProperty()
	
	#desc = MLStringProperty() - Later will implement a text input for multiple language handling

class Stops(db.Model):
	# An ID that uniquely identifies a stop or station. Multiple routes may use the same stop. 
	sid = db.StringProperty()
	
	# Optional field
	code = db.StringProperty()
	
	# name of the Stop (Multiple language)
	name = MLStringProperty()
	
	desc = MLStringProperty()

	# latitude and longitude value, it won't use the indexing function from BigTable. Use geohash instead
	latlng = db.GeoPtProperty()
	
	geohash = db.StringProperty()
	
	# TRUE if the geo position data is accuracy enough 
	accuracy = db.BooleanProperty()
	
	url = db.LinkProperty()
	
	location_type = db.IntegerProperty()
	
	parent_station = db.SelfReferenceProperty()
	
class Routes(db.Model):	
	rid = db.StringProperty()
	
	#agency = db.ReferenceProperty(agency)
	
	short_name = db.StringListProperty()
	
	long_name = db.StringListProperty()
	
	desc = db.StringListProperty()
	
	type = db.IntegerProperty()
	
	url = db.LinkProperty()
	
	color = db.StringProperty()
	
	text_color = db.StringProperty()

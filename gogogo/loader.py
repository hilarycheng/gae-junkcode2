from google.appengine.ext import db
from google.appengine.tools import bulkloader
from google.appengine.ext import bulkload

import sys
import os

sys.path.insert(0 , os.path.abspath(os.path.dirname(__file__) + "/../common/appenginepatch"))
sys.path.insert(0 , os.path.abspath(os.path.dirname(__file__) + "/../"))
import main
import gogogo.models

class AgencyLoader(bulkloader.Loader):
	def __init__(self):
		bulkloader.Loader.__init__(self, 'gogogo_agency',
                               [('name', lambda x: unicode(x,'utf-8').split(u'|') ),
                                ('url', str),
                                ('phone', str),
                                ('timzone',str),                                
                               ])

loaders = [AgencyLoader]


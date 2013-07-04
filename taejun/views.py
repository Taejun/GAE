# -*- coding:utf-8 -*-
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

from google.appengine.api import users
from jinja2 import Environment, FileSystemLoader
from os import path
import webapp2
#from google.appengine.ext import db
from models import Board


jinja_env = Environment(autoescape=True,
    loader=FileSystemLoader(path.join(path.dirname(__file__), 'templates')))



class MainPage(webapp2.RequestHandler):

    def get(self):
        user = users.get_current_user()

        if user:
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('Hello, ' + user.nickname())
        else:
            self.redirect(users.create_login_url(self.request.uri))

class SubPage(webapp2.RequestHandler):
    def get(self):
        q = Board.all()
        results = q.fetch(limit=10)
        
        values = {'name': results}
        
        template = jinja_env.get_template('index.html')
        self.response.out.write(template.render(values))
        
        
class Input(webapp2.RedirectHandler):
    def get(self):
        subject = self.request.get("subject")
        content = self.request.get("content")
        q = Board(subject=subject,content=content)
        q.put()
        
        
            

# -*- coding:utf-8 -*-
import webapp2
import views
from google.appengine.ext.webapp.util import run_wsgi_app

application = webapp2.WSGIApplication([
    ('/', views.MainPage),

], debug=True)




def main():
    run_wsgi_app(application)

if __name__ == '__main__':
    main()
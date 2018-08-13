import webapp2
import os
import jinja2


jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Welcome to Study Spot")
class LogInHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Log In Here")
class AddCoursesHandler(webapp2.RequestHandler):
    def get(self):
        self.respone.write("Add Courses Here")
class AddTestsHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Add test dates")

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/login', LogInHandler),
    ('/addcourses', AddCoursesHandler),
    ('/tests', AddTestsHandler)

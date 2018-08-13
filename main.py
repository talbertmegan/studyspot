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
        LogIn_template = jinji_current_directory.get_template("/templates/login.html")
        self.response.write("Log In Here")

class AddCoursesHandler(webapp2.RequestHandler):
    def get(self):
        addcourses_template = jinji_current_directory.get_template("/templates/addcourses.html")
        self.respone.write("Add Courses Here")

class AddTestsHandler(webapp2.RequestHandler):
    def get(self):
        addtests_template = jinji_current_directory.get_template("/templates/tests.html")
        self.response.write("Add test dates")

class SignUpHandler(webapp2.RequestHandler):
    def get(self):
        SignUp_template = jinja_current_directory.get_template(
            "/templates/signup.html")
        self.response.write("Sign Up Here")

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/login', LogInHandler),
    ('/addcourses', AddCoursesHandler),
    ('/tests', AddTestsHandler),
    ('/signup', SignUpHandler),
        ], debug=True)

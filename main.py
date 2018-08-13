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
<<<<<<< HEAD
<<<<<<< HEAD
        
=======
=======

>>>>>>> f55f8c9e490949048ea955818fdf0612516ca446
class LogInHandler(webapp2.RequestHandler):
    def get(self):
        LogIn_template = jinja_env.get_template("/templates/login.html")
        self.response.write("Log In Here")

class AddCoursesHandler(webapp2.RequestHandler):
    def get(self):
        addcourses_template = jinja_env.get_template("/templates/addcourses.html")
        self.response.write(addcourses_template.render())

class AddTestsHandler(webapp2.RequestHandler):
    def get(self):
        addtests_template = jinja_env.get_template("/templates/tests.html")
        self.response.write("Add test dates")
<<<<<<< HEAD
>>>>>>> 7a550a50f9d6b72bb8fc3ce9c26d614a37f84fd8
class SignupHandler(webapp2.RequestHandler):
=======

class SignUpHandler(webapp2.RequestHandler):
>>>>>>> f55f8c9e490949048ea955818fdf0612516ca446
    def get(self):
        SignUp_template = jinja_env.get_template(
            "/templates/signup.html")
        self.response.write("Sign Up Here")

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/login', LogInHandler),
    ('/addcourses', AddCoursesHandler),
    ('/tests', AddTestsHandler),
<<<<<<< HEAD
    ('/signup', SignupHandler),
<<<<<<< HEAD
    ], debug=True)
=======
=======
    ('/signup', SignUpHandler),
>>>>>>> f55f8c9e490949048ea955818fdf0612516ca446
        ], debug=True)
>>>>>>> 7a550a50f9d6b72bb8fc3ce9c26d614a37f84fd8

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
        google_login_template = jinja_env.get_template("/templates/google_login.html")
        new_user_template = jinja_env.get_template("/templates/new_user.html")

        user = users.get_current_user()

        if user:
            existing_user = User.query().filter(User.email == user.email()).get()
            username = user.username()
        else:
            self.response.write(google_login_template.render({ }))



class AddCoursesHandler(webapp2.RequestHandler):
    def get(self):
        addcourses_template = jinji_env.get_template("/templates/addcourses.html")
        self.respone.write("Add Courses Here")

class AddTestsHandler(webapp2.RequestHandler):
    def get(self):
        addtests_template = jinji_env.get_template("/templates/tests.html")
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

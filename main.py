import webapp2
import os
import jinja2


jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template= jinja_env.get_template("/templates/home.html")
        self.response.write(template.render())

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
        addcourses_template = jinja_env.get_template("/templates/addcourses.html")
        self.response.write(addcourses_template.render())
    def post(self):
        self.response.write("This is where I will add the course")

class AddTestsHandler(webapp2.RequestHandler):
    def get(self):
        addtests_template = jinja_env.get_template("/templates/tests.html")
        self.response.write("Add test dates")

class SignUpHandler(webapp2.RequestHandler):
    def get(self):
        SignUp_template = jinja_env.get_template(
            "/templates/signup.html")
        self.response.write("Sign Up Here")

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/login', LogInHandler),
    ('/addcourses', AddCoursesHandler),
    ('/tests', AddTestsHandler),
    ('/signup', SignUpHandler),
    ], debug=True)

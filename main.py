import webapp2
import os
import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb
from database import seed_data

logout_url = users.create_logout_url('/')
login_url = users.create_login_url('/')

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
            nickname = user.nickname()
            if not existing_user:
                fields = {
                  "nickname": nickname,
                  "logout_url": logout_url,
                }
                self.response.write(new_user_template.render(fields))
            else:
                self.redirect('/addcourses.html')
        else:
            self.response.write(google_login_template.render({ "login_url": login_url  }))


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

class ChatHandler(webapp2.RequestHandler):
    def get(self):
        chatTemplate = jinja_env.get_template(
            "/templates/chat.html")
        self.response.write(chatTemplate.render())

class ViewCourseHandler(webapp2.RequestHandler):
    def get(self):
        userdata_template = jinja_env.get_template("/templates/userdata.html")
        fields = {"names": User.query().filter(User.email == user.email()).get()}
        self.response.write(template.render(fields))

class LoadDataHandler(webapp2.RequestHandler):
    def get(self):
        seed_data()
        self.response.write("Seed data added")

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/login', LogInHandler),
    ('/addcourses', AddCoursesHandler),
    ('/tests', AddTestsHandler),
    ('/signup', SignUpHandler),
    ('/chat', ChatHandler),
    ('/viewcourses', ViewCourseHandler),
    ('/seed-data', LoadDataHandler),
    ], debug=True)

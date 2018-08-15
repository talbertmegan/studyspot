import webapp2
import os
import jinja2
import time
from google.appengine.api import users
from google.appengine.ext import ndb
from database import seed_data
from users import User
from content_manager import populate_feed, logout_url, login_url
from data import Course, Teacher, User, Post

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
                self.redirect('/google_login.html')
        else:
            self.response.write(google_login_template.render({ "login_url": login_url  }))


class AddCoursesHandler(webapp2.RequestHandler):
    def get(self):
        addcourses_template = jinja_env.get_template("/templates/addcourses.html")
        self.response.write(addcourses_template.render())

    def post(self):
        user = users.get_current_user()
        if user is None:
            self.redirect('/')
            return
        current_user = User.query().filter(User.email == user.email()).get()
        if not current_user:
            new_user_entry = User(
                name = self.request.get("name"),
                username = self.request.get("username"),
                email = user.email(),
            )
            new_user_entry.put()
            current_user = new_user_entry
    
        time.sleep(.2)
        self.redirect('/chat?course=' + self.request.get("course"))


class TeacherHandler(webapp2.RequestHandler):
    def get(self):
        teachers = Teacher.query().order(Teacher.name).fetch()
        template = jinja_env.get_template("templates/addcourses.html")
        self.response.write(template.render({'teacher_info' : teachers}))

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
        user = users.get_current_user()
        if user is None:
            self.redirect('/')
            return
        current_user = User.query().filter(User.email == user.email()).get()
        chat_fields = populate_feed(current_user, self.request.get("course"))
        start_chat = jinja_env.get_template("templates/chat.html")
        self.response.write(start_chat.render(chat_fields))

    def post(self):
        user = users.get_current_user()
        if user is None:
            self.redirect('/')
            return
        current_user = User.query().filter(User.email == user.email()).get()
        print(self.request.get("course"))
        new_post = Post(author= current_user.key, board=self.request.get("course"), content= self.request.get("user_post"))
        new_post.put()
        time.sleep(.2)
        self.redirect('/chat?course=' + self.request.get("course"))

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
    ('/teachers', TeacherHandler),
    ], debug=True)

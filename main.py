import webapp2
import os
import jinja2
import json
import datetime
import time
from google.appengine.api import users
from google.appengine.ext import ndb
from database import seed_data
from users import User
from content_manager import populate_feed, logout_url, login_url
from data import Course, Teacher, User, Post, Enrollment


from pprint import pprint, pformat

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def get_auth():

    # Get the Google user
    user = users.get_current_user()
    nickname = None
    if user:
        nickname = user.nickname()
        auth_url = users.create_logout_url('/')
    else:
        auth_url = users.create_login_url('/login')
    return {
        "nickname": nickname,
        "auth_url": auth_url,
        "auth_text": "Sign out" if user else "Sign in"}

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template= jinja_env.get_template("/templates/home.html")

        self.response.write(template.render(get_auth()))

        # self.response.write(template.render())

class LogInHandler(webapp2.RequestHandler):
    def get(self):
        google_login_template = jinja_env.get_template("/templates/google_login.html")
        new_user_template = jinja_env.get_template("/templates/new_user.html")

        user = users.get_current_user()

        if user:
            print("ACCOUNT EXISTS:")
            print(user.email())
            print(user.nickname())


            existing_user = User.query().filter(User.email == user.email()).get()
            nickname = user.nickname()
            if existing_user:
                self.redirect('/addcourses')

            if not existing_user:
                fields = {
                  "nickname": nickname,
                  "logout_url": logout_url,
                }
                self.response.write(new_user_template.render(fields))
            # else:
            #     self.redirect('/layout.html')
        else:
            self.response.write(google_login_template.render({ "login_url": login_url  }))



class AddCoursesHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template("/templates/addcourses.html")

        google_user = users.get_current_user()
        study_spot_user =  User.query().filter(User.email == google_user.email()).get()

        enrollments = Enrollment.query().filter(Enrollment.user == study_spot_user.key).fetch()
        courses = [e.course.get().name for e in enrollments]
        params = get_auth()
        params['courses'] = courses
        self.response.write(template.render(params))


    def post(self):
        # Get the current Google account user
        user = users.get_current_user()
        print(user)
        # If the user doesn't exist, go home
        if user is None:
            self.redirect('/')
            return
        # Fetch the user from the data store
        current_user = User.query().filter(User.email == user.email()).get()

        # If the user doesn't exist in the data store, create and put the new user
        if not current_user:
            new_user_entry = User(
                name = self.request.get("name"),
                username = self.request.get("username"),
                email = user.email(),
            )
            new_user_entry.put()
            current_user = new_user_entry


        time.sleep(.2)
        self.redirect('/addcourses')

class ChatHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user is None:
            self.redirect('/')
            return

        print("user.email(): " + user.email())
        # Get current user from data store
        current_user = User.query().filter(User.email == user.email()).get()

        if current_user is None:
            self.redirect('/')
            return
        print(current_user);

        chat_fields = populate_feed(current_user, self.request.get("course") +" "+ self.request.get("teacher"))
        start_chat = jinja_env.get_template("templates/chat.html")
        self.response.write(start_chat.render(chat_fields))

    def post(self):
        user = users.get_current_user()
        if user is None:
            self.redirect('/')
            return
        current_user = User.query().filter(User.email == user.email()).get()
        print(self.request.get("course"))
        new_post = Post(author= current_user.key, board=self.request.get("course")+" "+self.request.get("teacher"), content= self.request.get("user_post"))
        new_post.put()
        time.sleep(.2)
        self.redirect('/chat?course=' + self.request.get("course")+"&teacher="+self.request.get("teacher"))

class ViewCourseHandler(webapp2.RequestHandler):
    def get(self):
        userdata_template = jinja_env.get_template("/templates/userdata.html")
        fields = {"names": User.query().filter(User.email == user.email()).get()}
        self.response.write(template.render(fields))

class LoadDataHandler(webapp2.RequestHandler):
    def get(self):
        seed_data()
        self.response.write("Seed data added")

class CourseService(webapp2.RequestHandler):

    def get(self):
        key = self.getKey(self.request);
        course_key = ndb.Key('Courses', key)
        courses = Course.query().order(Course.name).fetch()
        teachers = Teacher.query().order(Teacher.name).fetch()

        results = []

        for course in courses:
            result = {}
            teacher_keys = course.teachers
            result['course_id'] = course.key.id()
            result['course_name'] = course.name
            result['teachers'] = []

            for teacher_key in teacher_keys:

                for teacher in teachers:
                    if teacher.key == teacher_key:
                        teacher_dict = {}
                        teacher_dict['teacher_name'] = teacher.name
                        teacher_dict['teacher_id'] = teacher_key.id()
                        result['teachers'].append(teacher_dict)

            results.append(result)

        self.response.headers['Content-Type'] = 'application/json'
        print(json.dumps(results))
        self.response.write(json.dumps(results))

    def post(self):
        key = self.getKey(self.request);
        content = self.request.get('content');
        course = Course(parent=ndb.Key("Courses", key), content=content)
        course.put()

    def getKey(self, request):
        from_user = self.request.get('from');
        to_user = self.request.get('to');
        key_values = [from_user, to_user]
        key_values.sort()
        return key_values[0] + '_' + key_values[1];

    def to_serializable(self, data):
        """Build a new dict so that the data can be JSON serializable"""
        result = data.to_dict()
        record = {}
        # Populate the new dict with JSON serializiable values
        for key in result.iterkeys():
          if isinstance(result[key], datetime.datetime):
            record[key] = result[key].isoformat()
            continue
          record[key] = result[key]
        # Add the key so that we have a reference to the record
        record['key'] = data.key.id()
        return record


""" Teacher Service will allow look up by ID in datastore """
class TeacherService(webapp2.RequestHandler):
    def get(self):
        teacher_id = self.getKey(self.request);
        # course_key = ndb.Key('Courses', key)
        teachers = Teacher.query().order(Teacher.name).fetch()
        # print(teachers)
        results = json.dumps([t.to_dict() for t in teachers], default=str)

        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(results)

    def getKey(self, request):
        field = self.request.get('id');
        id = "";
        print("field: " + field);
        return id;

class UserCourseService(webapp2.RequestHandler):
    def get(self):
        stub='[]'
        print(stub)

    def post(self):
        google_user = users.get_current_user()
        study_spot_user = User.query().filter(User.email == google_user.email()).get()
        course_name = self.request.get("course")
        course = Course.query().filter(Course.name == course_name).get();
        Enrollment(user=study_spot_user.key, course=course.key).put()
        teacher_name = self.request.get("teacher")
        time.sleep(.2)
        self.redirect("/chat?course={}&teacher={}".format(course.name, teacher_name))

        print("/chat?course={}&teacher={}".format(course.name, teacher_name))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/login', LogInHandler),
    ('/addcourses', AddCoursesHandler),
    ('/chat', ChatHandler),
    ('/viewcourses', ViewCourseHandler),
    ('/seed-data', LoadDataHandler),
    ('/course', CourseService),
    ('/teacher', TeacherService),
    ('/user-course', UserCourseService),
    ], debug=True)

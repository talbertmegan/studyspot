from google.appengine.ext import ndb

class User(ndb.Model):
    name = ndb.StringProperty(required=True)
    username = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)

class Post(ndb.Model):
    author = ndb.KeyProperty(User, required=True)
    board = ndb.StringProperty(required=True)
    content = ndb.StringProperty(required=True)
    time = ndb.DateTimeProperty(auto_now_add=True)

class Course(ndb.Model):
    name = ndb.StringProperty()

class Teacher(ndb.Model):
    name = ndb.StringProperty(required=True)
    classes_taught = ndb.KeyProperty(Course, repeated=True)
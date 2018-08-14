from data import Course, Teacher, Users

def seed_data():

    English = Course(name = "English").put()
    Math = Course(name = "Math").put()
    Science = Course(name = "Science").put()
    Social_Studies = Course(name = "SocialStudies").put()

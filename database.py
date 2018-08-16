from data import Course, Teacher, User

def seed_data():



    Lucy_Wilson_key = Teacher(name="Lucy Wilson").put()
    Chuck_Rosenthal_key = Teacher(name="Chuck Rosenthal").put()
    Paul_A_Harris_key = Teacher(name="Paul A. Harris").put()
    Michael_Berg_key = Teacher(name="Michael Berg").put()
    Alissa_Crans_key = Teacher(name="Alissa Crans").put()
    Blake_Mellor_key = Teacher(name="Blake Mellor").put()
    David_Moffet_key = Teacher(name="David Moffet").put()
    Eric_Strauss_key = Teacher(name="Eric Strauss").put()
    John_Dorsey_key = Teacher(name="John Dorsey").put()
    Jennifer_Abe_key = Teacher(name="Jennifer Abe").put()
    Nadia_Y_Kim_key = Teacher(name="Nadia Y. Kim").put()
    Alicia_Partnoy_key = Teacher(name="Alicia Partnoy").put()

    English = Course(name = "English", teachers = [Lucy_Wilson_key, Chuck_Rosenthal_key, Paul_A_Harris_key]).put()
    Math = Course(name = "Math", teachers = [Michael_Berg_key, Alissa_Crans_key, Blake_Mellor_key]).put()
    Science = Course(name = "Science", teachers = [David_Moffet_key, Eric_Strauss_key, John_Dorsey_key]).put()
    Social_Studies = Course(name = "SocialStudies", teachers = [Jennifer_Abe_key, Nadia_Y_Kim_key, Alicia_Partnoy_key]).put()


    User_One = User(name="User One Name", username="UserOne", email="UserOne@example.com", courses=[Math, Science]).put()
    User_Two = User(name="User Two Name", username="UserTwo", email="UserTwo@example.com", courses=[Social_Studies, Science]).put()
    User_Three = User(name="User Three Name", username="UserThree", email="UserThree@example.com", courses=[English, Science]).put()


var courses = {};

document.addEventListener("DOMContentLoaded", function(event) {
  refreshMessages().then(function() {
    courseChanged();
    document.querySelector('#course').addEventListener('change', courseChanged);

  })
});

function courseChanged() {
  const courseSelect = document.querySelector('#course');
  const selectedOption = courseSelect.options[courseSelect.selectedIndex].text;
  console.log(selectedOption);
  console.log(courses);
  course = courses[courseSelect.selectedIndex];
  console.log(course);

  teachers = course.teachers;
  console.log(teachers);

  const teachers_select = document.querySelector('#teacher');

  teachers_select.innerHTML = '';
  teachers.forEach(function(teacher) {
    const option = document.createElement('option');
    option.text = teacher.teacher_name;
    teachers_select.append(option);
  });


}

function sendMessageClicked() {
  postMessage().then(function() {
    refreshMessages();
  })
}


function postMessage() {
  // Call fetch on the chat api.
  const textarea = document.querySelector('#message');
  const message = textarea.value;
  return fetch('./chat?from=213&to=562&content=' + encodeURI(message), {
    method: 'POST'
  }).then(function() {
    textarea.value = '';
  });
}


function refreshMessages() {
  return fetch('./course')
      .then(function(response) {
        return response.json();
      })
      .then(function(messages) {
        console.log(messages);
        courses = messages;
        const courses_select = document.querySelector('#course');
        courses_select.innerHTML = '';
        messages.forEach(function(message) {
          const option = document.createElement('option');
          console.log(message)
          option.text = message.course_name;

          courses_select.append(option);
        });
      });
}

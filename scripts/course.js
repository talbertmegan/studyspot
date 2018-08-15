
var courses = {};

document.addEventListener("DOMContentLoaded", function(event) {
  refreshMessages();
  document.querySelector('#course').addEventListener('change', courseChanged);
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
  fetch('./course')
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
          option.text = message.name;

          courses_select.append(option);
        });
      });
}

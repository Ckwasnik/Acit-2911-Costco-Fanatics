// JavaScript to handle modal
function showModal(name, teacher, credits, dates, cost) {
  document.getElementById('courseName').textContent = name;
  document.getElementById('courseTeacher').textContent = teacher;
  document.getElementById('courseCredits').textContent = credits;
  document.getElementById('courseDates').textContent = dates;
  document.getElementById('courseCost').textContent = cost;
  document.getElementById('courseModal').style.display = "block";
}

function closeModal() {
  document.getElementById('courseModal').style.display = "none";
}

// Close the modal when clicking outside of it
window.onclick = function(event) {
  var modal = document.getElementById('courseModal');
  if (event.target == modal) {
      modal.style.display = "none";
  }
}

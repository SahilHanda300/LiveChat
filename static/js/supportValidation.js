let name = document.querySelector(".name").value;
let email = document.querySelector(".email").value;
let phone = document.querySelector(".phone").value;
let query = document.querySelector(".query").value;
let msgBox = document.querySelector(".formValidate");

function validateSupportForm() {
  if (name == "" || email == "" || phone == "" || query == "") {
    msgBox.textContent = "Kindly Fill in all the fields";
    msgBox.classList.add("py-2");
    return false;
  }
  return true;
}

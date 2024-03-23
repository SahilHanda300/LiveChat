let phone = document.querySelector(".phone");
let name = document.querySelector(".name");
let email = document.querySelector(".email");
let query = document.querySelector(".query");
let submitBtn = document.querySelector(".submitBtn");

function validateSupportForm(){
    if (phone.value=="" || name.value=="" || email.value=="" || query.value=="") {
        return false;
    }
    else{
        return true;
    }
}
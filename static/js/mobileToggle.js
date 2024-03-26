let mobileDiv = document.querySelector(".m-info");
let hamburger = document.querySelector(".hamburger-toggle");
let mobileParent = document.querySelector(".mobile-parent");
hamburger.addEventListener("click", () => {
  mobileParent.classList.toggle("h-20");
  mobileDiv.classList.toggle("translate-x-full");
});

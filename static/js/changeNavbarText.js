let arr = [
  "Where You can stay updated !",
  "Where you can connect to the world !",
  "Where You can make friends ! ",
  "Where You Connect to Several groups",
  "Where you can relax !",
];
let index = 0;
let heading = document.querySelector(".heading span");
let mainText = document.querySelector(".main-text");
setInterval(() => {
  heading.textContent = arr[index];
  index++;
  if (index == arr.length) {
    mainText.textContent = "This is LiveChat";
    index = 0;
  }
}, 2000);

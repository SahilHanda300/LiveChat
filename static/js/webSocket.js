export default function webSocketFunction(
  webSocketParameter,
  user,
  audioParameter
) {
  let ws = new WebSocket(
    `ws://${window.location.host}/ws/sc/${webSocketParameter}/`
  );

  let sendBtn = document.querySelector(".submit");
  let userInp = document.querySelector(".text");

  sendBtn.addEventListener("click", function () {
    if (ws.readyState == WebSocket.OPEN) {
      let val = userInp.value;

      ws.send(
        JSON.stringify({
          msg: val,
          token: user,
        })
      );
    }
  });

  let audio = new Audio();
  audio.src = audioParameter;

  async function audioPlay() {
    try {
      await audio.play();
    } catch (err) {
      console.log("Audio error : ", err);
    }
  }

  ws.onopen = function () {
    audio.preload = "auto";
  };
  ws.onmessage = function (event) {
    let showChat = document.querySelector(".show-chat");
    let msg = JSON.parse(event.data);

    if (msg.msg === userInp.value) {
      if (msg.msg === "" || userInp.value === "") {
        console.log("Cannot Send Empty Messages");
      } else {
        // Create a new chat bubble element
        const newChat = document.createElement("div");
        newChat.className = "flex justify-end";
        newChat.innerHTML = `
      <div class="bg-blue-200 rounded-md float-right mb-5" style="margin-top:4px; margin-right:10px;padding:4px">
        <span class="text-xs float-right">${msg.token} Sent : </span>
        <div class="bg-blue-200 rounded-md clear-both  p-2 w-36  flex justify-end">
              
              <h3 class="">${msg.msg}</h3>
              
              </div>
         </div>     
              `;

        showChat.appendChild(newChat);

        userInp.value = "";
      }
    } else {
      showChat.innerHTML += `
    <div class="bg-blue-200 rounded-md w-52 w-32 clear-both mb-5 " style='margin-top:4px;margin-left:10px;padding:4px'>
      <span class="text-xs float-right">${msg.token} Sent : </span>
      <h3 class="relative top-2">${msg.msg}</h3> <br>
     
    </div>    
    `;
      audioPlay();
    }
  };

  if (performance.navigation.type == 1) {
    window.location.href = `http://${window.location.host}/loggedIndex`;
  }
}

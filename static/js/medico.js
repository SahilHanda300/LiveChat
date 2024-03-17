let ws = new WebSocket(`ws://${window.location.host}/ws/sc/medico/`)
    ws.onopen = function(){
      
    }
    let sendBtn = document.querySelector(".submit")
    let userInp = document.querySelector(".text")
    sendBtn.addEventListener('click',function(){
      let val = userInp.value
      ws.send(JSON.stringify({
        'msg':val
      }))
    })
    ws.onmessage = function(event){
      let showChat = document.querySelector(".show-chat")
      let msg = JSON.parse(event.data)
      showChat.innerHTML+=`
        <div class="bg-blue-100 w-64 mt-5 rounded-lg p-2">
          ${msg.msg}
        </div>
      `
    
    }

   
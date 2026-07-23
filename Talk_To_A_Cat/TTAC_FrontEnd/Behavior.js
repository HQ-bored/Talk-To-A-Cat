const SendButton = document.querySelector('.SendButton');
const TextBox = document.querySelector('.TextBox'); 
const ChatLog = document.querySelector('.ChatLog'); 

// Selects wich url to get the AI.py from
let BASE_URL;
if (window.location.hostname === "localhost" || window.location.hostname === "127.0.0.1") {
    BASE_URL = "http://127.0.0.1:5000"; 
} else {
    BASE_URL = "https://talk-to-a-cat-backend.onrender.com"; 
}

//new
fetch(`${BASE_URL}/start-chat`, { // send this command to AI.py via json
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    }
})
.then(response => { 
    if (!response.ok) { // like the 500 error
        //fail message
        const newMsg = document.createElement('div');
        newMsg.className = 'MyMessage';
        newMsg.innerText = "I can't find the cat... let me look again... \n *error: Chat session initiation failed. Please refresh the page.";
        ChatLog.appendChild(newMsg);
    }
    return response.json(); 
})
.then(data => {
    // Detect your specific 404 message from the python file
    if (data.status === "Chat Session Initiated!") {
        // intro
        const catMsg = document.createElement('div');
        catMsg.className = 'CatMessage'; 
        catMsg.innerText = "hh mMII hH mMMeeooow MmMmeEO hh MmMmEEEooOwWwwHhh MMmiimmmMi MmMMIIIhhH mMIiiaaaAooWwWwm mmMmIIIhHh Miiiih mMmiiAAaooooW mMMmeEewwMmMmi \n (I am a wise cat. I could give you advice... for the right price.)";
        ChatLog.appendChild(catMsg); 

        const newMsg = document.createElement('div');
        newMsg.className = 'MyMessage'; 
        newMsg.innerText = "Well, ig i gotta figure out what this cat is yapping about...";
        ChatLog.appendChild(newMsg);
    }
})
.catch(err => { // Triggers if the backend is entirely offline/unreachable
    /*
    const newMsg = document.createElement('div');
    newMsg.className = 'MyMessage';
    newMsg.innerText = "I can't find the cat... let me look again... \n *error: Backend unreachable or bad Wifi. Please try again later.";
    ChatLog.appendChild(newMsg); 
    The strat-chat does not work yet so im putting this as a temporary band-aid for now*/
    // temp intro
        const catMsg = document.createElement('div');
        catMsg.className = 'CatMessage'; 
        catMsg.innerText = "hh mMII hH mMMeeooow MmMmeEO hh MmMmEEEooOwWwwHhh MMmiimmmMi MmMMIIIhhH mMIiiaaaAooWwWwm mmMmIIIhHh Miiiih mMmiiAAaooooW mMMmeEewwMmMmi \n (I am a wise cat. I could give you advice... for the right price.)";
        ChatLog.appendChild(catMsg);
        
        const newMsg = document.createElement('div');
        newMsg.className = 'MyMessage'; 
        newMsg.innerText = "Well, ig i gotta figure out what this cat is yapping about...";
        ChatLog.appendChild(newMsg);
});
//new end

SendButton.addEventListener('click', function() {
    if (TextBox.value.trim() !== "") { 
        LogMyMessage();
        LogCatMessage(); 
        
        TextBox.value = "";
    } else {
        TextBox.value = "";
    }
});

TextBox.addEventListener('keydown', function(event) { 
    if (event.key === 'Enter') {
        event.preventDefault(); //prevents addind a \n like the default browser behavior
        SendButton.click();
    }
});

function LogMyMessage() {
    const newMsg = document.createElement('div');
    newMsg.className = 'MyMessage';
    newMsg.innerText = TextBox.value;
    ChatLog.appendChild(newMsg);
    // scrolls to bottom of chatlog
    ChatLog.scrollTop = ChatLog.scrollHeight;
}

function LogCatMessage() { 
    fetch(`${BASE_URL}/chat`, { // talks to this url using json
        method: 'POST', 
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: TextBox.value })
    })
    .then(response => response.json()) // convert received response to json
    .then(data => { // when data received
        const catMsg = document.createElement('div');
        catMsg.className = 'CatMessage'; 
        catMsg.innerText = data.reply;
        ChatLog.appendChild(catMsg); 

        ChatLog.scrollTop = ChatLog.scrollHeight;
    });
}
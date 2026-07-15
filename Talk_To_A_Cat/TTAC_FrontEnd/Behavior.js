// Defines these Variables
const SendButton = document.querySelector('.SendButton');
const TextBox = document.querySelector('.TextBox'); 
const ChatLog = document.querySelector('.ChatLog'); 
// When clicked
SendButton.addEventListener('click', function() {
    
    if (TextBox.value.trim() !== "") { // !== means "is not equal to"
        LogMyMessage();
        LogCatMessage(); 
        // Erases TextBox 
        TextBox.value = "";
        
    } else {
        TextBox.value = "";
    }
});

function LogMyMessage() {
    // Creates a new <div> 
    const newMsg = document.createElement('div');
    // Applies MessageBlock CSS rules onto it
    newMsg.className = 'MyMessage';
    // Adds the text from our snapshot
    newMsg.innerText = TextBox.value;
    // Makes it a Child of ChatLog
    ChatLog.appendChild(newMsg);
}

function LogCatMessage() { //requests a reply from the server and logs it to the chat
    fetch('https://Talk-To-A-Cat.onrender.com/chat', { //go to this server
        method: 'POST', // Way of transmition : post the message to the server
        headers: { // lables that tell the server what kind of data is being sent
            'Content-Type': 'application/json' // talk in json language
        },
        body: JSON.stringify({ message: TextBox.value }) // send the message in json format
    })
    .then(response => response.json()) // when response is received and convert it to json
    .then(data => { // when the data is received
        const catMsg = document.createElement('div');// create a new div for the cat's message
        catMsg.className = 'CatMessage'; // use the CatMessage class
        catMsg.innerText = data.reply; // extracts anwser from the data bundle so {"reply": "... --- ..."} -> "... --- ..."
        ChatLog.appendChild(catMsg); // set this div as a child of ChatLog
    });
}
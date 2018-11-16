
var loginPage = document.querySelector('#login-page'),
    usernameInput = document.querySelector('#username'),
    loginButton = document.querySelector('#login'),
    callPage = document.querySelector('#call-page'),
    theirUsernameInput = document.querySelector('#their-username'),
    callButton = document.querySelector('#call'),
    hangUpButton = document.querySelector('#hang-up');

callPage.style.display = "none";

var name,
    connectedUser;
var connection = new WebSocket('wss://192.168.0.35:8888');

connection.onopen = function() {
    console.log("Connected");
};

//Make sure websocket is closed before page is closed
window.onbeforeunload = function() {
    connection.onclose = function () {}; // disable onclose handler first
    connection.close()
};

// Handle all messages through this callback
connection.onmessage = function(message) {
    console.log("Got message", message.data);
    var data = JSON.parse(message.data);
    switch (data.type) {
        case "login":
            onLogin(data.success);
            break;
        case "offer":
            onOffer(data.offer, data.name);
            break;
        case "answer":
            onAnswer(data.answer);
            break;
        case "candidate":
            onCandidate(data.candidate);
            break;
        case "leave":
            onLeave();
            break;
        default:
            break;
    }
};
connection.onerror = function(err) {
    console.log("Got error", err);
};
// Alias for sending messages in JSON format
function send(message) {
    if (connectedUser) {
        message.name = connectedUser;
    }
    connection.send(JSON.stringify(message));
};


// Login when the user clicks the button
loginButton.addEventListener("click", function(event) {
    name = usernameInput.value;
    if (name.length > 0) {
        send({
            type: "login",
            name: name
        });
    }
});

callButton.addEventListener("click", function() {
    var theirUsername = theirUsernameInput.value;
    if (theirUsername.length > 0) {
        startPeerConnection(theirUsername);
    }
});

hangUpButton.addEventListener("click", function() {
    send({
        type: "leave"
    });
    onLeave();
});

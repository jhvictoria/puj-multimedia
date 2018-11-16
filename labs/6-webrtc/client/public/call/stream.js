var yourVideo = document.querySelector('#yours'),
    theirVideo = document.querySelector('#theirs'),
    yourConnection, connectedUser, my_stream;

function startConnection() {
    if (hasUserMedia()) {
        navigator.mediaDevices.getUserMedia({
            video: true,
            audio: false
        }).then(function(stream){
            my_stream = stream;
            yourVideo.src = window.URL.createObjectURL(stream);
            if (hasRTCPeerConnection()) {
                setupPeerConnection(stream);
            } else {
                alert("Sorry, your browser does not support WebRTC.");
            }
        }).catch(function(error) {
            console.log(error);
        });
    } else {
        alert("Sorry, your browser doesn't allow to share the webcam, or you don't have one available");
    }
}

function setupPeerConnection(stream) {
    var configuration = {
        "iceServers": [{
            "url": "stun:stun.1.google.com:19302"
        }]
    };
    yourConnection = new RTCPeerConnection(configuration);
    // Setup stream listening
    yourConnection.addStream(stream);
    yourConnection.onaddstream = function(e) {
        theirVideo.src = window.URL.createObjectURL(e.stream);
    };
    // Setup ice handling
    yourConnection.onicecandidate = function(event) {
        if (event.candidate) {
            send({
                type: "candidate",
                candidate: event.candidate
            });
        }
    };
}

function hasUserMedia() {
    navigator.getUserMedia = navigator.getUserMedia ||
        navigator.webkitGetUserMedia || navigator.mozGetUserMedia ||
        navigator.msGetUserMedia;
    return !!navigator.getUserMedia;
}

function hasRTCPeerConnection() {
    window.RTCPeerConnection = window.RTCPeerConnection ||
        window.webkitRTCPeerConnection || window.mozRTCPeerConnection;
    window.RTCSessionDescription = window.RTCSessionDescription ||
        window.webkitRTCSessionDescription ||
        window.mozRTCSessionDescription;
    window.RTCIceCandidate = window.RTCIceCandidate ||
        window.webkitRTCIceCandidate || window.mozRTCIceCandidate;
    return !!window.RTCPeerConnection;
}

//Starting a Call
function startPeerConnection(user) {
    connectedUser = user;
    // Begin the offer
    yourConnection.createOffer(function(offer) {
        send({
            type: "offer",
            offer: offer
        });
        yourConnection.setLocalDescription(offer);
    }, function(error) {
        alert("An error has occurred.");
    });
};

function onLogin(success) {
    if (success === false) {
        alert("Login unsuccessful, please try a different name.");
    } else {
        loginPage.style.display = "none";
        callPage.style.display = "block";
        // Get the plumbing ready for a call
        startConnection();
    }
};

function onOffer(offer, name) {
    connectedUser = name;
    yourConnection.setRemoteDescription(new RTCSessionDescription(offer));
    yourConnection.createAnswer(function(answer) {
        yourConnection.setLocalDescription(answer);
        send({
            type: "answer",
            answer: answer
        });
    }, function(error) {
        alert("An error has occurred");
    });
};

function onAnswer(answer) {
    yourConnection.setRemoteDescription(new RTCSessionDescription(answer));
};

function onCandidate(candidate) {
    yourConnection.addIceCandidate(new RTCIceCandidate(candidate));
};

function onLeave() {
    yourConnection.removeStream(my_stream);
    connectedUser = null;
    yourConnection.close();
    yourConnection.onicecandidate = null;
    yourConnection.onaddstream = null;
    setupPeerConnection(my_stream);
};

function hasUserMedia() {
    return !!(navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia || navigator.msGetUserMedia);
}

if (hasUserMedia()) {
    navigator.getUserMedia = navigator.getUserMedia ||
        navigator.webkitGetUserMedia ||
        navigator.mozGetUserMedia ||
        navigator.msGetUserMedia;

    /*var constraints = { 
                        video: {
                            mandatory: {
                                minAspectRatio: 1.777,
                                maxAspectRatio: 1.778
                            },
                            optional: [
                                { maxWidth: 640 },
                                { maxHeigth: 480 }
                            ]
                        },
                        audio: false 
                    }
    */

    var constraints = {
        video: {
            mandatory: {
                minWidth: 640,
                minHeight: 480
            }
        },
        audio: true
    };

    if (/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|OperaMini/i.test(navigator.userAgent)) {
        // The user is using a mobile device, lower our minimum resolution
        constraints = {
            video: {
                mandatory: {
                    minWidth: 480,
                    minHeight: 320,
                    maxWidth: 1024,
                    maxHeight: 768
                }
            },
            audio: true
        };
    }

    navigator.mediaDevices.enumerateDevices().then(function(sources) {
        var audioSource = null;
        var videoSource = null;
        for (var i = 0; i < sources.length; ++i) {
            var source = sources[i];
            if (source.kind === "audio") {
                console.log("Microphone found:", source.label, source.id);
                audioSource = source.id;
            } else if (source.kind === "video") {
                console.log("Camera found:", source.label, source.id);
                videoSource = source.id;
            } else {
                console.log("Unknown source found:", source);
            }
        }
        navigator.mediaDevices.getUserMedia(constraints).then(function(stream) {
                var video = document.querySelector('video');
                video.src = window.URL.createObjectURL(stream);
            }).catch(function(error) {
                console.log("Raised an error when capturing:", error);
            });
    });
} else {
    alert("Sorry, your browser does not support getUserMedia.");
}
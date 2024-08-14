document.addEventListener('DOMContentLoaded', function() {
    const talkButton = document.querySelector('.talk');
    const contentH2 = document.querySelector('.content');

    if (talkButton) {
        talkButton.addEventListener('click', () => {
            contentH2.textContent = "Listening...";
            const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
            recognition.lang = 'en-US';
            recognition.interimResults = false;

            recognition.onstart = function() {
                console.log('Voice recognition started.');
            };

            recognition.onresult = function(event) {
                const transcript = event.results[0][0].transcript;
                console.log('Recognized text:', transcript);
                contentH2.textContent = transcript;

                fetch('/start-recognition', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ transcript: transcript })
                }).then(response => response.json()).then(data => {
                    processCommand(data.transcript);
                }).catch(error => {
                    console.error('Error processing recognition:', error);
                });
            };

            recognition.onerror = function(event) {
                console.error('Recognition error:', event.error);
                contentH2.textContent = "Sorry, I didn't catch that. Please try again.";
            };

            recognition.start();
        });
    } else {
        console.error("Microphone button not found.");
    }

    function processCommand(command) {
        fetch('/process', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ command: command })
        }).then(response => response.json()).then(data => {
            if (data.url) {
                window.open(data.url, "_blank");
            } else if (data.response) {
                contentH2.textContent = data.response;
            } else if (data.redirect) {
                window.location.href = data.redirect;
            }
        }).catch(error => {
            console.error("Error processing command:", error);
        });
    }
});

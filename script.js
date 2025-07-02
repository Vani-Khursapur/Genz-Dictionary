function sendMessage() {
    const userInput = document.getElementById('user-input').value.trim(); // Trim whitespace

    if (!userInput) return; // Prevent empty messages

    // Display the user's message in the chat window
    appendMessage(userInput, 'user');

    // Send the input to the backend (API call)
    fetch('/get_response', { // Use a relative URL for the backend endpoint
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ term: userInput })
    })
    .then(response => {
        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        return response.json();
    })
    .then(data => {
        if (data.message) {
            appendMessage(data.message, 'bot'); // Display chatbot's response
        } else {
            appendMessage("Sorry, I don't know that term! 🤷‍♂️", 'bot');
        }
    })
    .catch(error => {
        console.error("Error:", error);
        appendMessage("Oops! Something went wrong. Please try again later. 😥", 'bot');
    });

    // Clear the input box after sending the message
    document.getElementById('user-input').value = '';  // This clears the text box
}

function appendMessage(message, sender) {
    const chatBox = document.getElementById('chat-box');
    const messageDiv = document.createElement('div');
    messageDiv.classList.add(sender);
    messageDiv.textContent = message;
    chatBox.appendChild(messageDiv);

    // Scroll to the bottom of the chat box
    chatBox.scrollTop = chatBox.scrollHeight;
}
function sendMessage() {
    const input = document.getElementById("message");
    const chatBox = document.getElementById("chat");
    const message = input.value.trim();

    // Do nothing if input is empty
    if (message === "") {
        return;
    }

    // Display user message
    chatBox.innerHTML += `<p><strong>You:</strong> ${message}</p>`;

    // Send message to Flask backend
    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: message })
    })
    .then(response => response.json())
    .then(data => {
        // Display bot reply
        chatBox.innerHTML += `<p><strong>Bot:</strong> ${data.reply}</p>`;
        chatBox.scrollTop = chatBox.scrollHeight;
    })
    .catch(error => {
        console.error("Error:", error);
        chatBox.innerHTML += `<p style="color:red;"><strong>Error:</strong> Unable to reach server.</p>`;
    });

    // Clear input box
    input.value = "";
}

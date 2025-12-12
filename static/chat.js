async function sendMessage() {
    let input = document.getElementById("user-input");
    let text = input.value.trim();
    if (!text) return;

    addMessage("You", text);

    const response = await fetch("/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({message: text})
    });

    const data = await response.json();
    addMessage("Bot", data.reply);

    input.value = "";
}

function addMessage(sender, text) {
    let box = document.getElementById("chat-box");
    let msg = document.createElement("p");
    msg.innerHTML = `<strong>${sender}:</strong> ${text}`;
    box.appendChild(msg);
    box.scrollTop = box.scrollHeight;
}

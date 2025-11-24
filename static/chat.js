async function sendMessage() {
  const input = document.getElementById("userInput");
  const text = input.value;

  const response = await fetch("/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: text })
  });

  const data = await response.json();

  const chatbox = document.getElementById("chatbox");
  chatbox.innerHTML += `<p><b>You:</b> ${text}</p>`;
  chatbox.innerHTML += `<p><b>Bot:</b> ${data.reply}</p>`;

  input.value = "";
}

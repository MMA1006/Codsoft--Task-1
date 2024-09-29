document.getElementById("send").addEventListener("click", sendMessage);

document.getElementById("user_input").addEventListener("keypress", function(event) {
    
    if (event.key === "Enter") {
        sendMessage();
    }
});

function sendMessage() {
    const userInput = document.getElementById("user_input").value;

    if (userInput) {
       
        fetch("/ask", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            body: new URLSearchParams({
                "user_input": userInput
            })
        })
        .then(response => response.json())
        .then(data => {
            
            const messagesDiv = document.getElementById("messages");
            messagesDiv.innerHTML += `<div class="message user">User: ${userInput}</div>`;
            
            messagesDiv.innerHTML += `<div class="message chatbot">Chatbot: ${data.response}</div>`;
            document.getElementById("user_input").value = ""; 
            messagesDiv.scrollTop = messagesDiv.scrollHeight; 
        })
        .catch(error => console.error("Error:", error));
    }
}

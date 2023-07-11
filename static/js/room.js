const roomId = JSON.parse(document.getElementById('room-id').textContent);
const chatThread = document.querySelector('#chat-thread');
const messageInput = document.querySelector('#chat-message-input');

const centrifuge = new Centrifuge("ws://" + window.location.host + "/connection/websocket");

centrifuge.on('connect', function (ctx) {
    console.log("connected", ctx);
});

centrifuge.on('disconnect', function (ctx) {
    console.log("disconnected", ctx);
});

const channelName = 'rooms:' + roomId;

let userEmail = "{% if user.is_authenticated %}{{ user.email }}{% endif %}";

const sub = centrifuge.subscribe(channelName, function (ctx) {
    const chatNewThread = document.createElement('li');
    let chatNewMessage;
    if (ctx.data.user === userEmail) {
        chatNewThread.classList.add('current-user');
        chatNewMessage = document.createTextNode(ctx.data.message);
    } else {
        chatNewThread.classList.add('other-user');
        chatNewMessage = document.createTextNode(ctx.data.message);
    }
    chatNewThread.appendChild(chatNewMessage);
    chatThread.appendChild(chatNewThread);
    chatThread.scrollTop = chatThread.scrollHeight;
});

centrifuge.connect();

messageInput.focus();
messageInput.onkeyup = function (e) {
    if (e.keyCode === 13) {
        e.preventDefault();
        const message = messageInput.value;
        if (!message) {
            return;
        }
        sub.publish({ 'message': message, 'user': userEmail });
        messageInput.value = '';
    }
};

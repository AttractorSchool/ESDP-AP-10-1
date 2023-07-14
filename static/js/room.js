import { handleFileUpload } from './fileSharing.js';

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

let userFirstName = document.getElementById('user-first-name') ? document.getElementById('user-first-name').value : '';
let userLastName = document.getElementById('user-last-name') ? document.getElementById('user-last-name').value : '';
let userEmail = document.getElementById('user-email') ? document.getElementById('user-email').value : '';
let userAvatarUrl = document.getElementById('user-avatar-url') ? document.getElementById('user-avatar-url').value : '';

const channelName = 'rooms:' + roomId;
const sub = centrifuge.subscribe(channelName, function (ctx) {
    const chatNewThread = document.createElement('li');
    const chatMessageBody = document.createElement('div');
    chatMessageBody.classList.add('message-body');

    const chatAvatar = document.createElement('div');
    chatAvatar.classList.add('user-avatar');
    chatAvatar.style.backgroundImage = 'url(' + ctx.data.avatarUrl + ')';

    const chatUserName = document.createElement('div');
    chatUserName.classList.add('user-name');
    chatUserName.innerText = ctx.data.userFirstName + ' ' + ctx.data.userLastName;

    const chatTimestamp = document.createElement('div');
    chatTimestamp.classList.add('timestamp');
    chatTimestamp.innerText = new Date(ctx.data.timestamp).toLocaleString();

    const chatMessageContent = document.createElement('div');
    chatMessageContent.classList.add('message-content');

    if (ctx.data.fileMessage) {
        const chatFileLink = document.createElement('a');
        chatFileLink.href = ctx.data.fileUrl;
        chatFileLink.target = '_blank';
        chatFileLink.textContent = ctx.data.message;
        chatMessageContent.appendChild(chatFileLink);
    } else {
        const chatNewMessage = document.createTextNode(ctx.data.message);
        chatMessageContent.appendChild(chatNewMessage);
    }

    chatMessageBody.appendChild(chatUserName);
    chatMessageBody.appendChild(chatMessageContent);
    chatMessageBody.appendChild(chatTimestamp);
    chatNewThread.appendChild(chatAvatar);
    chatNewThread.appendChild(chatMessageBody);

    if (ctx.data.user === userEmail) {
        chatNewThread.classList.add('current-user');
    } else {
        chatNewThread.classList.add('other-user');
    }

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

        sub.publish({
            'message': message,
            'user': userEmail,
            'timestamp': new Date().toISOString(),
            'userFirstName': userFirstName,
            'userLastName': userLastName,
            'avatarUrl': userAvatarUrl
        });

        messageInput.value = '';
    }
};

const fileInput = document.querySelector('#chat-file-input');

handleFileUpload(fileInput, centrifuge, roomId, userEmail, userFirstName, userLastName, userAvatarUrl);

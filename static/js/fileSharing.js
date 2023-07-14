function handleFileUpload(fileInput, centrifuge, roomId, userEmail, userFirstName, userLastName, userAvatarUrl) {
    fileInput.onchange = async function(e) {
        e.preventDefault();
        const file = fileInput.files[0];
        if (!file) {
            return;
        }

        const formData = new FormData();
        formData.append('file', file);

        const response = await fetch(`/chat/chatfiles/${roomId}/`, {
            method: 'POST',
            body: formData
        });


        if (!response.ok) {
            alert('File upload failed');
            return;
        }

        const data = await response.json();

        const message = {
            'message': data.file_url,
            'user': userEmail,
            'timestamp': new Date().toISOString(),
            'userFirstName': userFirstName,
            'userLastName': userLastName,
            'avatarUrl': userAvatarUrl
        };

        const channelName = 'rooms:' + roomId;
        centrifuge.publish(channelName, message);
    };
}

export { handleFileUpload };

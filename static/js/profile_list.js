$.ajax({
    url: 'http://127.0.0.1:8000/api/accounts/',
    method: 'GET',
    success: function(data, status) {
        const profile = document.getElementById('profile_list');
        for (let i = 0; i < data.length; i++) {
            const profileBlock = document.createElement('div');
            const profileName = document.createElement('p');
            const profileNameLink = document.createElement('a');
            profileNameLink.innerText = data[i].first_name
            profileName.append(profileNameLink)
            const profileLastName = document.createElement('p');
            profileLastName.innerText = data[i].last_name
            const profileCity = document.createElement('p');
            profileCity.innerText = data[i].cities.citi_name
            profileBlock.append(profileName, profileLastName, profileCity)
            profile.append(profileBlock)

            const profileAvatar = document.createElement('img');
            profileAvatar.className = 'avatar'
            profileAvatar.src = `${data[i].avatar.image}`
            profileBlock.append(profileAvatar)
            profileBlock.className = 'profile_str'
        }
    },
    error: function(response, status) {
    }
});
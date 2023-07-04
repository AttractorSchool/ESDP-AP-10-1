const currentUrl = window.location.pathname;
console.log(currentUrl);
listUsrl = currentUrl.split('/')


$.ajax({
    url: 'http://127.0.0.1:8000/api/cities/',
    method: 'GET',
    success: function(data, status) {
        const eventSelect = document.getElementById('id_cities')
        for (let i = 0; i < data.length; i++) {
            const eventOption = document.createElement('option');
            eventOption.innerHTML = data[i].citi_name
            eventOption.value = data[i].id
            eventSelect.append(eventOption) 
        }
    },
});


$.ajax({
    url: 'http://127.0.0.1:8000/api/accounts/',
    method: 'GET',
    success: function(data, status) {
        const eventSelect = document.getElementById('id_user')
        for (let i = 0; i < data.length; i++) {
            const eventOption = document.createElement('option');
            eventOption.innerHTML = data[i].email
            eventOption.value = data[i].id
            eventSelect.append(eventOption) 
        }
    },
});



$.ajax({
    url: `http://127.0.0.1:8000/api/events/${listUsrl.at(-1)}`,
    method: 'GET',
    success: function(data, status) {
        let name = document.getElementById("id_name")
        let description = document.getElementById("id_description")
        let cities = document.getElementById("id_cities")
        let user = document.getElementById("id_user")
        let photo = document.getElementById("id_photo")
        name.value = data.name
        cities.value = data.cities.citi_name
        user.value = data.sponsor
        description.value = data.description
        photo.value = data.photo
        }
});

let divide = function(){
    const name = document.getElementById("id_name").value
    const description = document.getElementById("id_description").value
    const cities = document.getElementById("id_cities").value
    const user = document.getElementById("id_user").value
    const photo = document.getElementById("id_photo").value
   let xhr = new XMLHttpRequest();
   xhr.onload = function(){
       let data = JSON.parse(this.response);
       console.log(data)
       window.location.href = `http://127.0.0.1:8000/news/${data.id}`;
       };
       
   xhr.open('PUT', `http://127.0.0.1:8000/api/news/${listUsrl.at(-1)}`);
   send = {
    "name": name,
    "cities": cities,
    "user": user,
    "description": description,
    "photo": photo
   }
   xhr.send(JSON.stringify(send))
   
}


const create_id = document.getElementById('create_id')

create_id.addEventListener('click', divide)

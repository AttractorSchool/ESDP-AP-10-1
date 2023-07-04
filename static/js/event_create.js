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
    url: 'http://127.0.0.1:8000/api/type_events/',
    method: 'GET',
    success: function(data, status) {
        const eventSelect = document.getElementById('id_type_events')
        for (let i = 0; i < data.length; i++) {
            const eventOption = document.createElement('option');
            eventOption.innerHTML = data[i].events_name
            eventOption.value = data[i].id
            eventSelect.append(eventOption) 
        }
    },
});
$.ajax({
    url: 'http://127.0.0.1:8000/api/accounts/',
    method: 'GET',
    success: function(data, status) {
        const eventSelect = document.getElementById('id_sponsor')
        for (let i = 0; i < data.length; i++) {
            const eventOption = document.createElement('option');
            eventOption.innerHTML = data[i].email
            eventOption.value = data[i].id
            eventSelect.append(eventOption) 
        }
    },
});


let divide = function(){
    const name = document.getElementById("id_name").value
    const events_at = document.getElementById("events_at").value
    const number_of_seats = document.getElementById("id_number_of_seats").value
    const start_register_at = document.getElementById("start_register_at").value
    const end_register_at = document.getElementById("end_register_at").value
    const description = document.getElementById("id_description").value
    const place = document.getElementById("id_place").value
    const price = document.getElementById("id_price").value
    const cities = document.getElementById("id_cities").value
    const type_events = document.getElementById("id_type_events").value
    const sponsor = document.getElementById("id_sponsor").value
    const photo = document.getElementById("id_photo").value
   let xhr = new XMLHttpRequest();
   xhr.onload = function(){
       let data = JSON.parse(this.response);
       console.log(data)
       window.location.href = `http://127.0.0.1:8000/events/${data.id}`;
       };
       
   xhr.open('POST', "http://127.0.0.1:8000/api/events/");
   send = {
       "name": name,
       "cities": cities,
       "type_events": type_events,
       "events_at": events_at,
       "sponsor": sponsor,
       "number_of_seats": number_of_seats,
       "start_register_at": start_register_at,
       "end_register_at": end_register_at,
       "description": description,
       "place": place,
       "price": price,
       "photo": photo
   }
   xhr.send(JSON.stringify(send))
   
}


const create_id = document.getElementById('create_id')

create_id.addEventListener('click', divide)




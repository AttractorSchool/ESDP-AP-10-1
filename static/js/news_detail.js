const currentUrl = window.location.pathname;
console.log(currentUrl);
listUsrl = currentUrl.split('/')

$.ajax({
    url: `http://127.0.0.1:8000/api/news/${listUsrl.at(-1)}`,
    method: 'GET',
    success: function(data, status) {
        const eventDiv = document.getElementById('events')
        const updateId = document.getElementById('update_id')
        const deleteId = document.querySelectorAll('.btn-success')
        deleteId.id = data.id
        updateId.value = data.id
            const eventsAvatar = document.createElement('img');
            eventsAvatar.className = 'photo'
            eventsAvatar.src = `${data.photo.image}`
            eventDiv.append(eventsAvatar)
            const eventsName = document.createElement('p');
            eventsName.innerText = data.name
            eventDiv.append(eventsName)
            const eventsCities = document.createElement('p');
            eventsCities.innerText = data.cities.citi_name
            eventDiv.append(eventsCities)
            const sponsor = document.createElement('p');
            sponsor.innerText = data.user
            eventDiv.append(sponsor)
            const description = document.createElement('p');
            description.innerText = data.description
            eventDiv.append(description)
        }
});
const updateId = document.getElementById('update_id')
document.getElementById('update_id').onclick = function() {
    window.location.href = `http://127.0.0.1:8000/update_news/${updateId.value}`;
  };


  let divide = function(){
   let xhr = new XMLHttpRequest();
   xhr.onload = function(){
       let data = JSON.parse(this.response);
       console.log(data)
       };

   xhr.open('DELETE', `http://127.0.0.1:8000/api/news/${listUsrl.at(-1)}`);

   xhr.send()

}


const deleteId = document.getElementById('delete')

deleteId.addEventListener('click', divide)


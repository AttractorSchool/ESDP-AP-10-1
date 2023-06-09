$.ajax({
    url: 'http://127.0.0.1:8000/api/newsline/',
    method: 'GET',
    success: function(data, status) {
        const newsline = document.getElementById('newsline');
        for (let i = 0; i < data.length; i++) {
            const newsBlock = document.createElement('div');
            const newsName = document.createElement('p');
            const newsNameLink = document.createElement('a');
            newsNameLink.innerText = data[i].name
            newsName.append(newsNameLink)
            const newsDescription = document.createElement('p');
            newsDescription.innerText = data[i].description
            const newsCreatedAt = document.createElement('p');
            newsCreatedAt.innerText = data[i].created_at
            newsBlock.append(newsName, newsDescription, newsCreatedAt)
            newsline.append(newsBlock)
            if (!data[i].type_events){
                const newsPhoto = document.createElement('div');
                newsPhoto.className = 'images'
                for (let j = 0; j < data[i].photo.length; j++){
                    const newsImage = document.createElement('img');
                    newsImage.src = `${data[i].photo[j].image}`
                    newsPhoto.append(newsImage)
                    newsBlock.append(newsPhoto)
                }
            }
            else {
                const newsPhoto = document.createElement('img');
                newsPhoto.className = 'image'
                newsPhoto.src = `${data[i].photo}`
                newsBlock.append(newsPhoto)
            }
            newsBlock.className = 'news'
            newsDescription.className = 'news_description'
        }
    },
    error: function(response, status) {
    }
});
$.ajax({
    url: 'http://127.0.0.1:8000/api/newsline/',
    method: 'GET',
    success: function(data, status) {
    const newsline = document.getElementById('newsline');

    for (let i = 0; i < data.length; i++) {
      const newsBlock = document.createElement('div');
      const articleWrapper = document.createElement('div');
      articleWrapper.className = 'article-wrapper';

      const figure = document.createElement('figure');
      const newsPhoto = document.createElement('img');
      newsPhoto.src = data[i].photo;
      newsPhoto.alt = '';
      figure.appendChild(newsPhoto);
      articleWrapper.appendChild(figure);

      const articleBody = document.createElement('div');
      articleBody.className = 'article-body';

      const newsTitle = document.createElement('h2');
      newsTitle.innerText = data[i].name;
      articleBody.appendChild(newsTitle);

      const newsDescription = document.createElement('p');
      newsDescription.innerText = data[i].description;
      articleBody.appendChild(newsDescription);

      articleWrapper.appendChild(articleBody);
      newsBlock.appendChild(articleWrapper);

      newsBlock.className = 'news';
      newsDescription.className = 'news_description';

      newsline.appendChild(newsBlock);
    }
  },
    error: function (response, status) {
    }
});
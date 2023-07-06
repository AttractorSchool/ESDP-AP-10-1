document.addEventListener('DOMContentLoaded', function () {
    const dates = document.getElementsByClassName('date');

    for (let i = 0; i < dates.length; i++) {
        dates[i].addEventListener('click', function () {
            const eventList = this.nextElementSibling;
            const eventCount = this.parentNode.querySelector('.event-count');

            if (window.getComputedStyle(eventList).display === 'none') {
                eventList.style.display = 'block';
                eventCount.style.display = 'none';
            } else {
                eventList.style.display = 'none';
                eventCount.style.display = 'inline';
            }
        });
    }
});
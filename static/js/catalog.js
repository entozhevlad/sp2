document.querySelector('.category-toggle').addEventListener('click', function() {
    document.querySelector('.category-list').classList.toggle('show');
    document.querySelector('.overlay').classList.toggle('show');
});

document.querySelector('.overlay').addEventListener('click', function() {
    document.querySelector('.category-list').classList.toggle('show');
    document.querySelector('.overlay').classList.toggle('show');
});
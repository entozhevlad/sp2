window.addEventListener("DOMContentLoaded", (event) => {
    document.querySelector('.burger').addEventListener('click', function () {
        this.classList.toggle('active');
        document.querySelector('.navbar').classList.toggle('open');
    })
});
document.querySelector('.category-toggle').addEventListener('click', function() {
    document.querySelector('.category-list').classList.toggle('show');
});

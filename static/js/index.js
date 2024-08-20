window.addEventListener("DOMContentLoaded", (event) => {
    document.querySelector('.burger').addEventListener('click', function () {
        this.classList.toggle('active');
        document.querySelector('.navbar').classList.toggle('open');
    })
});

document.addEventListener("DOMContentLoaded", function () {
    $('.autoplay_news').slick({
        infinite: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        autoplay: true,
        autoplaySpeed: 5000,
        lazyLoad: 'progressive',
    });

    $('.autoplay').slick({
        dots: true,
        infinite: true,
        speed: 1000,
        arrows: false,
        autoplay: true,
        slidesToShow: 6,
        slidesToScroll: 1,
        focusOnSelect: true,
        lazyLoad: 'ondemand',
        responsive: [
            {
                breakpoint: 2520,
                settings: {
                    slidesToShow: 6,
                    slidesToScroll: 1,
                }
            },
            {
                breakpoint: 2160,
                settings: {
                    slidesToShow: 5,
                    slidesToScroll: 1,
                }
            },
            {
                breakpoint: 1800,
                settings: {
                    slidesToShow: 4,
                    slidesToScroll: 1,
                }
            },
            {
                breakpoint: 1440,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 1,
                }
            },
            {
                breakpoint: 1080,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 1,
                }
            },
            {
                breakpoint: 720,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1,
                    variableWidth: false, // Отключаем variableWidth для мобильных устройств
                }
            },
        ]
    });
});
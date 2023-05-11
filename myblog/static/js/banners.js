var banners = document.querySelectorAll('.banner');
var currentBanner = 0;

function changeBanner() {
    banners[currentBanner].classList.remove('active');
    currentBanner = (currentBanner + 1) % banners.length;
    banners[currentBanner].classList.add('active');
}
setInterval(changeBanner, 3000);
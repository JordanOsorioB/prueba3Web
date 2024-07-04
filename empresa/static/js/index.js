
function scrollToTop() {
window.scrollTo({
   top: 0,
   behavior: 'smooth'
});
}

window.onscroll = function() {
   const button = document.querySelector('.scroll-to-top');
   if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
       button.style.display = 'flex';
   } else {
       button.style.display = 'none';
   }
};

window.addEventListener('DOMContentLoaded', () => {



  const navbar = document.querySelector('nav')



  window.addEventListener('scroll', () => {

    const scroll = window.scrollY



    scroll >= '125' ? navbar.classList.add('activeNav') : navbar.classList.remove('activeNav')

  })



})

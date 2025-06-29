// assets/js/main.js

document.addEventListener('DOMContentLoaded', () => {

  // --- 1. THEME SWITCHER ---
  const themeSwitcher = document.getElementById('theme-switcher');
  const html = document.documentElement;

  // Set theme on initial load
  const currentTheme = localStorage.getItem('theme') || 'light';
  html.setAttribute('data-theme', currentTheme);
  
  themeSwitcher.addEventListener('click', () => {
    let newTheme = html.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
    html.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
  });

  // --- 2. HAMBURGER MENU ---
  const hamburger = document.getElementById('hamburger-menu');
  const navMenu = document.getElementById('nav-menu');

  hamburger.addEventListener('click', () => {
    navMenu.classList.toggle('nav-open');
    hamburger.classList.toggle('is-active');
  });

  // --- 3. 3D TILT EFFECT ON CARDS ---
  const cards = document.querySelectorAll('.item-card');

  cards.forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left; // x position within the element.
      const y = e.clientY - rect.top;  // y position within the element.

      const centerX = rect.width / 2;
      const centerY = rect.height / 2;

      const rotateX = ((y - centerY) / centerY) * -5; // Max 5deg rotation
      const rotateY = ((x - centerX) / centerX) * 5;  // Max 5deg rotation

      card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
    });

    card.addEventListener('mouseleave', () => {
      card.style.transform = 'perspective(1000px) rotateX(0) rotateY(0)'; // Reset
    });
  });

  // --- 4. BLOG SEARCH FUNCTIONALITY ---
  const searchInput = document.getElementById('search-input');
  const postList = document.getElementById('post-list');
  if (searchInput && postList) {
    searchInput.addEventListener('input', function () {
      const query = this.value.toLowerCase();
      const posts = postList.querySelectorAll('.post-item');
      posts.forEach(post => {
        const title = post.getAttribute('data-title').toLowerCase();
        const content = post.getAttribute('data-content').toLowerCase();
        if (title.includes(query) || content.includes(query)) {
          post.style.display = '';
        } else {
          post.style.display = 'none';
        }
      });
    });
  }

});


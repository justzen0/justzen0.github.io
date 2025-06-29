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

  // assets/js/main.js, inside the DOMContentLoaded listener

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

});


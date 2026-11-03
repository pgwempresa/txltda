const toggle = document.querySelector('.menu-toggle');
const nav = document.querySelector('#navigation');
toggle?.addEventListener('click', () => {
  const open = toggle.getAttribute('aria-expanded') !== 'true';
  toggle.setAttribute('aria-expanded', String(open));
  nav.classList.toggle('open', open);
});
nav?.querySelectorAll('a').forEach(a => a.addEventListener('click', () => {
  toggle.setAttribute('aria-expanded', 'false');
  nav.classList.remove('open');
}));
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && nav?.classList.contains('open')) {
    toggle.setAttribute('aria-expanded', 'false'); nav.classList.remove('open'); toggle.focus();
  }
});

// Animate only as an enhancement: HTML remains visible if JS is unavailable.
const motionPreference = window.matchMedia('(prefers-reduced-motion: reduce)');
const entranceAnimations = new Set();
let entranceObserver;
const finishMotion = () => {
  entranceObserver?.disconnect();
  entranceAnimations.forEach(animation => animation.cancel());
  entranceAnimations.clear();
};
if (!motionPreference.matches && 'IntersectionObserver' in window && Element.prototype.animate) {
  const targets = document.querySelectorAll('.hero > div:first-child > *, .section-head, .card, .purpose > div:first-child, .purpose-list article, .company > div, .data > div, .contact > div:first-child, .contact-row');
  entranceObserver = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      entranceObserver.unobserve(entry.target);
      if (motionPreference.matches || entry.target.contains(document.activeElement)) return;
      const siblings = Array.from(entry.target.parentElement.children);
      const order = Math.min(siblings.indexOf(entry.target), 3);
      const animation = entry.target.animate([
        { opacity: 0, transform: 'translateY(18px)' },
        { opacity: 1, transform: 'translateY(0)' }
      ], { duration: 650, delay: order * 65, easing: 'cubic-bezier(.22,1,.36,1)', fill: 'backwards' });
      entranceAnimations.add(animation);
      animation.onfinish = () => entranceAnimations.delete(animation);
    });
  }, { threshold: 0.08 });
  targets.forEach(target => entranceObserver.observe(target));
}
motionPreference.addEventListener('change', event => {
  if (event.matches) finishMotion();
});
// Keyboard users never have to wait for a link to finish entering.
document.addEventListener('focusin', event => {
  entranceAnimations.forEach(animation => {
    if (animation.effect?.target?.contains(event.target)) {
      animation.cancel();
      entranceAnimations.delete(animation);
    }
  });
});

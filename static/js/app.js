const toggleScrollBtn = document.getElementById('toggleScrollBtn');

toggleScrollBtn.addEventListener('click', () => {
  if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight) {
    window.scrollTo({ top: 0, behavior: 'smooth' });
    toggleScrollBtn.innerHTML = '▼';
  } else {
    window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });
    toggleScrollBtn.innerHTML = '▲';
  }
});

window.addEventListener('scroll', () => {
  if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight) {
    toggleScrollBtn.innerHTML = '▲';
  } else {
    toggleScrollBtn.innerHTML = '▼';
  }
});


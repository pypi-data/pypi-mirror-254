(props, cc, { el, onMount }) => {
  onMount(() => {
    if (!document.getElementById('alpine')) {
      const script = document.createElement('script');
      script.id = 'alpine';
      script.src = 'https://unpkg.com/alpinejs@3.13.3/dist/cdn.min.js';
      document.body.appendChild(script);
    }
    el.innerHTML = `
    <div x-data="{ open: false }">
      <button @click="open = !open">Expand</button>
      <span x-show="open">
          Content...
      </span>
    </div>
    `;
  });
};

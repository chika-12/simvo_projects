const quoteId = 'quote';
const authorId = 'author';
const card = document.getElementById('random-quote-generator');

const rand = (min, max) => Math.floor(Math.random() * (max - min + 1)) + min;

async function randomQuote() {
  const res = await fetch('https://dummyjson.com/quotes/random');
  if (!res.ok) throw new Error(`HTTP ${res.status}`);

  const data = await res.json();
  
  const h1 = rand(0, 360);
  const h2 = (h1 + rand(70, 170)) % 360;
  const angle = rand(0, 360);
  const saturation = rand(70, 90);
  const light1 = rand(42, 58);
  const light2 = rand(38, 56);

  card.style.background = `linear-gradient(${angle}deg, hsl(${h1}, ${saturation}%, ${light1}%), hsl(${h2}, ${saturation}%, ${light2}%))`;

  document.getElementById(quoteId).textContent = data.quote;
  document.getElementById(authorId).textContent = data.author;
}

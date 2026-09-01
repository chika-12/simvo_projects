# Craps Casino Game

A browser-based dice betting game built with vanilla HTML, CSS, and JavaScript — no frameworks, no build step. Part of a larger portfolio project, styled to match its dark, colorful design system.

## How it works

**1. Register a username**
Enter a username to start playing. It must:

- Be at least 5 characters long
- Not begin with a number
- Contain only letters, numbers, and underscores (no spaces or special characters)

**2. Place your bet**

- You start with $1000
- Minimum bet is $100
- Use the `+` / `−` controls to adjust your bet amount up or down in $100 increments, up to your remaining balance

**3. Choose Even or Odd**
Pick a side before rolling — your selection is highlighted so you always know what's active.

**4. Roll the dice**
Hit "Roll dice" to play the round. Your balance, bet amount, and round counter update as you play.

## Tech stack

- **HTML** — game structure and layout
- **CSS** — custom-property-driven theming (shared design tokens with the portfolio site: colors, fonts, spacing)
- **JavaScript** — vanilla DOM manipulation, no external libraries or dependencies

## Project structure

```
crapscasino/
├── craps.css     # game-specific styles
└── index.js      # game logic (registration, betting, state)
```

Loaded alongside the main portfolio's `style.css` and `script.js` via `index.html`.

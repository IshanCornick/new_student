---
toc: true
comments: true
layout: hack
title: Match the image!
description: Match the image to the same one to win!
type: hacks
courses: { compsci: {week: 8} }
---

<html>
<head>
    <title>Frog Memory Match Game</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .memory-game {
            display: grid;
            grid-template-columns: repeat(4, 100px);
            grid-gap: 10px;
        }

        .memory-card {
            width: 100px;
            height: 100px;
            background-color: #2196F3;
            display: flex;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            user-select: none;
        }

        .matched {
            background-color: #4CAF50;
            pointer-events: none;
        }
    </style>
</head>
<body>
    <div class="memory-game" id="memory-game"></div>

    <script>
        const memoryGame = document.getElementById("memory-game");
        const frogs = [
            '🐸', '🐸', '🐢', '🐢', '🐍', '🐍', '🐊', '🐊',
            '🦎', '🦎', '🦖', '🦖', '🦗', '🦗', '🐛', '🐛'
        ];
        const shuffledFrogs = frogs.sort(() => 0.5 - Math.random());
        let firstCard = null;
        let secondCard = null;
        let canFlip = true;

        function createCard(frog) {
            const card = document.createElement('div');
            card.classList.add('memory-card');
            card.textContent = frog;
            card.addEventListener('click', flipCard);
            memoryGame.appendChild(card);
        }

        function flipCard() {
            if (!canFlip) return;
            if (!firstCard) {
                firstCard = this;
                firstCard.classList.add('matched');
                return;
            }
            if (this === firstCard) return;
            secondCard = this;
            secondCard.classList.add('matched');
            canFlip = false;

            setTimeout(checkForMatch, 1000);
        }

        function checkForMatch() {
            if (firstCard.textContent === secondCard.textContent) {
                firstCard.removeEventListener('click', flipCard);
                secondCard.removeEventListener('click', flipCard);
            } else {
                firstCard.classList.remove('matched');
                secondCard.classList.remove('matched');
            }

            firstCard = null;
            secondCard = null;
            canFlip = true;

            if (document.querySelectorAll('.memory-card.matched').length === frogs.length) {
                alert('Congratulations! You matched all the frogs!');
            }
        }

        shuffledFrogs.forEach(createCard);
    </script>
</body>
</html>

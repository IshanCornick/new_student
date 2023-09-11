---
toc: true
comments: false
layout: post
title: Mine Sweeper
description: Mine Sweeper made with chat gpt
type: hacks
courses: { compsci: {week: 3} }
---

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Minesweeper</title>
    <style>
        .board {
            display: grid;
            grid-template-columns: repeat(8, 30px);
            gap: 2px;
        }
        .cell {
            width: 30px;
            height: 30px;
            text-align: center;
            border: 1px solid #ccc;
            background-color: #eee;
            cursor: pointer;
        }
        .cell.revealed {
            background-color: #ddd;
            cursor: default;
        }
        .cell.mine {
            background-color: #f00;
        }
    </style>
</head>
<body>
    <div class="board"></div>
    <script>
        const board = document.querySelector('.board');
        let cells = [];
        function createBoard() {
            for (let i = 0; i < 64; i++) {
                const cell = document.createElement('div');
                cell.classList.add('cell');
                cell.dataset.index = i;
                cell.addEventListener('click', handleClick);
                board.appendChild(cell);
                cells.push(cell);
            }
        }
        function placeMines() {
            const mineCount = 10;
            for (let i = 0; i < mineCount; i++) {
                let randomIndex;
                do {
                    randomIndex = Math.floor(Math.random() * 64);
                } while (cells[randomIndex].classList.contains('mine'));
                cells[randomIndex].classList.add('mine');
            }
        }
        function handleClick(event) {
            const cell = event.target;
            if (cell.classList.contains('revealed') || cell.classList.contains('mine')) return;
            cell.classList.add('revealed');
            const index = parseInt(cell.dataset.index);
            const adjacentMines = getAdjacentMines(index);
            if (adjacentMines > 0) {
                cell.textContent = adjacentMines;
            }
            if (adjacentMines === 0) {
                revealAdjacentCells(index);
            }
        }
        function getAdjacentMines(index) {
            const adjacentIndices = [-9, -8, -7, -1, 1, 7, 8, 9];
            let count = 0;
            for (const offset of adjacentIndices) {
                const adjacentIndex = index + offset;
                if (cells[adjacentIndex] && cells[adjacentIndex].classList.contains('mine')) {
                    count++;
                }
            }
            return count;
        }
        function revealAdjacentCells(index) {
            const adjacentIndices = [-9, -8, -7, -1, 1, 7, 8, 9];
            for (const offset of adjacentIndices) {
                const adjacentIndex = index + offset;
                const adjacentCell = cells[adjacentIndex];
                if (adjacentCell && !adjacentCell.classList.contains('revealed')) {
                    handleClick({ target: adjacentCell });
                }
            }
        }
        createBoard();
        placeMines();
    </script>
</body>
</html>
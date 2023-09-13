---
toc: true
comments: false
layout: post
title: Driving
description: Basic driving game that makes new blocks for a drive to go through them.
type: hacks
courses: { compsci: {week: 3} }
---


<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Improved Driving Game</title>
    <style>
        body {
            margin: 0;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
            background-color: #333;
        }

        canvas {
            background-color: #333;
        }

        #gameOverScreen {
            display: none;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background-color: rgba(0, 0, 0, 0.7);
            color: white;
            padding: 20px;
            text-align: center;
        }

        #pauseButton {
            position: absolute;
            top: 10px;
            right: 10px;
            background-color: #333;
            color: white;
            border: none;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <canvas id="gameCanvas" width="800" height="400"></canvas>
    <button id="pauseButton">Pause</button>
    <div id="gameOverScreen">
        <h1>Game Over!</h1>
        <p>Your Score: <span id="scoreDisplay">0</span></p>
        <button id="restartButton">Restart</button>
    </div>
    <script>
        const canvas = document.getElementById('gameCanvas');
        const ctx = canvas.getContext('2d');

        const carWidth = 50;
        const carHeight = 30;
        const carSpeed = 5;
        const obstacleWidth = 20;
        const obstacleHeight = 20;
        const obstacleSpeed = 3;

        let carX = (canvas.width - carWidth) / 2;
        let carY = canvas.height - carHeight - 20;

        let leftPressed = false;
        let rightPressed = false;

        let obstacles = [];
        let score = 0;
        let isGameOver = false;
        let isPaused = false;

        const pauseButton = document.getElementById('pauseButton');
        const gameOverScreen = document.getElementById('gameOverScreen');
        const restartButton = document.getElementById('restartButton');
        const scoreDisplay = document.getElementById('scoreDisplay');

        document.addEventListener('keydown', (e) => {
            if (!isGameOver && !isPaused) {
                if (e.key === 'ArrowLeft') {
                    leftPressed = true;
                } else if (e.key === 'ArrowRight') {
                    rightPressed = true;
                }
            }
        });

        document.addEventListener('keyup', (e) => {
            if (!isGameOver && !isPaused) {
                if (e.key === 'ArrowLeft') {
                    leftPressed = false;
                } else if (e.key === 'ArrowRight') {
                    rightPressed = false;
                }
            }
        });

        pauseButton.addEventListener('click', () => {
            if (isPaused) {
                isPaused = false;
                pauseButton.textContent = 'Pause';
                requestAnimationFrame(draw);
            } else {
                isPaused = true;
                pauseButton.textContent = 'Resume';
            }
        });

        restartButton.addEventListener('click', () => {
            restartGame();
            requestAnimationFrame(draw);
        });

        function drawCar() {
            ctx.fillStyle = 'blue';
            ctx.fillRect(carX, carY, carWidth, carHeight);
        }

        function drawObstacles() {
            ctx.fillStyle = 'red';
            obstacles.forEach((obstacle) => {
                ctx.fillRect(obstacle.x, obstacle.y, obstacleWidth, obstacleHeight);
            });
        }

        function clearCanvas() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
        }

        function updateCarPosition() {
            if (leftPressed && carX > 0) {
                carX -= carSpeed;
            }
            if (rightPressed && carX + carWidth < canvas.width) {
                carX += carSpeed;
            }
        }

        function updateObstacles() {
            for (let i = obstacles.length - 1; i >= 0; i--) {
                obstacles[i].y += obstacleSpeed;

                if (obstacles[i].y > canvas.height) {
                    obstacles.splice(i, 1);
                    score++;
                }

                if (
                    obstacles[i].y + obstacleHeight >= carY &&
                    obstacles[i].x >= carX - obstacleWidth &&
                    obstacles[i].x <= carX + carWidth
                ) {
                    // Collision with an obstacle
                    endGame();
                }
            }
        }

        function endGame() {
            isGameOver = true;
            gameOverScreen.style.display = 'block';
            scoreDisplay.textContent = score;
        }

        function restartGame() {
            isGameOver = false;
            isPaused = false;
            carX = (canvas.width - carWidth) / 2;
            obstacles = [];
            score = 0;
            gameOverScreen.style.display = 'none';
            pauseButton.textContent = 'Pause';
        }

        function draw() {
            clearCanvas();
            drawCar();
            drawObstacles();

            // Display the score
            ctx.fillStyle = 'white';
            ctx.font = '20px Arial';
            ctx.fillText(`Score: ${score}`, 10, 30);

            if (!isGameOver && !isPaused) {
                requestAnimationFrame(draw);
            }
        }

        const gameInterval = setInterval(() => {
            if (!isGameOver && !isPaused) {
                updateCarPosition();
                updateObstacles();
                if (Math.random() < 0.3) {
                    obstacles.push({ x: Math.random() * (canvas.width - obstacleWidth), y: 0 });
                }
            }
        }, 1000 / 60); // Update at 60 frames per second

        draw();
    </script>
</body>
</html>


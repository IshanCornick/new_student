---
toc: true
comments: false
layout: post
title: Flappy Bird
description: This code sets up a basic Flappy Bird game where you control a bird by pressing any key. The bird jumps when a key is pressed, and obstacles move from right to left. The game checks for collisions with the obstacles, and the score increases each time an obstacle passes. When a collision occurs, an alert is shown displaying the score, and the game resets.
type: hacks
courses: { compsci: {week: 3} }
---

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flappy Bird</title>
    <style>
        body {
            margin: 0;
            overflow: hidden;
        }
        canvas {
            background-color: #70C5CE;
            display: block;
            margin: 0 auto;
        }
    </style>
</head>
<body>
    <canvas id="gameCanvas"></canvas>
    <script>
        const canvas = document.getElementById('gameCanvas');
        const ctx = canvas.getContext('2d');
        canvas.width = 800;
        canvas.height = 600;
        let bird = {
            x: 100,
            y: canvas.height / 2,
            width: 50,
            height: 50,
            velocityY: 0,
            gravity: 0.5,
            jumpStrength: 10
        };
        let obstacles = [];
        let score = 0;
        function drawBird() {
            ctx.fillStyle = 'yellow';
            ctx.fillRect(bird.x, bird.y, bird.width, bird.height);
        }
        function drawObstacles() {
            ctx.fillStyle = 'green';
            obstacles.forEach(obstacle => {
                ctx.fillRect(obstacle.x, obstacle.y, obstacle.width, obstacle.height);
            });
        }
        function updateBird() {
            bird.velocityY += bird.gravity;
            bird.y += bird.velocityY;
        }
        function updateObstacles() {
            obstacles.forEach(obstacle => {
                obstacle.x -= 5;
                // Check if bird collides with obstacle
                if (
                    bird.x < obstacle.x + obstacle.width &&
                    bird.x + bird.width > obstacle.x &&
                    bird.y < obstacle.y + obstacle.height &&
                    bird.y + bird.height > obstacle.y
                ) {
                    gameOver();
                }
                // If obstacle moves off screen, remove it and increase score
                if (obstacle.x + obstacle.width < 0) {
                    obstacles.splice(obstacles.indexOf(obstacle), 1);
                    score++;
                }
            });
        }
        function gameLoop() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            drawBird();
            drawObstacles();
            updateBird();
            updateObstacles();
            requestAnimationFrame(gameLoop);
        }
        function jump() {
            bird.velocityY = -bird.jumpStrength;
        }
        function spawnObstacle() {
            let height = Math.random() * (canvas.height - 200) + 50;
            obstacles.push({
                x: canvas.width,
                y: 0,
                width: 50,
                height: height
            });
            obstacles.push({
                x: canvas.width,
                y: height + 150,
                width: 50,
                height: canvas.height - height - 150
            });
        }
        function gameOver() {
            alert('Game Over!\nScore: ' + score);
            bird.y = canvas.height / 2;
            bird.velocityY = 0;
            obstacles = [];
            score = 0;
        }
        document.addEventListener('keydown', jump);
        setInterval(spawnObstacle, 2000);
        gameLoop();
    </script>
</body>
</html>
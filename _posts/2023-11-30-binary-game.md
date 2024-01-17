---
toc: true
comments: true
layout: post
title: Binary quiz
description: This is the diagram
type: hacks
courses: { compsci: {week: 13} }
---

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Binary Guessing Game</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 50px;
        }
        #output {
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <h1>Welcome to the Binary Guessing Game!</h1>
    <script>
        function generateRandomBinary(minValue, maxValue) {
            return (Math.floor(Math.random() * (maxValue - minValue + 1)) + minValue).toString(2);
        }
        function binaryGuessingGame() {
            var minValue = 0;
            var maxValue = 255;
            var secretBinary = generateRandomBinary(minValue, maxValue);
            var attempts = 0;
            while (true) {
                var playerGuess = prompt(`Guess the binary number between ${minValue.toString(2)} and ${maxValue.toString(2)}:`);
                try {
                    if (playerGuess === secretBinary) {
                        alert(`Congratulations! You guessed the correct binary number ${secretBinary} in ${attempts} attempts.`);
                        break;
                    } else {
                        if (playerGuess < secretBinary) {
                            alert("Too low! Try again.");
                            minValue = parseInt(playerGuess, 2) + 1;
                        } else {
                            alert("Too high! Try again.");
                            maxValue = parseInt(playerGuess, 2) - 1;
                        }
                        attempts += 1;
                    }
                } catch (error) {
                    alert("Invalid input. Please enter a valid binary number.");
                    continue;
                }
            }
        }
        // Run the game when the page loads
        binaryGuessingGame();
    </script>
    <div id="output"></div>
</body>
</html>

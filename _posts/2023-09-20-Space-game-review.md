---
toc: true
comments: false
layout: post
title: Documentation of the Space game
description: Description of the space game
type: hacks
courses: { compsci: {week: 4} }
---

Description:
Objective:
The objective of the game is to defeat your opponent by reducing their spaceship's health points (HP) to zero while avoiding their attacks.

Graphics and Display:

The game window is set to a size of 500x400 pixels.
The background features a space-themed image.
Health points (HP) of both players are displayed at the top corners of the screen.

Players:

There are two players in the game, represented by spaceships: one controlled by the player using the arrow keys (red), and the other controlled by the player using the 'W', 'A', 'S', and 'D' keys (yellow).
Each player starts with 10 HP.

Controls:

Player 1 (Red): Arrow keys ('LEFT', 'RIGHT', 'UP', 'DOWN') for movement, right 'SHIFT' key to shoot bullets.
Player 2 (Yellow): 'A', 'D', 'W', 'S' keys for movement, left 'SHIFT' key to shoot bullets.

Gameplay:

Players can move their spaceships left, right, up, and down within the game boundaries.
Shooting bullets is initiated by pressing the respective 'SHIFT' keys, with bullets fired from the spaceship's front.
Bullets from one player can hit the other player, reducing their HP by 1.
A hit sound effect plays when a player is hit.

Winning Condition:

The game continues until one player's HP reaches zero or below.
When a player's HP reaches zero, the game announces the winner (either "Red wins" or "Yellow wins").
The game then displays a game-over screen.
    
Sound Effects:

The game includes sound effects for shooting ('pew.ogg') and being hit ('hit-4.ogg').

How to Play:

Player 1 (Red) uses the arrow keys for movement and the right 'SHIFT' key to shoot.
Player 2 (Yellow) uses the 'A', 'D', 'W', and 'S' keys for movement and the left 'SHIFT' key to shoot.
The goal is to reduce the opponent's HP to zero while avoiding their bullets.

Notes:

The game features a fixed background and simple 2D graphics.
It uses Pygame to handle graphics, sound, and event handling.
The game loop runs at 60 frames per second (FPS).

List: 

This game uses list as a way to hold all the bullets. List are made to add and delete bullets. They are appened into the list to keep track of the amount.

Iteration: 

Iteration is used a ton throught the code. Prime examples are with "if" for shooting the bullets and moving the ship. "While true" are also used to check if the game should be ended.

Input and Output: 

This game used a ton of inputs and outputs to run. Inputs like keys being pressed would be sent to the code and a response was outputed. A ship was moved, the game was finished, shot was fired and more

Usage Instructions: 

Complexity and Performance: 
The performance of this game is decent. It runs smoothly and has easy to learn controls. It is fun to play with friends but could use some work on the gameplay. The games code is simple to follow but in some parts can be shortened.

Error Handling: 

With this code there was very few error but 2 main ones. One was the game lagging after a while from to many bullets off screen. To fix this we make it so the bullets would be deleted as they went off screen. Another error was with the boaders as the entire image was able to cross the board on the left because it was set to the top right corner of the image. To fix this I added valued to the ship and make a hitbox. 
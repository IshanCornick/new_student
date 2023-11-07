---
toc: true
comments: true
layout: post
title: Flash cards
description: This is connection of backend and frontend
type: hacks
courses: { compsci: {week: 11} }
---

<!DOCTYPE html>
<html>
<head>
    <title>Frog Flash Cards</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            text-align: center;
            margin: 0;
            padding: 0;
        }

        #flash-cards-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
        }

        .flash-card {
            width: 200px;
            height: 120px;
            background-color: #fff; /* White background for the flash card */
            border: 1px solid #ccc;
            margin: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: transform 0.2s ease-in-out;
            position: relative;
            border-radius: 5px;
        }

        .flash-card:hover {
            transform: scale(1.05);
        }

        .front, .back {
            background-color: #fff; /* White background for both sides */
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100%;
            text-align: center;
            padding: 10px;
        }

        .front {
            color: #000; /* Black text color */
            border-radius: 5px;
        }

        .back {
            color: #000; /* Black text color */
            display: none;
        }

        h3 {
            font-size: 20px;
            margin: 0;
            padding: 5px;
        }

        p {
            font-size: 14px;
            margin: 0;
            padding: 5px;
        }
    </style>
</head>
<body>
    <div id="flash-cards-container"></div>

    <script>
        const flashCardsContainer = document.getElementById("flash-cards-container");

        // Fetch data from your backend API
        fetch('https://projectsailbackend.stu.nighthawkcodingsociety.com/api/frog-items/') // Replace with your actual API endpoint
            .then(response => response.json())
            .then(data => {
                data.forEach(frog => {
                    const flashCard = document.createElement("div");
                    flashCard.className = "flash-card";
                    flashCard.innerHTML = `
                        <div class="front">
                            <h3>${frog.name}</h3>
                        </div>
                        <div class="back">
                            <p>Prey: ${frog.prey}<br>Predators: ${frog.predators}</p>
                        </div>
                    `;
                    flashCardsContainer.appendChild(flashCard);

                    flashCard.addEventListener("click", () => {
                        flashCard.querySelector(".front").style.display = "none";
                        flashCard.querySelector(".back").style.display = "block";
                    });

                    flashCard.addEventListener("mouseleave", () => {
                        flashCard.querySelector(".front").style.display = "block";
                        flashCard.querySelector(".back").style.display = "none";
                    });
                });
            })
            .catch(error => console.error(error));
    </script>
</body>
</html>

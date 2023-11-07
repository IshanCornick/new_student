---
toc: true
comments: false
layout: post
title: Image Searcher
description: This code allows you to search up images.
type: hacks
courses: { compsci: {week: 7} }
---

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    
    <form id="search-form">
        <input type="text" id="query" placeholder="Enter your search query">
        <button type="submit">Search</button>
    </form>
    <div id="image-results"></div>

    <script>
        const searchForm = document.getElementById('search-form');
        const queryInput = document.getElementById('query');
        const imageResults = document.getElementById('image-results');

        searchForm.addEventListener('submit', function (e) {
            e.preventDefault();
            const query = queryInput.value;
            if (query) {
                // Replace 'YOUR_API_KEY' with your actual Unsplash API key
                const apiKey = 'n9U-OR3Ylnh7at-fl7b7dFETxYrtLaB3CAzvUc6GRCY';
                const apiUrl = `https://api.unsplash.com/search/photos?query=${query}&per_page=10&client_id=${apiKey}`;

                fetch(apiUrl)
                    .then(response => response.json())
                    .then(data => {
                        displayImageResults(data.results);
                    })
                    .catch(error => {
                        console.error('Error fetching data:', error);
                    });
            }
        });

        function displayImageResults(results) {
            imageResults.innerHTML = '';

            results.forEach(result => {
                const imgElement = document.createElement('img');
                imgElement.src = result.urls.small;
                imgElement.alt = result.description;
                imageResults.appendChild(imgElement);
            });
        }
    </script>
</body>
</html>

function loadNews() {
    fetch("/api/news")  // Appeler l'API pour récupérer les actualités
        .then(response => response.json())  // Convertir la réponse en JSON
        .then(data => {
            // Préparer le HTML pour afficher les articles
            let htmlContent = "<h1>Actualités</h1>";

            if (data.length > 0) {
                data.forEach(article => {
                    htmlContent += `
                        <div class="article">
                            <h2>${article.title || 'Titre indisponible'}</h2>
                            <img src="${article.image_url || ''}" alt="Image de l'article" style="width: 300px;">
                            <p>${article.summary || 'Résumé indisponible'}</p>
                            <a href="${article.url || '#'}" target="_blank">Lire l'article</a>
                        </div>
                    `;
                });
            } else {
                htmlContent += "<p>Aucun article disponible.</p>";
            }

            // Insérer les articles dans le bloc content
            document.getElementById("content").innerHTML = htmlContent;
        })
        .catch(error => {
            console.error('Erreur lors du chargement des actualités :', error);
            document.getElementById("content").innerHTML = "<p>Erreur lors du chargement des actualités.</p>";
        });
}


function loadMeteo() {
    document.getElementById("content").innerHTML = "<h2>Page Météo</h2>";
}

function loadCalendrier() {
    document.getElementById("content").innerHTML = "<h2>Page Calendrier</h2>";
}

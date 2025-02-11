function loadNews() {
    fetch('http://back:5000/api/news')  // Utiliser 'back' pour communiquer entre les conteneurs Docker
        .then(response => response.json())
        .then(data => {
            console.log(data);  // Afficher les données dans la console pour vérifier
            let newsHtml = '<h2>Actualités</h2>';
            if (data.length > 0) {
                data.forEach(article => {
                    newsHtml += `<p>${article.title}</p>`;
                });
            } else {
                newsHtml += '<p>Aucune actualité disponible.</p>';
            }
            document.getElementById('content').innerHTML = newsHtml;
        })
        .catch(error => {
            console.error('Erreur lors du chargement des actualités:', error);
            document.getElementById('content').innerHTML = 'Erreur lors du chargement des actualités.';
        });
}



function loadMeteo() {
    document.getElementById("content").innerHTML = "<h2>Page Météo</h2>";
}

function loadCalendrier() {
    document.getElementById("content").innerHTML = "<h2>Page Calendrier</h2>";
}

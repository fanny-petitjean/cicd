document.addEventListener("DOMContentLoaded", function() {
    fetch('http://localhost:8080/api/nouvelles')  // Appelle l'API Flask
    .then(response => response.json())
    .then(data => {
        let content = document.getElementById('news-container');
        content.innerHTML = "";  // Efface "Chargement..."
        data.forEach(article => {
            let item = `<h3>${article.title}</h3>
                        <a href="${article.url}" target="_blank">Lire l'article</a>
                        <hr>`;
            content.innerHTML += item;
        });
    })
    .catch(error => console.error('Erreur:', error));
});

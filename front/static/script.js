async function loadNews() {
    const response = await fetch("http://127.0.0.1:5000/api/news");
    const articles = await response.json();
    
    let contentDiv = document.getElementById("content");
    contentDiv.innerHTML = "<h2>Dernières news</h2>";
    
    articles.forEach(article => {
        contentDiv.innerHTML += `<p><strong>${article.title}</strong> - <a href="${article.url}" target="_blank">Lire</a></p>`;
    });
}

function loadMeteo() {
    document.getElementById("content").innerHTML = "<h2>Page Météo</h2>";
}

function loadCalendrier() {
    document.getElementById("content").innerHTML = "<h2>Page Calendrier</h2>";
}

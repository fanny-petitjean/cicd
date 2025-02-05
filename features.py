import requests

url = "https://api.spaceflightnewsapi.net/v4/articles/"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    articles = data["results"]
    index = 0
    step = 5  # Nombre d'articles à afficher à chaque fois
    
    def show_articles():
        global index
        for article in articles[index:index + step]:
            print(f"Titre: {article['title']}")
            print(f"URL: {article['url']}\n")
        index += step

    # Affichage initial
    show_articles()
    print(len(articles))
    while index < len(articles):
        user_input = input("Tape 'more' pour voir plus ou 'exit' pour quitter: ").strip().lower()
        if user_input == "more":
            show_articles()
        elif user_input == "exit":
            break
        else:
            print("Commande inconnue. Tape 'more' pour continuer ou 'exit' pour quitter.")
    
    print("Plus d'articles disponibles.")
else:
    print(f"Erreur {response.status_code}: Impossible de récupérer les données")

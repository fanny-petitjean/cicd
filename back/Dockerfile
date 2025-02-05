# Utiliser l'image Python officielle
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /usr/src/app

# Copier les fichiers de requirements
COPY requirements.txt ./

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le code de l'application
COPY . /usr/src/app

# Exposer le port sur lequel Flask va tourner
EXPOSE 5000

# Commande pour démarrer l'application
CMD ["python", "app.py"]

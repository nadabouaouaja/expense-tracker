# Utilisation d'une image de base
FROM python:3.9

# Définition du répertoire de travail
WORKDIR /app

# Copier les fichiers du projet
COPY . .

# Installer les dépendances
RUN pip install -r requirements.txt

# Exposer le port de l'application
EXPOSE 5000

# Commande pour exécuter l'application
CMD ["python", "app.py"]

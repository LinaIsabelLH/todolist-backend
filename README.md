# ✅ To Do List App ➔ API Backend

![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![Django](https://img.shields.io/badge/Django-4.x-green.svg)
![Django REST Framework](https://img.shields.io/badge/DRF-3.x-red.svg)

Ce dépôt contient le code backend pour une application de liste de tâches (ToDo List). Il s'agit d'une API RESTful construite avec Django et Django REST Framework, permettant de gérer des catégories et des tâches associées.

## Fonctionnalités

*   **Gestion des Catégories** : CRUD complet (Créer, Lire, Mettre à jour, Supprimer) pour les catégories de tâches.
*   **Gestion des Tâches** : CRUD complet pour les tâches.
*   **Relation Tâche-Catégorie** : Chaque tâche est liée à une catégorie.
*   **Filtrage** : Possibilité de lister uniquement les tâches appartenant à une catégorie spécifique.
*   **Validation des données** : Empêche la création de catégories avec des noms en double.
*   **CORS** : Pré-configuré pour autoriser les requêtes depuis un serveur de développement frontend (React app avec Vite).

## API Endpoints

Voici la liste des points d'accès disponibles. Le préfixe de base de l'API est `/api/`.

### Catégories (`/api/categories/`)

| Endpoint | Méthode | Description |
| :--- | :--- | :--- |
| `/api/categories/` | `GET` | Lister toutes les catégories. |
| `/api/categories/` | `POST` | Créer une nouvelle catégorie. |
| `/api/categories/{id}/` | `GET` | Récupérer les détails d'une catégorie spécifique. |
| `/api/categories/{id}/` | `PUT`/`PATCH` | Mettre à jour une catégorie. |
| `/api/categories/{id}/` | `DELETE` | Supprimer une catégorie. |

### Tâches (`/api/tasks/`)

| Endpoint | Méthode | Description |
| :--- | :--- | :--- |
| `/api/tasks/` | `GET` | Lister toutes les tâches, triées par date de création (la plus récente en premier). |
| `/api/tasks/` | `POST` | Créer une nouvelle tâche. |
| `/api/tasks/{id}/` | `GET` | Récupérer les détails d'une tâche spécifique. |
| `/api/tasks/{id}/` | `PUT`/`PATCH` | Mettre à jour une tâche. |
| `/api/tasks/{id}/` | `DELETE` | Supprimer une tâche. |

#### Filtrage des Tâches

Pour ne lister que les tâches d'une catégorie spécifique, utilisez le paramètre de requête `category_id`.

**Exemple :**
```
GET /api/tasks/?category_id=1
```
Cette requête renverra uniquement les tâches appartenant à la catégorie avec l'ID `1`.

## Technologies utilisées

*   [Django](https://www.djangoproject.com/)
*   [Django REST Framework](https://www.django-rest-framework.org/)
*   [django-cors-headers](https://github.com/adamchainz/django-cors-headers)

## Installation et Lancement

Suivez ces étapes pour mettre en place l'environnement de développement et lancer le projet.

**1. Cloner le dépôt**
```bash
git clone https://github.com/LinaIsabelLH//todolist-backend.git
cd todolist-backend
```

**2. Créer et activer un environnement virtuel**

*   Sur macOS / Linux :
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```
*   Sur Windows :
    ```bash
    python -m venv env
    .\env\Scripts\activate
    ```

**3. Installer les dépendances**

Il est recommandé de créer un fichier `requirements.txt`. Vous pouvez le faire avec la commande suivante :
```bash
pip freeze > requirements.txt
```
Ensuite, pour installer les dépendances :
```bash
pip install -r requirements.txt
```
Si vous n'avez pas de fichier `requirements.txt`, installez les paquets manuellement :
```bash
pip install django djangorestframework django-cors-headers
```

**4. Naviguer dans le projet Django**

Le projet Django a été créé dans un sous-dossier `backend`.
```bash
cd backend
```

**5. Appliquer les migrations**

Cette commande créera la base de données SQLite et les tables nécessaires basées sur les modèles.
```bash
python manage.py makemigrations
python manage.py migrate
```

**6. Lancer le serveur de développement**

```bash
python manage.py runserver
```

L'API sera alors accessible à l'adresse [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/).

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

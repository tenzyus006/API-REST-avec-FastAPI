# API-REST-avec-FastAPI
This is my custom profile. API Deployment [ API REST avec FastAPI ]
# API-REST-avec-FastAPI

Une API RESTful pour la classification et le balisage de texte, développée avec FastAPI.
Ce projet montre comment utiliser un modèle de machine learning et un outil de binarisation d'étiquettes avec FastAPI, avec des instructions de déploiement pour Heroku.

---

## Fonctionnalités

- **Point de terminaison de prédiction** : obtenez rapidement des prédictions d'étiquettes pour le texte d'entrée via « /predict ».
- **Pipeline ML pré-entraîné** : utilise un pipeline scikit-learn et un outil MultiLabelBinarizer.
- **Téléchargement automatique du fichier modèle** : au démarrage, télécharge le modèle et l'outil de binarisation d'étiquettes à partir des URL.

---

## Exécution locale

1. **Cloner le dépôt** :
```sh
git clone <votre-url-de-dépôt>
cd API-REST-avec-FastAPI
```

2. **Créer un environnement virtuel et l'activer** :
```sh
python3.12 -m venv venv
source venv/bin/activate
```

3. **Installer les dépendances** :
```sh
pip install -r requirements.txt
```

4. **Définir les variables d'environnement pour les fichiers de modèle**
Obtenez les URL publiques de vos fichiers de modèle (voir ci-dessous), puis :
```sh
export LOGISTIC_MODEL_URL=<votre-url-de-modèle-logistique>
export MLB_URL=<votre-url-de-modèle-mlb>
```

5. **Exécuter l'API** :
```sh
uvicorn api:app --reload
```

---

## Déploiement sur Heroku

1. **Définir les variables de configuration pour les URL de modèle dans le tableau de bord Heroku**
Accédez à votre application → Paramètres → Afficher les variables de configuration, puis définissez :
- `LOGISTIC_MODEL_URL`
- `MLB_URL`

2. **Déploiement :**
```sh
git push heroku main
```

---

## Configuration du fichier de modèle

- `logistic_model_tfidf.pkl` : Votre pipeline scikit-learn entraîné.
- `mlb.pkl` : Votre MultiLabelBinarizer picklé.
- Importez ces fichiers vers un service de stockage public (S3, Hugging Face, etc.) et utilisez les liens directs pour vos variables d'environnement.

---

## Utilisation de l'API

- **POST /predict**
- Corps de la requête : `{ "text": "Votre exemple de texte ici" }`
- Réponse : `{ "tags": ["tag1", "tag2", ...] }`

---
## Exemple de requête

```bash
curl -X POST "http://localhost:8000/predict" \
-H "Content-Type: application/json" \
-d '{"text": "Texte à classer"}'
```
---

## Licence
Licence MIT
---

## Auteur

Tenzin WANGMO

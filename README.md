# ECOPulse – Centralisation et analyse des risques environnementaux

**ECOPulse** est une application qui centralise des données environnementales pour anticiper les risques d’inondation et de sécheresse. Elle fournit des indicateurs analytiques exploitables pour la prise de décision préventive.

---

## 📂 Structure du projet

```
bigdata-flood-drought-app/
│
├─ backend/
│   ├─ bronze/          # Données brutes multi-sources
│   │   ├─ weather
│   │   │    └─ ingest_weather.py
│   │   │    └─ weather_all_world.json
│   │   │    └─ zones_world_major.csv
│   │   └─ soil
│   │   │    └─ ingest_soil.py
│   │   │    └─ soil_data_world.csv
│   ├─ silver/          # Données nettoyées et harmonisées
│   │   └─ ingest_silver.py
│   │   └─ silver_data_world.csv
│   ├─ gold/            # Données agrégées pour l’analyse
│   │   └─ gold_daily_risk.csv
    │   └─ ingest_gold.py
│   ├─ app.py           # API FastAPI
│   ├─ ingest_weather.py
│   ├─ ingest_soil.py
│   └─ ingest_floods.py
│
├─ notebooks/           # Notebooks pour visualisation et analyse
└─ README.md            # Ce fichier
```

---

## ⚙️ Installation

1. Cloner le projet :

```bash
git clone <URL_DU_PROJET>
cd bigdata-flood-drought-app/backend
```

2. Créer un environnement Python (optionnel mais recommandé) :

```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

3. Installer les dépendances :

```bash
pip install -r requirements.txt
```

> Packages requis : `fastapi`, `uvicorn`, `pandas`, `requests`, `matplotlib` (pour visualisation)

---

## 🚀 Lancer le serveur

```bash
python -m uvicorn app:app --reload --port 9000
```

* Accès à l’API : `http://127.0.0.1:9000/`
* Interface Swagger pour tester les endpoints : `http://127.0.0.1:9000/docs`

---

## 🔹 Endpoints principaux

| Endpoint           | Méthode | Description                              |
| ------------------ | ------- | ---------------------------------------- |
| `/`                | GET     | Vérifie que l’API fonctionne             |
| `/zones`           | GET     | Liste toutes les zones disponibles       |
| `/risk/{zone_id}`  | GET     | Indicateurs flood/drought pour une zone  |
| `/top_flood?n=5`   | GET     | Top N zones à risque d’inondation élevé  |
| `/top_drought?n=5` | GET     | Top N zones à risque de sécheresse élevé |

> Paramètres optionnels : `start` et `end` pour filtrer par date.

---

## 🛠️ Scripts d’ingestion

* `ingest_weather.py` : Récupère les données météo (Open-Meteo/OpenWeather).
* `ingest_soil.py` : Récupère le type de sol et la capacité de rétention.
* `ingest_floods.py` : Récupère l’historique des inondations.
* `ingest_silver.py` : Nettoie et fusionne les données pour la table Silver.
* `ingest_gold.py` : Agrège et calcule les indicateurs pour la table Gold.

---

## 💾 Gestion des données

1. **Bronze** : Données brutes multi-sources.
2. **Silver** : Données nettoyées et harmonisées.
3. **Gold** : Tables analytiques prêtes à l’analyse et visualisation.

---

## 📊 Visualisation

* Les fichiers Gold (`gold_daily_risk.csv`) peuvent être utilisés dans :

  * Notebook Python (Jupyter / Colab)
  * Power BI / Tableau pour dashboards interactifs

* Exemple minimal avec Matplotlib :

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("gold/gold_daily_risk.csv")
df.plot(x="zone_id", y=["flood_risk", "drought_risk"], kind="bar")
plt.show()
```

---

## 🔧 Conseils

* Toujours vérifier que le serveur FastAPI est lancé.
* Supprimer les caches Python `__pycache__` si des modifications ne sont pas prises en compte.
* Les endpoints `/zones` et `/risk/{zone_id}` sont les principaux pour les visualisations.

---

## ✅ Objectifs

* Centraliser les données environnementales multi-sources.
* Mettre en place une architecture Big Data complète (Bronze → Silver → Gold).
* Produire des indicateurs analytiques exploitables.
* Aider à la prise de décision préventive pour la gestion des risques.

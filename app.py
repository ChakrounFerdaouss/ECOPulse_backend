from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI(title="EnviroRisk API")

# ✅ ADD CORS HERE
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Charger les données Gold
GOLD_PATH = "gold/gold_daily_risk.csv"
gold_df = pd.read_csv(GOLD_PATH)
gold_df["date"] = pd.to_datetime(gold_df["date"])

@app.get("/")
def root():
    return {"message": "EnviroRisk API en ligne"}

@app.get("/zones")
def list_zones():
    zones = gold_df["zone_id"].unique().tolist()
    return {"zones": zones}

@app.get("/risk/{zone_id}")
def risk_by_zone(zone_id: str):
    data = gold_df[gold_df["zone_id"] == zone_id]
    if data.empty:
        return {"error": "Zone non trouvée"}
    return data.to_dict(orient="records")

@app.get("/top_flood")
def top_flood(n: int = 10):
    """Retourne les top n zones avec le plus haut flood risk moyen"""
    top = (
        gold_df.groupby("zone_id")["flood_risk"]
        .mean()
        .sort_values(ascending=False)
        .head(n)
    )
    return top.reset_index().to_dict(orient="records")

@app.get("/top_drought")
def top_drought(n: int = 10):
    """Retourne les top n zones avec le plus haut drought risk moyen"""
    top = (
        gold_df.groupby("zone_id")["drought_risk"]
        .mean()
        .sort_values(ascending=False)
        .head(n)
    )
    return top.reset_index().to_dict(orient="records")

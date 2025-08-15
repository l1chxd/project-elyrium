# Next.js + Tailwind CSS + TypeScript Starter and Boilerplate

<div align="center">

# 🧠 project-elyrium

**project-elyrium** ist ein KI-gestütztes Marktprognose-Dashboard, das mit **Next.js**, **Tailwind CSS**, **TypeScript** und einem **FastAPI-Backend** entwickelt wird. Ziel ist es, auf täglicher, wöchentlicher und monatlicher Basis präzise Kursprognosen für Kryptowährungen (z. B. BTC/USD) zu liefern – inklusive Entry-Zonen, Confidence-Werten und Chart-Visualisierungen.

---

## 🚀 Features

- 📈 Tagesprognose: dynamisch basierend auf aktueller Uhrzeit
- 🎯 Entry-Zonen mit Wahrscheinlichkeit & Confidence-Level
- 📊 Live-Chart mit Kursverlauf (ApexCharts)
- 🤖 Backend-API via FastAPI mit späterer ML-Integration
- 💨 Tailwind CSS & responsive Design
- 📦 Modularer Aufbau (Snapshot-basierte Roadmap)

---

## 🧩 Tech Stack

- Frontend: Next.js 14, React 18, TypeScript, Tailwind CSS 3
- Charting: ApexCharts via `react-apexcharts`
- Backend: Python, FastAPI
- Deployment: lokal (später optional via Vercel + Docker)

---

## 🛠 Setup

```bash
# 1. Projekt klonen
git clone https://github.com/l1chxd/project-elyrium.git
cd project-elyrium

# 2. Abhängigkeiten installieren (Frontend)
npm install

# 3. Entwicklungsserver starten
npm run dev

# 4. Backend starten (in separatem Terminal)
cd backend
source venv/bin/activate
uvicorn main:app --reload
```

---

## 📦 Snapshots (Roadmap)

| Snapshot | Inhalt                                                           |
|----------|------------------------------------------------------------------|
| 1        | Prognose-Dashboard mit statischen Uhrzeiten                     |
| 2        | Dynamische Zeitpunkte + BTC-Demo-Chart (lokal)                  |
| 3        | Live-Datenintegration (z. B. CoinGecko)                          |
| 4        | Entry-Zonen + einfache ML-Prognose                              |
| 5        | Auth, User-Modus, Personalisierung (Scalper, Swing usw.)        |

---

## 🧠 Autor

Projektidee, Umsetzung & Code von [@l1chxd](https://github.com/l1chxd)

---

## 📝 Lizenz

MIT License – frei verwendbar & anpassbar.

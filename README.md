# 🏎 F1 Race Intelligence Copilot v2

> AI-powered Formula 1 strategy simulator built on real telemetry data,
> machine learning and AWS cloud deployment.

## 📊 Model Results
| Metric | Score |
|--------|-------|
| MAE | 0.313 seconds |
| Baseline MAE | 0.790 seconds |
| Improvement | 60.3% |
| R² Score | 0.80 |
| Data | 802 laps — 2023 British GP |

## 🔍 Key Findings
- Optimal pit window for VER at Silverstone: **Lap 14**
- Track evolution dominates tyre degradation at Silverstone 2023
- LapNumber is the strongest predictor of lap time (35% importance)


## 🛠 Tech Stack
- **Data**: FastF1 API (real F1 telemetry, free and open source)
- **ML Model**: XGBoost regression
- **Analysis**: Pandas, NumPy, Matplotlib, Seaborn
- **Deployment**: AWS Lambda + S3 (coming soon)
- **Interface**: Gradio (coming soon)

## 📁 Project Structure
```
F1-Race-Intelligence-Copilot-v2/
├── notebooks/
│   ├── 01_data_pipeline.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_lap_time_model.ipynb
│   └── 04_strategy_simulator.ipynb
├── data/
│   ├── processed/
│   └── charts/
├── models/
│   └── lap_time_predictor.pkl
└── requirements.txt
```

## 🚀 How to Run
```bash
git clone https://github.com/Noel2521/F1-Race-Intelligence-Copilot-v2
pip install -r requirements.txt
jupyter notebook notebooks/01_data_pipeline.ipynb
```


## 📈 Notebooks
1. **01_data_pipeline** — Pulls real F1 data using FastF1 API, 
   cleans and saves 802 laps from 2023 British GP
2. **02_eda** — Exploratory analysis: lap time distributions, 
   tyre degradation curves, driver pace comparison
3. **03_lap_time_model** — XGBoost model predicting lap times 
   to within 0.313 seconds MAE
4. **04_strategy_simulator** — Simulates pit stop windows, 
   finds optimal strategy for any driver

## 👤 Author
**Noel Anthony**  
ML Engineer | MSc University of South Wales  
Open to relocation | Targeting motorsport & simulation roles  
[GitHub](https://github.com/Noel2521)
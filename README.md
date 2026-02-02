# 🚦 ML-Based Adaptive Network Congestion Controller

> A systems + machine learning project that simulates network congestion, predicts it using ML, and dynamically controls traffic to reduce packet loss using a closed-loop feedback mechanism.

---

## 📌 Overview

Traditional networks rely on static congestion control, reacting after congestion occurs.  
This project demonstrates how machine learning can proactively control network traffic before packet loss happens.

---

## 🚀 What This System Does

- Simulates real network congestion (queues, bandwidth, packet drops)
- Generates its own dataset from system behavior
- Trains an ML model to predict congestion
- Uses ML predictions to actively control traffic
- Achieves more than 99% reduction in packet loss

---

## 🎯 Key Features

- Network congestion simulation  
- Automatic dataset generation  
- ML-based congestion prediction (Logistic Regression)  
- Closed-loop adaptive controller  
- Static vs Adaptive system comparison  
- Lightweight and CPU-safe  

---

## 🧠 System Architecture

### High-Level Flow

```mermaid
flowchart LR
    Traffic[Incoming Traffic] --> Router[Router Queue]
    Router --> Stats[Network Statistics]
    Stats --> ML[ML Congestion Predictor]
    ML --> Decision{Congestion?}
    Decision -->|Yes| Reduce[Reduce Traffic Rate]
    Decision -->|No| Normal[Allow Normal Traffic]
    Reduce --> Traffic
    Normal --> Traffic
🏗️ Project Structure
ml-network-congestion/
│
├── simulator/
│   ├── network_simulator.py
│   └── data_collector.py
│
├── data/
│   └── network_data.csv
│
├── ml/
│   ├── train_model.py
│   └── congestion_model.pkl
│
├── controller/
│   └── adaptive_controller.py
│
├── README.md
└── .gitignore
⚙️ Module Breakdown
Network Simulation
Models packet arrival, router queues, and bandwidth limits

Simulates congestion and packet drops under heavy traffic

Dataset Generation
Extracted features:

Incoming packet rate

Queue length

Sent packets

Dropped packets

Labels:

0 → No congestion

1 → Congestion

Machine Learning Model
Model: Logistic Regression

Fast, interpretable, low latency

Saved and reused for prediction

Adaptive Congestion Controller
flowchart TD
    Start[Simulation Running]
    Start --> Collect[Collect Network Stats]
    Collect --> Predict[ML Predicts Congestion]
    Predict -->|Congested| Throttle[Reduce Incoming Traffic]
    Predict -->|Clear| Allow[Allow Normal Traffic]
    Throttle --> Continue[Continue Simulation]
    Allow --> Continue
This forms a closed-loop feedback control system.

🧪 Experimental Results
Static System

Total packets dropped: 1188
ML-Adaptive System

Total packets dropped: 10
Packet loss reduced by more than 99%.

▶️ How to Run
.\.venv\Scripts\activate
python simulator/data_collector.py
python ml/train_model.py
python controller/adaptive_controller.py
👩‍💻 Author
Bhumika Kumari
B.Tech Computer Science & Engineering

GitHub: https://github.com/Bhumika-0204
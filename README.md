# 🚦 ML-Based Adaptive Network Congestion Controller

> A systems + machine learning project that simulates network congestion, predicts it using ML, and dynamically controls traffic to reduce packet loss using a closed-loop feedback mechanism.

---

## 📌 Overview

Traditional networks rely on **static congestion control**, reacting *after* congestion occurs.  
This project demonstrates how **machine learning can proactively control network traffic** to prevent congestion **before packet loss happens**.

---

## 🚀 What This System Does

- Simulates real network congestion (queues, bandwidth, packet drops)
- Generates its own dataset from system behavior
- Trains an ML model to predict congestion
- Uses ML predictions to actively control traffic
- Achieves **more than 99% reduction in packet loss**

---

## 🎯 Key Features

- 📡 Network congestion simulation  
- 📊 Automatic dataset generation  
- 🤖 ML-based congestion prediction (Logistic Regression)  
- 🔁 Closed-loop adaptive controller  
- 📉 Static vs Adaptive system comparison  
- ⚡ Lightweight, CPU-safe, reproducible  

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
    Normal --> Traffic ```
    
🏗️ Project Structure
ml-network-congestion/
│
├── simulator/
│   ├── network_simulator.py      # Basic congestion simulation
│   └── data_collector.py         # Dataset generation
│
├── data/
│   └── network_data.csv          # Generated dataset
│
├── ml/
│   ├── train_model.py            # ML training script
│   └── congestion_model.pkl      # Trained ML model
│
├── controller/
│   └── adaptive_controller.py    # ML-based adaptive controller
│
├── README.md
└── .gitignore
⚙️ Module Breakdown
1️⃣ Network Simulation
Models packet arrival, router queues, and bandwidth limits

Simulates congestion and packet drops under heavy traffic

2️⃣ Dataset Generation
Extracted features from live simulation:

Incoming packet rate

Queue length

Sent packets

Dropped packets

Congestion labels:

0 → No congestion

1 → Congestion

3️⃣ Machine Learning Model
Model: Logistic Regression

Why Logistic Regression?

Fast inference

Low latency

Interpretable

Suitable for real-time systems

The trained model is saved and reused for prediction (no retraining required).

4️⃣ Adaptive Congestion Controller (Core Innovation)
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
❌ Static System (No ML)
Total packets dropped: 1188
✅ ML-Adaptive System
Total packets dropped: 10
📉 Packet loss reduced by more than 99%

▶️ How to Run
1️⃣ Activate virtual environment
.\.venv\Scripts\activate
2️⃣ Generate dataset
python simulator/data_collector.py
3️⃣ Train ML model
python ml/train_model.py
4️⃣ Run adaptive controller
python controller/adaptive_controller.py
🧠 Why This Project Is Strong
This project goes beyond ML prediction and demonstrates ML-driven system control.

It showcases:

Core computer networks concepts

Machine learning applied to real systems

Feedback control loops

Experimental comparison

Clean engineering practices (Git, modular design)

📈 Future Enhancements
Reinforcement Learning–based controller

Multi-router / network topology simulation

Software-Defined Networking (SDN) integration

Real-time visualization dashboard

Cloud traffic management use cases

👩‍💻 Author
Bhumika Kumari
B.Tech Computer Science & Engineering

Focus: Machine Learning + Core CSE + Systems

GitHub: https://github.com/Bhumika-0204

⭐ Final Note
This project reflects real-world ML + networking engineering, not just academic theory.
If you found it useful, feel free to ⭐ star the repository.
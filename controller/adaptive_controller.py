from collections import deque
import joblib
import pandas as pd

# ---------------- LOAD TRAINED ML MODEL ----------------
model = joblib.load("ml/congestion_model.pkl")


# ---------------- PACKET CLASS ----------------
class Packet:
    def __init__(self, arrival_time):
        self.arrival_time = arrival_time


# ---------------- ROUTER CLASS ----------------
class Router:
    def __init__(self, bandwidth, max_queue_size):
        self.bandwidth = bandwidth
        self.queue = deque()
        self.max_queue_size = max_queue_size
        self.dropped = 0


# ---------------- RECEIVE PACKETS ----------------
def receive_packets(router, packet_count, time):
    for _ in range(packet_count):
        if len(router.queue) < router.max_queue_size:
            router.queue.append(Packet(time))
        else:
            router.dropped += 1


# ---------------- SEND PACKETS ----------------
def send_packets(router):
    sent = 0
    for _ in range(router.bandwidth):
        if router.queue:
            router.queue.popleft()
            sent += 1
        else:
            break
    return sent


# ---------------- STATIC SYSTEM (NO ML) ----------------
def static_simulation():
    router = Router(bandwidth=8, max_queue_size=20)

    for time in range(1, 101):
        incoming_packets = 20  # fixed traffic
        receive_packets(router, incoming_packets, time)
        send_packets(router)

    print("STATIC SYSTEM")
    print("Total packets dropped:", router.dropped)
    print("-" * 40)


# ---------------- ADAPTIVE SYSTEM (ML CONTROLLED) ----------------
def adaptive_simulation():
    router = Router(bandwidth=8, max_queue_size=20)

    for time in range(1, 101):

        # ---- ML FEATURES (WITH COLUMN NAMES) ----
        features = pd.DataFrame([{
            "incoming_rate": 20,
            "queue_length": len(router.queue),
            "sent_packets": router.bandwidth,
            "dropped_packets": router.dropped
        }])

        prediction = model.predict(features)[0]

        # ---- ML-BASED CONTROL LOGIC ----
        if prediction == 1:
            incoming_packets = 6    # reduce traffic
        else:
            incoming_packets = 20   # normal traffic

        receive_packets(router, incoming_packets, time)
        send_packets(router)

    print("ADAPTIVE SYSTEM (ML CONTROLLED)")
    print("Total packets dropped:", router.dropped)
    print("-" * 40)


# ---------------- MAIN ----------------
if __name__ == "__main__":
    static_simulation()
    adaptive_simulation()

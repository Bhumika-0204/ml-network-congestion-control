import csv
from collections import deque

print("Running data_collector.py...")

class Packet:
    def __init__(self, arrival_time):
        self.arrival_time = arrival_time


class Router:
    def __init__(self, bandwidth, max_queue_size):
        self.bandwidth = bandwidth
        self.queue = deque()
        self.max_queue_size = max_queue_size
        self.total_dropped = 0


def receive_packets(router, packet_count, current_time):
    for _ in range(packet_count):
        if len(router.queue) < router.max_queue_size:
            router.queue.append(Packet(current_time))
        else:
            router.total_dropped += 1


def send_packets(router):
    sent = 0
    for _ in range(router.bandwidth):
        if router.queue:
            router.queue.popleft()
            sent += 1
        else:
            break
    return sent


def simulate_and_collect():
    router = Router(bandwidth=8, max_queue_size=20)

    with open("data/network_data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "time",
            "incoming_rate",
            "queue_length",
            "sent_packets",
            "dropped_packets",
            "congestion"
        ])

        for time in range(1, 101):

            # 🚨 THIS IS THE KEY PART 🚨
            if time <= 40:
                incoming_packets = 6      # no congestion
            else:
                incoming_packets = 25     # heavy congestion

            receive_packets(router, incoming_packets, time)
            sent = send_packets(router)

            queue_length = len(router.queue)

            # explicit congestion condition
            congestion = 1 if queue_length >= 10 else 0

            writer.writerow([
                time,
                incoming_packets,
                queue_length,
                sent,
                router.total_dropped,
                congestion
            ])

    print("Dataset written with BOTH classes (0 and 1)")


if __name__ == "__main__":
    simulate_and_collect()

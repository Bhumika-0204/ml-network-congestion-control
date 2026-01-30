from collections import deque


# -------------------- PACKET --------------------
class Packet:
    def __init__(self, arrival_time):
        self.arrival_time = arrival_time


# -------------------- ROUTER --------------------
class Router:
    def __init__(self, bandwidth, max_queue_size):
        self.bandwidth = bandwidth              # packets/sec
        self.queue = deque()
        self.max_queue_size = max_queue_size
        self.total_dropped = 0


# -------------------- RECEIVE PACKETS --------------------
def receive_packets(router, packet_count, current_time):
    for _ in range(packet_count):
        if len(router.queue) < router.max_queue_size:
            router.queue.append(Packet(current_time))
        else:
            router.total_dropped += 1


# -------------------- SEND PACKETS --------------------
def send_packets(router):
    sent = 0
    for _ in range(router.bandwidth):
        if router.queue:
            router.queue.popleft()
            sent += 1
        else:
            break
    return sent


# -------------------- SIMULATION --------------------
def simulate():
    router = Router(bandwidth=8, max_queue_size=20)

    print("Starting Network Simulation...\n")

    for time in range(1, 31):
        incoming_packets = 12  # heavy traffic
        receive_packets(router, incoming_packets, time)
        sent = send_packets(router)

        print(
            f"Time {time}s | "
            f"Queue Size: {len(router.queue)} | "
            f"Sent: {sent} | "
            f"Dropped: {router.total_dropped}"
        )


if __name__ == "__main__":
    simulate()

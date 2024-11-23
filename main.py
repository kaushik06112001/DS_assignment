class LamportClock:
    def __init__(self, process_id):
        self.process_id = process_id
        self.clock = 0

    def increment(self):
        """Increment the clock for an internal event."""
        self.clock += 1
        print(f"Process {self.process_id}: Clock incremented to {self.clock}")

    def send(self):
        """Simulate sending a message, increasing the clock value."""
        self.clock += 1
        print(f"Process {self.process_id}: Sent message with clock {self.clock}")
        return self.clock

    def receive(self, received_clock):
        """
        Update the clock upon receiving a message.
        The clock becomes the maximum of the current clock or received clock + 1.
        """
        self.clock = max(self.clock, received_clock) + 1
        print(f"Process {self.process_id}: Received message and updated clock to {self.clock}")


# Example Usage
if __name__ == "__main__":
    # Instantiate clocks for two processes
    process_A = LamportClock("A")
    process_B = LamportClock("B")

    # Simulate events in process A
    process_A.increment()       # Internal event in A
    sent_clock = process_A.send()  # A sends a message

    # Simulate events in process B
    process_B.increment()       # Internal event in B
    process_B.receive(sent_clock)  # B receives the message from A

    # Another event in process A
    process_A.increment()

    # Process B sends a message to process A
    sent_clock = process_B.send()
    process_A.receive(sent_clock)  # A receives the message from B

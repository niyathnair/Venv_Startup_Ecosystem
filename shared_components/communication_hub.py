class CommunicationHub:
    def __init__(self):
        self.agents = {}
        self.message_logs = []
        self.message_queue = {}

    def register_agent(self, name, agent):
        """Register a new agent for communication."""
        if name not in self.agents:
            self.agents[name] = agent
            self.message_queue[name] = []
            print(f"[Info] Agent {name} registered successfully.")
        else:
            print(f"[Warning] Agent {name} is already registered.")

    def send_message(self, sender, recipient, message):
        """Send a direct message between agents."""
        if recipient in self.agents:
            self.agents[recipient].receive_message(sender, message)
            self.log_message(sender, recipient, message)
        else:
            print(f"[Error] Recipient {recipient} not found.")
            self.queue_message(recipient, message)  # Queue message if agent is not found

    def broadcast_message(self, sender, message):
        """Broadcast a message to all registered agents."""
        for recipient in self.agents.keys():
            self.send_message(sender, recipient, message)

    def log_message(self, sender, recipient, message):
        log_entry = {
            "sender": sender,
            "recipient": recipient,
            "message": message
        }
        self.message_logs.append(log_entry)
        print(f"[Log] Message sent from {sender} to {recipient}: {message}")

    def get_message_logs(self):
        """Retrieve all message logs."""
        return self.message_logs

    def queue_message(self, recipient, message):
        """Queue a message for offline agents."""
        if recipient not in self.message_queue:
            self.message_queue[recipient] = []  # Create queue if missing
        self.message_queue[recipient].append(message)
        print(f"[Queue] Message queued for {recipient}.")

    def fetch_queued_messages(self, recipient):
        """Fetch queued messages for a specific agent."""
        if recipient in self.message_queue:
            queued_messages = self.message_queue[recipient]
            self.message_queue[recipient] = []  # Clear the queue after fetching
            return queued_messages
        else:
            print(f"[Error] No message queue found for {recipient}.")
            return []

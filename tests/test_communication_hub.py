import pytest
import os
from shared_components.communication_hub import CommunicationHub

class MockAgent:
    def __init__(self, name):
        self.name = name
        self.received_messages = []

    def receive_message(self, sender, message):
        self.received_messages.append({"sender": sender, "message": message})

@pytest.fixture
def hub():
    return CommunicationHub()

@pytest.fixture
def agent_a():
    return MockAgent("AgentA")

@pytest.fixture
def agent_b():
    return MockAgent("AgentB")

def test_agent_registration(hub, agent_a, agent_b):
    hub.register_agent("AgentA", agent_a)
    hub.register_agent("AgentB", agent_b)
    assert "AgentA" in hub.agents
    assert "AgentB" in hub.agents

def test_send_message(hub, agent_a, agent_b):
    hub.register_agent("AgentA", agent_a)
    hub.register_agent("AgentB", agent_b)
    hub.send_message("AgentA", "AgentB", "Hello AgentB!")
    assert len(agent_b.received_messages) == 1
    assert agent_b.received_messages[0]["message"] == "Hello AgentB!"

def test_broadcast_message(hub, agent_a, agent_b):
    hub.register_agent("AgentA", agent_a)
    hub.register_agent("AgentB", agent_b)
    hub.broadcast_message("AgentA", "System Update")
    assert len(agent_a.received_messages) == 1
    assert len(agent_b.received_messages) == 1

def test_message_logging(hub, agent_a, agent_b):
    hub.register_agent("AgentA", agent_a)
    hub.register_agent("AgentB", agent_b)
    hub.send_message("AgentA", "AgentB", "Logging Test")
    logs = hub.get_message_logs()
    assert len(logs) == 1
    assert logs[0]["message"] == "Logging Test"

def test_message_queuing(hub):
    hub.queue_message("AgentB", "Queued Message")
    queued_messages = hub.fetch_queued_messages("AgentB")
    assert len(queued_messages) == 1
    assert queued_messages[0] == "Queued Message"

def test_invalid_recipient(hub, capsys):
    hub.send_message("AgentA", "UnknownAgent", "Hello?")
    captured = capsys.readouterr()
    assert "[Error] Recipient UnknownAgent not found." in captured.out

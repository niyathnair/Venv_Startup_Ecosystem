# tests/test_agents.py
import pytest
import time
from unittest.mock import patch
from shared_components.communication_hub import CommunicationHub
from agents.rag_agents.strategy_leadership.strategy_agent import StrategyLeadershipAgent
from agents.rag_agents.marketing_growth.marketing_agent import MarketingAgent

@pytest.fixture
def setup_agents():
    # Create a CommunicationHub and two agents
    hub = CommunicationHub()
    strategy_agent = StrategyLeadershipAgent("./data/knowledge_base/", hub)
    marketing_agent = MarketingAgent("./data/knowledge_base/", hub)

    # Register agents
    hub.register_agent("StrategyLeadershipAgent", strategy_agent)
    hub.register_agent("MarketingAgent", marketing_agent)

    yield hub, strategy_agent, marketing_agent

    # Cleanup thread after test if running
    if hasattr(marketing_agent, 'shutdown'):
        marketing_agent.shutdown()

@patch('random.uniform', return_value=80.0)  # Stable KPI values
@patch('time.sleep', return_value=None)      # No actual waiting
def test_marketing_agent_performance_update(mock_sleep, mock_rand, setup_agents):
    hub, strategy_agent, marketing_agent = setup_agents

    # Temporarily set a low update interval for quick tests
    marketing_agent.update_interval = 1

    # Manually trigger performance metrics update and sending data
    marketing_agent.update_performance_metrics()
    # Since all KPIs are 80, the performance score should be 80.
    # 80 is above the threshold (75), so it's a routine update
    # but we can still force sending an update:
    marketing_agent.send_performance_data_if_needed()

    # Since performance is above threshold, StrategyLeadershipAgent should reward (or at least record the update)
    # Check the strategy_agent's performance_records
    # The message handling in StrategyLeadershipAgent when receiving 'performance_update'
    # should store "MarketingAgent" in its performance_records.

    # Give a brief pause if needed (mocked sleep means no real wait, but let's call directly)
    # Normally, we rely on prints or direct data access. If StrategyLeadershipAgent updates performance_records immediately:
    assert "MarketingAgent" in strategy_agent.performance_records, "StrategyLeadershipAgent did not record MarketingAgent's performance."
    assert strategy_agent.performance_records["MarketingAgent"] == 80.0, "Performance score not recorded correctly."

@patch('random.uniform', return_value=60.0)  # Below threshold to trigger penalties
@patch('time.sleep', return_value=None)
def test_strategy_agent_responses(mock_sleep, mock_rand, setup_agents):
    hub, strategy_agent, marketing_agent = setup_agents

    marketing_agent.update_interval = 1

    # Update metrics (all 60, below threshold 75)
    marketing_agent.update_performance_metrics()
    marketing_agent.send_performance_data_if_needed()

    # If performance < 75, StrategyLeadershipAgent should send improvement plan and penalty
    # improvement_history should be updated
    assert "MarketingAgent" in strategy_agent.performance_records, "No performance record for MarketingAgent."
    assert strategy_agent.performance_records["MarketingAgent"] == 60.0, "Incorrect performance score recorded."
    assert "MarketingAgent" in strategy_agent.improvement_history, "No improvement plan logged."
    assert len(strategy_agent.improvement_history["MarketingAgent"]) > 0, "Improvement history not updated."

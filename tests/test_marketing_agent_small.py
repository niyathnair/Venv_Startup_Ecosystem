import pytest
from unittest.mock import MagicMock
from agents.rag_agents.marketing_growth.marketing_agent import MarketingAgent

@pytest.fixture
def marketing_agent():
    """Fixture for initializing the MarketingAgent."""
    return MarketingAgent("./data/knowledge_base/")

def test_run_marketing_campaign_success(marketing_agent):
    """Test successful marketing campaign execution."""
    # Mocking the retriever response
    marketing_agent.retriever.retrieve_trends = MagicMock(return_value={"trends": "Strong market growth expected"})

    # Execute the marketing campaign
    result = marketing_agent.run_marketing_campaign(
        product_info="SmartWidget",
        market_query="Wearable Technology Market Trends"
    )

    # Assertions
    assert isinstance(result, dict), "Result should be a dictionary."
    assert "market_trends" in result and result["market_trends"], "Market trends should be included."
    assert "campaign_message" in result and result["campaign_message"], "Campaign message should be generated."
    assert "optimized_message" in result and result["optimized_message"], "Optimized message should be returned."
    assert "campaign_score" in result and result["campaign_score"] > 0, "Campaign score should be positive."
    assert "social_media_ad" in result and result["social_media_ad"], "Social media ad should be generated."

def test_run_marketing_campaign_failure(marketing_agent):
    """Test marketing campaign failure handling."""
    # Mock the retriever to raise an error
    marketing_agent.retriever.retrieve_trends = MagicMock(side_effect=Exception("API Error"))

    # Execute the marketing campaign
    result = marketing_agent.run_marketing_campaign(
        product_info="SmartWidget",
        market_query="Wearable Technology Market Trends"
    )

    # Assertions
    assert isinstance(result, dict), "Result should be a dictionary."
    assert "error" in result, "Error key should be present on failure."
    assert "API Error" in result["error"], "Error message should be descriptive."

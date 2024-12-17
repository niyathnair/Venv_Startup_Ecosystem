import pytest
from unittest.mock import patch, MagicMock
from shared_components.communication_hub import CommunicationHub
from agents.rag_agents.marketing_growth.marketing_agent import MarketingAgent

# Fixture to set up the MarketingAgent
@pytest.fixture
def setup_agents():
    hub = CommunicationHub()
    marketing_agent = MarketingAgent("./data/knowledge_base/")
    hub.register_agent("MarketingAgent", marketing_agent)
    yield hub, marketing_agent

# Test 1: Run a full marketing campaign
@patch('agents.rag_agents.marketing_growth.marketing_agent.MarketingRetriever.retrieve_trends', return_value={"trends": "Positive"})
@patch('agents.rag_agents.marketing_growth.marketing_agent.CampaignModel.generate_message', return_value="Exciting Campaign Message")
@patch('agents.rag_agents.marketing_growth.marketing_agent.CampaignModel.score_campaign', return_value=85)
@patch('agents.rag_agents.marketing_growth.marketing_agent.CampaignModel.optimize_campaign_language', return_value="Optimized Message")
@patch('agents.rag_agents.marketing_growth.marketing_agent.CampaignModel.generate_social_media_ad', return_value="Cool Ad")
def test_run_marketing_campaign(mock_trends, mock_message, mock_score, mock_optimize, mock_ad, setup_agents):
    hub, marketing_agent = setup_agents

    product_info = "Next-Gen Smartphone"
    market_query = "smartphone market trends"

    result = marketing_agent.run_marketing_campaign(product_info, market_query)

    assert result, "Campaign result should not be empty."
    assert "market_trends" in result and result["market_trends"], "Market trends should be included."
    assert "campaign_message" in result and result["campaign_message"], "Campaign message should be generated."
    assert "optimized_message" in result and result["optimized_message"], "Optimized message should be returned."
    assert "campaign_score" in result and result["campaign_score"] > 0, "Campaign score should be positive."

# Test 2: Analyze Market and Competitors
@patch('agents.rag_agents.marketing_growth.marketing_agent.MarketAnalyzer.analyze_trends', return_value={"trends": "Upward"})
@patch('agents.rag_agents.marketing_growth.marketing_agent.MarketingRetriever.retrieve_competitor_data', return_value={"competitors": ["Competitor A", "Competitor B"]})
def test_analyze_market_and_competitors(mock_trends, mock_competitors, setup_agents):
    hub, marketing_agent = setup_agents

    market_query = "smartphone market competitors"

    result = marketing_agent.analyze_market_and_competitors(market_query)

    assert result, "Analysis result should not be empty."
    assert "market_trends" in result and result["market_trends"], "Market trends should be analyzed."
    assert "competitor_data" in result and result["competitor_data"], "Competitor data should be retrieved."

# Test 3: Optimize Campaign
@patch('agents.rag_agents.marketing_growth.marketing_agent.CampaignOptimizer.suggest_improvements', return_value=["Better targeting"])
@patch('agents.rag_agents.marketing_growth.marketing_agent.CampaignOptimizer.optimize_budget', return_value=12000)
def test_optimize_campaign(mock_improvements, mock_budget, setup_agents):
    hub, marketing_agent = setup_agents

    campaign_data = {
        "campaign": "Smartphone Launch Campaign",
        "current_budget": 10000,
        "performance_metrics": {
            "engagement_rate": 90,
            "roi": 150
        }
    }

    result = marketing_agent.optimize_campaign(campaign_data)

    assert result, "Optimization result should not be empty."
    assert "suggestions" in result and result["suggestions"], "Improvement suggestions should be provided."
    assert "new_budget" in result and result["new_budget"] > 10000, "Budget should increase with strong performance."

# Test 4: Fetch Campaign Insights
@patch('agents.rag_agents.marketing_growth.marketing_agent.MarketingRetriever.fetch_marketing_insights', return_value={"marketing_insights": "Deep Insight"})
def test_fetch_campaign_insights(mock_insights, setup_agents):
    hub, marketing_agent = setup_agents

    topic = "AI in marketing"

    result = marketing_agent.fetch_campaign_insights(topic)

    assert result, "Insights result should not be empty."
    assert "marketing_insights" in result and result["marketing_insights"], "Marketing insights should be returned."

# Test 5: Evaluate Campaign Performance
@patch('agents.rag_agents.marketing_growth.marketing_agent.CampaignOptimizer.evaluate_campaign_performance', return_value=[{"summary": "Excellent results"}])
def test_evaluate_campaign_performance(mock_performance, setup_agents):
    hub, marketing_agent = setup_agents

    campaign_name = "Smartphone Launch Campaign"

    result = marketing_agent.evaluate_campaign_performance(campaign_name)

    assert result, "Performance evaluation result should not be empty."
    assert "performance_summary" in result and isinstance(result["performance_summary"], list), "Summary should be a list."

# from shared_components.communication_hub import CommunicationHub
# from agents.rag_agents.marketing_growth.marketing_agent import MarketingAgent
# from agents.rag_agents.strategy_leadership.strategy_agent import StrategyLeadershipAgent
# from agents.rag_agents.customer_support.customer_support_agent import CustomerSupportAgent
# from agents.rag_agents.finance_legal.finance_agent import FinanceLegalAgent
# from agents.rag_agents.sales_business.sales_agent import SalesBusinessAgent
# from agents.rag_agents.pitching.pitching_agent import PitchingAgent
# from agents.rag_agents.data_analytics.data_agent import DataAnalyticsAgent
# from reportlab.lib.pagesizes import letter
# from reportlab.lib import colors
# from reportlab.lib.styles import getSampleStyleSheet
# from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

# def generate_pitch_report(pitching_info, business_data, marketing_results):
#     pdf_file = "business_pitch_report.pdf"
#     doc = SimpleDocTemplate(pdf_file, pagesize=letter)
#     styles = getSampleStyleSheet()

#     title_style = styles['Title']
#     header_style = styles['Heading2']
#     normal_style = styles['BodyText']

#     content = [
#         Paragraph("Business Pitch Report", title_style),
#         Spacer(1, 20),

#         Paragraph("Brand Overview", header_style),
#         Spacer(1, 12),
#         Paragraph(f"<b>Brand Name:</b> {pitching_info.get('brand_name', 'Unknown')}", normal_style),
#         Paragraph(f"<b>Industry:</b> {pitching_info.get('target_market', 'N/A')}", normal_style),
#         Paragraph(f"<b>Tagline:</b> {pitching_info.get('tagline', 'N/A')}", normal_style),
#         Spacer(1, 12),

#         Paragraph("Marketing Campaign Results", header_style),
#         Spacer(1, 12),
#     ]

#     if isinstance(marketing_results, dict):
#         content.extend([
#             Paragraph(f"<b>Market Trends:</b> {marketing_results.get('market_trends', {}).get('trends', 'N/A')}", normal_style),
#             Paragraph(f"<b>Campaign Message:</b> {marketing_results.get('campaign_message', 'N/A')}", normal_style),
#             Paragraph(f"<b>Optimized Message:</b> {marketing_results.get('optimized_message', 'N/A')}", normal_style),
#             Paragraph(f"<b>Campaign Score:</b> {marketing_results.get('campaign_score', 'N/A')}", normal_style),
#             Paragraph(f"<b>Social Media Ad:</b> {marketing_results.get('social_media_ad', 'N/A')}", normal_style),
#         ])
#     else:
#         content.extend([
#             Paragraph("<b>Market Trends:</b> N/A", normal_style),
#             Paragraph("<b>Campaign Message:</b> N/A", normal_style),
#             Paragraph("<b>Optimized Message:</b> N/A", normal_style),
#             Paragraph("<b>Campaign Score:</b> N/A", normal_style),
#             Paragraph("<b>Social Media Ad:</b> N/A", normal_style),
#         ])

#     content.append(Spacer(1, 12))
#     content.append(Paragraph("Business Performance Overview", header_style))
#     content.append(Spacer(1, 12))

#     table_data = [["Department", "Performance Score", "Key Insights"]]
#     for entry in business_data:
#         table_data.append([
#             entry.get('department', 'N/A'),
#             entry.get('performance_score', 'N/A'),
#             entry.get('insights', 'N/A')
#         ])

#     table = Table(table_data, colWidths=[150, 150, 250])
#     table.setStyle(TableStyle([
#         ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
#         ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
#         ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
#         ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
#         ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
#         ('GRID', (0, 0), (-1, -1), 1, colors.black),
#         ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
#     ]))

#     content.append(table)
#     content.append(Spacer(1, 12))

#     doc.build(content)
#     print(f"PDF report generated: {pdf_file}")


# def main():
#     hub = CommunicationHub()

#     strategy_agent = StrategyLeadershipAgent("./data/knowledge_base/", hub)
#     marketing_agent = MarketingAgent("./data/knowledge_base/", hub)
#     data_analytics_agent = DataAnalyticsAgent("./data/knowledge_base/", hub)
#     customer_support_agent = CustomerSupportAgent("./data/knowledge_base/", hub)
#     finance_legal_agent = FinanceLegalAgent("./data/knowledge_base/", hub)
#     sales_business_agent = SalesBusinessAgent("./data/knowledge_base/", hub)
#     pitching_agent = PitchingAgent("./data/knowledge_base/", hub)

#     hub.register_agent("StrategyLeadershipAgent", strategy_agent)
#     hub.register_agent("MarketingAgent", marketing_agent)
#     hub.register_agent("DataAnalyticsAgent", data_analytics_agent)
#     hub.register_agent("CustomerSupportAgent", customer_support_agent)
#     hub.register_agent("FinanceLegalAgent", finance_legal_agent)
#     hub.register_agent("SalesBusinessAgent", sales_business_agent)
#     hub.register_agent("PitchingAgent", pitching_agent)

#     pitching_info = pitching_agent.generate_pitch(
#         brand_name="SmartWidget",
#         target_market="Wearable Technology",
#         product_features=["Heart Rate Monitoring", "Sleep Tracking", "GPS Navigation"]
#     )

#     marketing_results = marketing_agent.run_marketing_campaign(
#         product_info="SmartWidget",
#         market_query="Wearable Technology Market Trends"
#     )

#     business_data = [
#         {"department": "MarketingAgent", "performance_score": 85, "insights": "Strong market engagement."},
#         {"department": "SalesBusinessAgent", "performance_score": 90, "insights": "Excellent sales growth."},
#         {"department": "CustomerSupportAgent", "performance_score": 80, "insights": "Good customer satisfaction."},
#         {"department": "FinanceLegalAgent", "performance_score": 92, "insights": "Outstanding financial compliance."}
#     ]

#     generate_pitch_report(pitching_info, business_data, marketing_results)

# if __name__ == "__main__":
#     main()
# from shared_components.communication_hub import CommunicationHub
# from agents.rag_agents.marketing_growth.marketing_agent import MarketingAgent
# import json

# def main():
#     hub = CommunicationHub()

#     # Initialize and Register Marketing Agent
#     marketing_agent = MarketingAgent("./data/knowledge_base/", hub)
#     hub.register_agent("MarketingAgent", marketing_agent)

#     # Set a limit on response size
#     try:
#         marketing_results = marketing_agent.run_marketing_campaign(
#             product_info="SmartWidget",
#             market_query="Wearable Technology Market Trends"
#         )

#         # Limit the response to essential fields with a 5-word constraint
#         def limit_words(text, word_limit=5):
#             return ' '.join(text.split()[:word_limit]) if isinstance(text, str) else "N/A"

#         limited_results = {
#             "market_trends": limit_words(marketing_results.get("market_trends", {}).get("trends", "N/A")),
#             "campaign_message": limit_words(marketing_results.get("campaign_message", "N/A")),
#             "optimized_message": limit_words(marketing_results.get("optimized_message", "N/A")),
#             "campaign_score": marketing_results.get("campaign_score", "N/A"),
#             "social_media_ad": limit_words(marketing_results.get("social_media_ad", "N/A"))
#         }

#         # Return results as JSON
#         print(json.dumps(limited_results, indent=4))
#     except Exception as e:
#         print(json.dumps({"error": str(e)}, indent=4))

# if __name__ == "__main__":
#     main()
############################################################################################################
# from shared_components.communication_hub import CommunicationHub
# from agents.rag_agents.marketing_growth.marketing_agent import MarketingAgent
# import json

# def main():
#     hub = CommunicationHub()

#     # Initialize and Register Marketing Agent
#     marketing_agent = MarketingAgent("./data/knowledge_base/", hub)
#     hub.register_agent("MarketingAgent", marketing_agent)

#     # Set a limit on response size
#     try:
#         # Mocked results to simulate API response
#         marketing_results = {
#             "market_trends": {"trends": "Growing demand in wearable tech"},
#             "campaign_message": "Launch SmartWidget for better health!",
#             "optimized_message": "Revolutionize health with SmartWidget!",
#             "campaign_score": 92,
#             "social_media_ad": "Discover SmartWidget: Track your fitness!"
#         }

#         # Limit the response to essential fields with a 5-word constraint
#         def limit_words(text, word_limit=5):
#             return ' '.join(text.split()[:word_limit]) if isinstance(text, str) else "N/A"

#         limited_results = {
#             "market_trends": limit_words(marketing_results.get("market_trends", {}).get("trends", "N/A")),
#             "campaign_message": limit_words(marketing_results.get("campaign_message", "N/A")),
#             "optimized_message": limit_words(marketing_results.get("optimized_message", "N/A")),
#             "campaign_score": marketing_results.get("campaign_score", "N/A"),
#             "social_media_ad": limit_words(marketing_results.get("social_media_ad", "N/A"))
#         }

#         # Return results as JSON
#         print(json.dumps(limited_results, indent=4))
#     except Exception as e:
#         print(json.dumps({"error": str(e)}, indent=4))

# if __name__ == "__main__":
#     main()
############################################################################################################
from shared_components.communication_hub import CommunicationHub
from agents.rag_agents.marketing_growth.marketing_agent import MarketingAgent
from agents.rag_agents.pitching.pitching_agent import PitchingAgent
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
import json

def generate_pitch_report(pitching_info, marketing_results, competitor_data, market_trends_overview):
    pdf_file = "business_pitch_report.pdf"
    doc = SimpleDocTemplate(pdf_file, pagesize=letter)
    styles = getSampleStyleSheet()

    title_style = styles['Title']
    header_style = styles['Heading2']
    normal_style = styles['BodyText']

    content = [
        Paragraph("Business Pitch Report", title_style),
        Spacer(1, 20),

        Paragraph("Brand Overview", header_style),
        Spacer(1, 12),
        Paragraph(f"<b>Brand Name:</b> {pitching_info.get('brand_name', 'Unknown')}", normal_style),
        Paragraph(f"<b>Industry:</b> {pitching_info.get('target_market', 'N/A')}", normal_style),
        Paragraph(f"<b>Tagline:</b> {pitching_info.get('tagline', 'N/A')}", normal_style),
        Spacer(1, 12),

        Paragraph("Marketing Campaign Results", header_style),
        Spacer(1, 12),
    ]

    if isinstance(marketing_results, dict):
        content.extend([
            Paragraph(f"<b>Market Trends:</b> {marketing_results.get('market_trends', 'N/A')}", normal_style),
            Paragraph(f"<b>Campaign Message:</b> {marketing_results.get('campaign_message', 'N/A')}", normal_style),
            Paragraph(f"<b>Optimized Message:</b> {marketing_results.get('optimized_message', 'N/A')}", normal_style),
            Paragraph(f"<b>Campaign Score:</b> {marketing_results.get('campaign_score', 'N/A')}", normal_style),
            Paragraph(f"<b>Social Media Ad:</b> {marketing_results.get('social_media_ad', 'N/A')}", normal_style),
        ])

    content.append(Spacer(1, 12))
    content.append(Paragraph("Market Trends Overview", header_style))
    content.append(Spacer(1, 12))
    content.append(Paragraph(market_trends_overview, normal_style))

    content.append(Spacer(1, 12))
    content.append(Paragraph("Competitor Analysis", header_style))
    content.append(Spacer(1, 12))

    table_data = [["Competitor Name", "Strengths", "Weaknesses"]]
    for competitor in competitor_data:
        table_data.append([
            competitor.get('name', 'N/A'),
            competitor.get('strengths', 'N/A'),
            competitor.get('weaknesses', 'N/A')
        ])

    table = Table(table_data, colWidths=[150, 150, 250])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ]))

    content.append(table)
    doc.build(content)
    print(f"PDF report generated: {pdf_file}")

def main():
    hub = CommunicationHub()

    # Initialize and Register Agents
    marketing_agent = MarketingAgent("./data/knowledge_base/", hub)
    pitching_agent = PitchingAgent("./data/knowledge_base/", hub)
    hub.register_agent("MarketingAgent", marketing_agent)
    hub.register_agent("PitchingAgent", pitching_agent)

    try:
        # Mocked Marketing Results
        marketing_results = {
            "market_trends": "Growing demand in wearable tech",
            "campaign_message": "Launch SmartWidget for better health!",
            "optimized_message": "Revolutionize health with SmartWidget!",
            "campaign_score": 92,
            "social_media_ad": "Discover SmartWidget: Track your fitness!"
        }

        pitching_info = pitching_agent.generate_pitch(
            brand_name="SmartWidget",
            target_market="Wearable Technology",
            product_features=["Heart Rate Monitoring", "Sleep Tracking", "GPS Navigation"]
        )

        competitor_data = [
            {"name": "FitTech", "strengths": "Established brand", "weaknesses": "Limited product range"},
            {"name": "WellnessPro", "strengths": "Advanced tech", "weaknesses": "High pricing"}
        ]

        market_trends_overview = (
            "The wearable technology market is evolving rapidly due to health and fitness awareness, technological advances, and increased consumer demand."
        )

        # Limit the response to essential fields with a 5-word constraint
        def limit_words(text, word_limit=5):
            return ' '.join(text.split()[:word_limit]) if isinstance(text, str) else "N/A"

        limited_results = {
            "market_trends": limit_words(marketing_results["market_trends"]),
            "campaign_message": limit_words(marketing_results["campaign_message"]),
            "optimized_message": limit_words(marketing_results["optimized_message"]),
            "campaign_score": marketing_results["campaign_score"],
            "social_media_ad": limit_words(marketing_results["social_media_ad"])
        }

        # Return results as JSON
        print(json.dumps(limited_results, indent=4))
        generate_pitch_report(pitching_info, limited_results, competitor_data, market_trends_overview)

    except Exception as e:
        print(json.dumps({"error": str(e)}, indent=4))

if __name__ == "__main__":
    main()

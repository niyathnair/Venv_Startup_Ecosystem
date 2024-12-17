class LeadModel:
    def score_leads(self, lead_data):
        scored_leads = [lead for lead in lead_data if lead['score'] >= 75]
        return scored_leads

    def forecast_sales(self, current_leads):
        forecast = sum(lead['estimated_value'] for lead in current_leads)
        return forecast

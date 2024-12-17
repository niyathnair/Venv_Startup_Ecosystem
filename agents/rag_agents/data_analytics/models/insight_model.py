class InsightModel:
    def generate_insights(self, data):
        insights = {
            "average_value": sum(d['value'] for d in data) / len(data),
            "top_records": sorted(data, key=lambda x: x['value'], reverse=True)[:5]
        }
        return insights

    def forecast_trends(self, historical_data):
        trend_forecast = [
            {
                "period": record['period'],
                "forecast": record['value'] * 1.1  # Assuming 10% growth
            }
            for record in historical_data
        ]
        return trend_forecast
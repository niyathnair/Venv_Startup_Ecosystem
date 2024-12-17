class FinancialAnalyzer:
    def analyze_financial_records(self, records):
        net_worth = sum(record['asset_value'] - record['liability'] for record in records)
        return {
            "net_worth": net_worth,
            "liabilities": sum(record['liability'] for record in records),
            "assets": sum(record['asset_value'] for record in records)
        }

    def generate_financial_summary(self, records):
        summary = {
            "total_revenue": sum(record['revenue'] for record in records),
            "total_expenses": sum(record['expenses'] for record in records),
            "net_profit": sum(record['revenue'] - record['expenses'] for record in records)
        }
        return summary
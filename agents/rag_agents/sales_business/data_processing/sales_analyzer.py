class SalesAnalyzer:
    def analyze_sales(self, sales_data):
        total_revenue = sum(item['price'] * item['quantity'] for item in sales_data)
        total_units = sum(item['quantity'] for item in sales_data)
        return {
            "total_revenue": total_revenue,
            "total_units_sold": total_units
        }

    def sales_trends(self, sales_data):
        high_performers = [item for item in sales_data if item['quantity'] > 100]
        return high_performers

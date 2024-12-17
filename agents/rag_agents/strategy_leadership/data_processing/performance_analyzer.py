class PerformanceAnalyzer:
    def evaluate_performance(self, performance_data):
        evaluated_data = [record for record in performance_data if record['performance_score'] >= 80]
        return evaluated_data

    def generate_performance_summary(self, performance_data):
        average_score = sum(record['performance_score'] for record in performance_data) / len(performance_data)
        summary = {
            "average_score": average_score,
            "top_performers": [record for record in performance_data if record['performance_score'] > 90]
        }
        return summary
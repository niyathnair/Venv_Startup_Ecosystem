class ComplianceModel:
    def verify_compliance(self, financial_data):
        violations = []
        for record in financial_data:
            if record['tax_paid'] < record['required_tax']:
                violations.append({
                    "record_id": record['id'],
                    "violation": "Underpaid taxes"
                })
            if not record['audit_status']:
                violations.append({
                    "record_id": record['id'],
                    "violation": "Missing audit certification"
                })
        return violations
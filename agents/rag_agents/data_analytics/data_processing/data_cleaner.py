class DataCleaner:
    def clean_data(self, raw_data):
        cleaned_data = [record for record in raw_data if record['valid']]
        return cleaned_data

    def normalize_data(self, data):
        normalized_data = [{**record, 'value': record['value'] / 100} for record in data]
        return normalized_data
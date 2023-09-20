
import pandas as pd
from tensorflow.keras.models import load_model

class CompanyIdentifier:
    def __init__(self):
        self.model = load_model('../models/company_identification_model.h5')

    def identify_companies(self, sector):
        data = pd.read_csv('../data/companies.csv')
        sector_data = data[data['sector'] == sector]
        sector_data['score'] = self.model.predict(sector_data.drop('company_name', axis=1))
        top_companies = sector_data.sort_values('score', ascending=False).head(10)
        return top_companies['company_name'].tolist()

if __name__ == "__main__":
    identifier = CompanyIdentifier()
    print(identifier.identify_companies('Technology'))

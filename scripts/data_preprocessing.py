
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def preprocess_data(data):
    scaler = MinMaxScaler()
    for column in data.columns:
        if data[column].dtype == 'float64':
            data[column] = scaler.fit_transform(data[column].values.reshape(-1,1))
    return data

if __name__ == "__main__":
    leads_data = load_data('../data/leads.csv')
    companies_data = load_data('../data/companies.csv')

    leads_data = preprocess_data(leads_data)
    companies_data = preprocess_data(companies_data)

    leads_data.to_csv('../data/leads.csv', index=False)
    companies_data.to_csv('../data/companies.csv', index=False)

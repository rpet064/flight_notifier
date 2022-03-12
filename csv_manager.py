from countryinfo import CountryInfo
import pandas as pd


class CSVManager:
    def __init__(self, pod, name, destinations, country_name, file_name):
        self.POD = pod
        self.name = name
        self.destinations = destinations
        self.country_name = country_name
        self.country = CountryInfo(self.country_name)
        self.currency_array = self.country.currencies()
        self.currency = self.currency_array[0]
        self.file_name = file_name
        self.create_csv()

    def create_csv(self):
        # creates and inputs csv from user input
        self.data = {"Categories": ["name", "country", "departure", "destinations", "currency"],
                     "details": [self.name, self.POD, self.country_name, self.destinations, self.currency]
                     }
        self.details_df = pd.DataFrame(self.data)
        self.details_df.to_csv(self.file_name, index=False)

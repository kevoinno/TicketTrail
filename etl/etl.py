from extract import extract_event
from transform import transform_event
import os
from dotenv import load_dotenv

def main():
    # load in API key
    load_dotenv()
    API_KEY = os.getenv("CONSUMER_KEY")

    # extract events
    events_data_json = extract_event(API_KEY, "Crypto Arena")

    # transform
    venues, events, ticket_prices = transform_event(API_KEY, events_data_json)

    print(venues.head())
    print('\n')
    print(events.head())
    print('\n')
    print(ticket_prices.head())
    print('\n')
    

if __name__ == "__main__":
    main()

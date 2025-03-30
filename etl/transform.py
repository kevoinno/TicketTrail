"""
Transforms data from JSON to a dataframe to be prepared to load into database
"""

import pandas as pd
from datetime import datetime
import pytz

def transform_event(api_key, events):
    """
    Args:
        api_key 
        events = json object of events from API call

    Turns events json into a pandas dataframe
    """
    events_list = []
    venues_list = []
    ticket_prices_list = []

    print(f"Events to process: ", len(events['_embedded']['events']))
    for e in events['_embedded']['events']:
        # venues
        venue_id = e['_embedded']['venues'][0]['id']
        venue_name = e['_embedded']['venues'][0]['name']
        address = e['_embedded']['venues'][0]['address']['line1']
        city =  e['_embedded']['venues'][0]['city']['name']
        state = e['_embedded']['venues'][0]['state']['stateCode']
        country = e['_embedded']['venues'][0]['country']['countryCode']
        
        # events
        event_id = e['id']
        event_name = e['name']
        event_date = e['dates']['start']['dateTime']
        url = e.get('url', None)

        # ticket_prices
        snapshot_time = datetime.now(pytz.UTC)
        if e.get('priceRanges', None):
            min_price = e['priceRanges'][0]['min']
            max_price =  e['priceRanges'][0]['max']
            currency = e['priceRanges'][0]['currency']
        else:
            min_price = max_price = currency = None
        # create dictionaries to add to lists
        venues_dict = {
            'venue_id' : venue_id,
            'name' : venue_name,
            'address' : address,
            'city' : city,
            'state' : state,
            'country' : country
        }

        events_dict = {
            'event_id': event_id,
            'venue_id': venue_id,  
            'name': event_name,
            'event_date': event_date,
            'ticketmaster_url': url
        }

        ticket_prices_dict = {
            # Note: price_id is SERIAL, so we don't include it
            'event_id': event_id,  
            'snapshot_time': snapshot_time,
            'min_price': min_price,
            'max_price': max_price,
            'currency': currency
        }

        # add to lists
        venues_list.append(venues_dict)
        events_list.append(events_dict)
        ticket_prices_list.append(ticket_prices_dict)

    # convert to pandas dataframes
    venues_df = pd.DataFrame(venues_list)
    events_df = pd.DataFrame(events_list)
    ticket_prices_df = pd.DataFrame(ticket_prices_list)

    return venues_df, events_df, ticket_prices_df
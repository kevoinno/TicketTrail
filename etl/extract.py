"""
Extracts data using the Ticketmaster API, returning a JSON output
"""

import os
import json
import requests

def extract_event(api_key, keyword):
    """
    Args:
        api_key 
        keyword = keyword to search for event (e.g. a venue name)
    Extracts events from a specific venue using the Ticketmaster API
    """
    url = f"https://app.ticketmaster.com/discovery/v2/events.json?apikey={api_key}"
    
    repsonse = requests.get(url, params={"keyword" : keyword})
    json_reponse = repsonse.json()
    # Code to see output (DELETE LATER)
    json_object = json.dumps(json_reponse, indent = 4)

    # Code to see output (DELETE LATER)
    with open("sample_output.json", "w") as f:
        f.write(json_object)
    return json_reponse
                            
                            
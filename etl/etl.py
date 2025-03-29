from extract import extract_event
import os
from dotenv import load_dotenv

def main():
    # load in API key
    load_dotenv()
    API_KEY = os.getenv("CONSUMER_KEY")
    # extract events
    events = extract_event(API_KEY, "Crypto Arena")

if __name__ == "__main__":
    main()

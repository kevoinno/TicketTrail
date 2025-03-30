import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

# connection
try:
    conn = psycopg2.connect(dbname = os.getenv("POSTGRESQL_DBNAME"), user = os.getenv("POSTGRESQL_USER"), password = os.getenv("POSTGRESQL_PASSWORD"), host = os.getenv("POSTGRESQL_HOST"), port = os.getenv("POSTGRESQL_PORT"))
    # cursor
    with conn.cursor() as cur:
        # create tables
        
        # venues table
        cur.execute("""CREATE TABLE IF NOT EXISTS venues (
                        venue_id VARCHAR(255) PRIMARY KEY,
                        name VARCHAR(255),
                        address VARCHAR(255),
                        city VARCHAR(255),
                        state VARCHAR(255),
                        country VARCHAR(255)
                    );
                    """)
        
        # events table
        cur.execute("""CREATE TABLE IF NOT EXISTS events (
                        event_id VARCHAR(255) PRIMARY KEY,
                        venue_id VARCHAR(255) REFERENCES venues(venue_id),
                        name VARCHAR(255),
                        event_date TIMESTAMPTZ,
                        ticketmaster_url VARCHAR(255),
                        created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
                    );
                    """)
        
        # ticket_prices table
        cur.execute("""CREATE TABLE IF NOT EXISTS ticket_prices (
                        price_id SERIAL PRIMARY KEY,
                        event_id VARCHAR(255) REFERENCES events(event_id),
                        snapshot_time TIMESTAMPTZ,
                        min_price DECIMAL(10, 2),
                        max_price DECIMAL(10, 2),
                        currency VARCHAR(3),
                        created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
                    );
                    """)
                    
        # forecast results
        cur.execute("""CREATE TABLE IF NOT EXISTS forecast_results (
                        forecast_id SERIAL PRIMARY KEY,
                        event_id VARCHAR(255) REFERENCES events(event_id),
                        forecast_date TIMESTAMPTZ,
                        pred_min_price DECIMAL(10, 2),
                        pred_max_price DECIMAL(10, 2),
                        confidence_interval NUMRANGE,
                        created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
                    );
                    """)
    conn.commit()
    
    conn.close()
    print("Database created successfully")
except Exception as e:
    print(f"Error connecting to database: {e}")
    


# TicketTrail

## 1. Overview
A web application that collects, stores, and visualizes historical ticket pricing data for events at Crypto Arena, LA. Users can search for events and view historical price charts along with basic time series forecasting.

## 2. Goals and Objectives
- **Data Transparency**: Provide public access to historical ticket pricing information
- **User Insight**: Help users make informed decisions with historical trends and basic forecasts
- **Simplicity**: Develop a straightforward MVP focused on core functionalities

## 3. Scope

### In Scope
- **Event Tracking**: Monitor ticket events exclusively at Crypto Arena, LA
- **Data Pipeline**: Automated ETL process using GitHub Actions
- **Database**: PostgreSQL for data storage
- **Web Application**: Streamlit app with:
  - Event search
  - Historical price charts
  - Basic time series forecasts

### Out of Scope
- Expansion to other venues/event types
- Advanced error notifications
- Complex user account management
- Highly optimized database performance

## 4. Functional Requirements

### 4.1 Data Collection & ETL Pipeline
- **Data Source**: Ticketmaster API
- **Target Venue**: Crypto Arena, LA
- **Collected Data**:
  - Event details (name, date, time, venue)
  - Ticket price ranges
  - Timestamped price snapshots
- **Pipeline Approach**:
  - GitHub Actions for automation
  - Daily data pulls
  - Simple ETL process

### 4.2 Web Application (Streamlit)
- **Search Functionality**: Search by event name, date
- **Data Visualization**: 
  - Historical price charts
  - Summary statistics
- **Time Series Forecasting**:
  - Basic forecasting model (ARIMA/Prophet)
  - Forecast visualization
- **User Interface**:
  - Clean, straightforward design
  - Desktop and mobile responsive

## 5. Non-Functional Requirements
- **Performance**: Efficient ETL and quick web responses
- **Reliability**: Basic data integrity
- **Simplicity**: Core functionalities only
- **Security**: Secure credential management

## 6. Technical Architecture

### 6.1 Data Layer
- PostgreSQL Database with simple schema

#### Database Schema

##### 1. venues
Purpose: Store details about event venues
- _venues_(_venue_id_, name, address, city, state, country, created_at)

##### 2. events
Purpose: Record information about individual events
- _events_(_event_id_, venue_id, name, event_date, ticketmaster_url, created_at)
  - venue_id references venues(venue_id)

##### 3. ticket_prices
Purpose: Track historical ticket pricing snapshots
- _ticket_prices_(_price_id_, event_id, snapshot_time, min_price, max_price, currency, created_at)
  - event_id references events(event_id)

##### 4. forecast_results (Optional)
Purpose: Store time series forecasting results
- _forecast_results_(_forecast_id_, event_id, forecast_date, pred_min_price, pred_max_price, confidence_interval, created_at)
  - event_id references events(event_id)

### 6.2 ETL Pipeline
- GitHub Actions for scheduling
- Python scripts for ETL
- Minimal monitoring

### 6.3 Application Layer
- Streamlit web interface
- PostgreSQL integration
- Python visualization libraries

## 7. Future Enhancements
- Additional venues/event types
- Advanced forecasting models
- Enhanced UI features
- Mobile app development



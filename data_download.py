import gdown

# Download the traffic data
gdown.download('https://drive.google.com/1--VLwDi2HPZVzFJ5ZJv3g2XbsryrnshG', 'cleaned_traffic_nyc.csv', quiet=False)

# Download the EV station data (USA)
gdown.download('https://drive.google.com/1B8Pw46JHEcfzxqeuMiiCO5FV06H16Wm4', 'cleaned_ev_usa.csv', quiet=False)

# Download the EV station data (Germany)
gdown.download('https://drive.google.com/your_google_drive_link_for_ev_germany_data', 'ev_charging_stations_germany_cleaned.csv', quiet=False)

CREATE TABLE car_grades (
  id SERIAL PRIMARY KEY,
  description VARCHAR(50) NOT NULL,
  per_mileage_rate DECIMAL(5,2) NOT NULL
);

INSERT INTO car_grades VALUES
(DEFAULT, 'Standard', 2.20),
(DEFAULT, 'Premium', 2.54),
(DEFAULT, 'Executive', 3.25);


CREATE TABLE pickup_locations (
  id SERIAL PRIMARY KEY,
  iata_id VARCHAR(3) NOT NULL,
  location_name VARCHAR(50) NOT NULL
);

INSERT INTO pickup_locations VALUES 
(DEFAULT, 'LHR', 'London Heathrow'),
(DEFAULT, 'LGW', 'London Gatwick'),
(DEFAULT, 'MAN', 'Manchester'),
(DEFAULT, 'STN', 'Stansted'),
(DEFAULT, 'BHX', 'Birmingham International Airport'),
(DEFAULT, 'GLA', 'Glasgow International'),
(DEFAULT, 'EDI', 'Edinburgh'),
(DEFAULT, 'LTN', 'London Luton'),
(DEFAULT, 'BFS', 'Aldergrove International Airport'),
(DEFAULT, 'BRS', 'Bristol');

CREATE TABLE reservations (
  id SERIAL PRIMARY KEY,
  reservation_tstamp TIMESTAMP NOT NULL DEFAULT now(),
  customer_name VARCHAR(60) NOT NULL,
  pickup_id INT NOT NULL,
  pickup_datetime TIMESTAMP NOT NULL CHECK (pickup_datetime > now()),
  cargrade_id INT NOT NULL,
  distance_miles DECIMAL(7,2) NOT NULL CHECK (distance_miles > 0),
  FOREIGN KEY (pickup_id) REFERENCES pickup_locations (id),
  FOREIGN KEY (cargrade_id) REFERENCES car_grades (id)
);

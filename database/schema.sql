CREATE TABLE production (
    production_id BIGSERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL,
    line_id VARCHAR(10),
    machine_id VARCHAR(20),
    product_id VARCHAR(20),
    cycle_time NUMERIC(6,2),
    temperature NUMERIC(6,2),
    pressure NUMERIC(6,2),
    production_time NUMERIC(6,2),
    defect BOOLEAN,
    defect_type VARCHAR(50),
    energy_consumption NUMERIC(8,2)
);
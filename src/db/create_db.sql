-- crée la BDD (exécuté par un superuser ou via psql)
-- psql postgres
-- psql -U postgres -f src/db/create_db.sql

CREATE DATABASE dbfuturisys;

-- Connect to dbfuturisys then run below to create tables:
-- Tables for requests/predictions
CREATE TABLE IF NOT EXISTS predictions (
    id SERIAL PRIMARY KEY,
    request_id UUID NOT NULL DEFAULT gen_random_uuid(),
    model_version TEXT,
    input_json JSONB,
    prediction_json JSONB,
    latency_ms INTEGER,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT now()
);

CREATE TABLE IF NOT EXISTS requests (
    id SERIAL PRIMARY KEY,
    request_id UUID NOT NULL,
    user_id TEXT,
    payload JSONB,
    response JSONB,
    status_code INTEGER,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT now()
);

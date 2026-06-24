-- Dimensions Tables
CREATE TABLE IF NOT EXISTS dim_fund (
    scheme_code INTEGER PRIMARY KEY,
    scheme_name TEXT,
    fund_house TEXT
);

-- Fact Tables (Star Schema Structure)
CREATE TABLE IF NOT EXISTS fact_nav (
    scheme_code INTEGER,
    date TEXT,
    nav REAL,
    PRIMARY KEY (scheme_code, date),
    FOREIGN KEY (scheme_code) REFERENCES dim_fund(scheme_code)
);
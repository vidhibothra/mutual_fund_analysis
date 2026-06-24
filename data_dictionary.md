# Data Dictionary - Mutual Fund Analytics

## Table: dim_fund
| Column Name | Data Type | Description |
|-------------|-----------|------------|
| scheme_code | INTEGER   | Primary Key. Unique identifier for each fund |
| scheme_name | TEXT      | The official name of the mutual fund scheme |
| fund_house  | TEXT      | The asset management company handling the fund |

## Table: fact_nav
| Column Name | Data Type | Description |
|-------------|-----------|------------|
| scheme_code | INTEGER   | Foreign Key matching dim_fund |
| date        | TEXT      | The specific date of the NAV record |
| nav         | REAL      | Net Asset Value on that trading day |
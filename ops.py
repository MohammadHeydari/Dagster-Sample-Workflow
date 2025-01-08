import pandas as pd
from dagster import op
@op
def fetch_sales_data():
    data = {
        "Date": ["2025-01-01", "2025-01-02", "2025-01-03"],
        "Product": ["Laptop", "Mouse", "Keyboard"],
        "Quantity": [10, 50, 30],
        "Price": [1000, 25, 75],
    }
    df = pd.DataFrame(data)
    print("Fetched Sales Data:\n", df)
    return df

@op
def calculate_total_sales(data: pd.DataFrame):
    data["Total"] = data["Quantity"] * data["Price"]
    print("Processed Data with Total Sales:\n", data)
    return data

@op
def save_sales_data(data: pd.DataFrame):
    data.to_csv("processed_sales.csv", index=False)
    print("Saved processed data to 'processed_sales.csv'")

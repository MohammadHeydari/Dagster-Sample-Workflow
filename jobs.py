from dagster import job
from ops import fetch_sales_data, calculate_total_sales, save_sales_data

@job
def sales_data_pipeline():
    save_sales_data(calculate_total_sales(fetch_sales_data()))

if __name__ == "__main__":
    sales_data_pipeline.execute_in_process()

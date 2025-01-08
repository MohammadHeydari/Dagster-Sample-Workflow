# Dagster: Hands-On Guide to Building and Running Data Pipelines

## Overview
This repository accompanies the article **"Dagster: Hands-On Guide to Building and Running Data Pipelines"**. It provides practical examples for creating and managing data pipelines using Dagster. Dagster is a modern data orchestration tool that simplifies building, testing, and monitoring pipelines with an asset-based approach.

---

## Repository Contents

### Files:
- **`ops.py`:** Contains the operations (Ops) for the pipeline.
- **`jobs.py`:** Defines the pipeline (Job) connecting the Ops into a complete workflow.
- **`requirements.txt`:** Lists the Python dependencies needed for the project.

---

## Features
- **Asset-Based Architecture:** Treats data as first-class citizens in the pipeline.
- **Robust Typing System:** Ensures validation of inputs and outputs at every step.
- **Seamless Integration:** Easily integrates with tools like dbt and Airbyte.
- **Built-in Observability:** Provides insights into pipeline performance and dependencies.

---

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Pip installed on your machine

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/dagster-hands-on-guide.git
   cd dagster-hands-on-guide
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Running the Pipeline

### Step 1: Start the Dagster UI (Dagit)
```bash
dagit
```

### Step 2: Open Dagit
- Navigate to `http://127.0.0.1:3000` in your browser.

### Step 3: Execute the Pipeline
- Select the `sales_pipeline` job.
- Click **Launch Execution** to run the pipeline.

---

## Example Code

### Operations (`ops.py`)
```python
from dagster import op

@op
def fetch_sales_data():
    return [
        {"date": "2025-01-01", "product": "Laptop", "quantity": 10, "price": 1000},
        {"date": "2025-01-02", "product": "Mouse", "quantity": 50, "price": 25},
    ]

@op
def calculate_total_sales(data):
    return [{**item, "total": item["quantity"] * item["price"]} for item in data]

@op
def save_sales_data(data):
    print("Processed Sales Data:", data)
```

### Job (`jobs.py`)
```python
from dagster import job
from ops import fetch_sales_data, calculate_total_sales, save_sales_data

@job
def sales_pipeline():
    save_sales_data(calculate_total_sales(fetch_sales_data()))
```

---

## Advanced Features

1. **Partitions and Backfills:**
   - Process data in chunks (e.g., daily or monthly).
   - Reprocess specific data periods easily.

2. **Integration with dbt:**
   - Import dbt models as assets.
   - Orchestrate dbt runs within Dagster.

3. **Data Quality and Lineage:**
   - Validate data at every step.
   - Track dependencies automatically.

---

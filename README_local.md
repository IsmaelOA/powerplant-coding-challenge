
# PowerPlant API

This project provides an API to calculate production plans for power plants based on load demand, fuel costs, and power plant characteristics. The API is built using Flask, and requests are tested with a Python script.

---

### Prerequisites

- Python 3.8 or higher installed on your system.

---

### Setup Instructions

1. **Create a Virtual Environment**

   Open your terminal and navigate to your project directory. Then, create a virtual environment:

   ```bash
   python -m venv venv
   ```

   Activate the virtual environment:

   - On **Windows**:
     ```bash
     venv\Scripts\activate
     ```

   - On **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

2. **Install Required Packages**

   Install the necessary Python packages (`flask` and `requests`) using pip:

   ```bash
   pip install flask requests
   ```

3. **Copy the Code**

   Place the code into the following structure inside your project directory:

   ```
   .
   ├── powerplants/
   │   ├── __init__.py
   │   ├── base.py
   │   ├── units.py
   ├── endpoints/
   │   ├── __init__.py
   │   ├── production_plan.py
   ├── main.py
   ├── send_requests.py
   ```

   - **`powerplants/`**: Contains the power plant logic.
   - **`endpoints/`**: Contains the Flask endpoint logic.
   - **`main.py`**: Starts the Flask server.
   - **`send_requests.py`**: Sends test requests to the API.

4. **Start the Flask Server**

   Run the following command to start the Flask server:

   ```bash
   python main.py
   ```

   By default, the server will run on `http://127.0.0.1:8888`.

---

### Running Tests

To test the API with predefined payloads, execute the test script:

```bash
python send_requests.py
```

The script will:
- Send requests with three different payloads.
- Print the API responses.
- Validate that the total generated power matches the expected load.

---

### Example API Usage

#### Endpoint
- **URL**: `http://127.0.0.1:8888/productionplan`
- **Method**: `POST`

#### Example Request Payload

```json
{
  "load": 480,
  "fuels": {
    "gas(euro/MWh)": 13.4,
    "kerosine(euro/MWh)": 50.8,
    "co2(euro/ton)": 20,
    "wind(%)": 60
  },
  "powerplants": [
    {"name": "gasfiredbig1", "type": "gasfired", "efficiency": 0.53, "pmin": 100, "pmax": 460},
    {"name": "gasfiredbig2", "type": "gasfired", "efficiency": 0.53, "pmin": 100, "pmax": 460},
    {"name": "windpark1", "type": "windturbine", "efficiency": 1, "pmin": 0, "pmax": 150},
    {"name": "windpark2", "type": "windturbine", "efficiency": 1, "pmin": 0, "pmax": 36}
  ]
}
```

#### Example Response

```json
[
  {"name": "windpark1", "p": 150},
  {"name": "windpark2", "p": 36},
  {"name": "gasfiredbig1", "p": 294}
]
```

---

### Notes

- Ensure the Flask server is running before executing `send_requests.py`.
- Modify the `send_requests.py` file to add or adjust test payloads as needed.

---

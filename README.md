# INIVOS ASSESSMENT TASK

This API is used to store and retrieve data related to power consumption.

## Endpoints
    * POST /data - Receives data in a plaintext format and stores it in the database.
    * GET /data?from=2022-04-12&to=2022-04-14 - Retrieves data within the given date range and returns it in JSON format.
    
## Usage
    To send data to the POST /data endpoint, you can use a tool like Postman. To retrieve data from the GET /data endpoint, you can also use Postman or a web browser.

## Installation

1. Make sure Python 3.11 is installed. You can check the version by running the following command:

2. Clone the repository:

3. Navigate to the project directory:

4. Create a virtual environment and activate it:
```console
    virtualenv env 
```

5. Install the required dependencies: 
```console
    pip install -r requirements.txt    
```

6. Run the Flask application:
```console
    flask --app main run 
```

7. Access the application at `http://localhost:5000` in your web browser.


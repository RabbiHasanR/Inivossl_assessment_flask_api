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



# ADDITIONAL CONSIDERATIONS

* How can we test the code to be confident in the implementation?

    * There are many ways to test code to be confident in the implementation. Here are a few examples:
    Unit Testing, Integration Testing, System Testing, Acceptence Testing

* How can we make sure this code is easy to maintain for future developers?

    * To ensure that your code is easy to maintain for future developers, consider the following practices:
    Write Clean and Readable Code, Use Modular and DRY (Don't Repeat Yourself) Principles, Provide Clear Documentation, Apply Design Patterns and Principles, Test Coverage and Automation, Using Version Control

* Our API needs to be high-performance — how can we measure the performance of our API?

    * There are a number of ways to measure the performance of your API. Here are a few examples:
    Response Time Monitoring, Throughpot (monitoring how  many request can handle per second),
    Latency(monitoring time to takes for data travel one point to annother point),
    Error Rate monitoring, Concurrency (handling multiple request same time)

* How could we optimise this code if the API receives many more POST requests than GET requests? What about if the API receives many more GET requests than POST requests?

    Using chaching mechanism, Using database that is optimize for  writing operation for post  request and
    use database that is  optimize for reading operation for  get, using load balancer for distribute tarffic accross multiple  servers

* Would any of this logic need to change to scale to millions of simultaneous connections?
    Yes, the logic in the code would need to change to scale to millions of simultaneous connections. Here are a few things that you would need to consider: Scalable database, load balancer, caching mechanism, using cdn for static content, optimize database query, can use microservice architecture




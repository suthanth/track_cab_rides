# track_cab_rides
The application provides an API to store all the booked and cancelled cab booking details.
Since there will be 200+ request per minute, I made the API Async. When the API is called it put the request into celery queue and returns a task_id.
The user can use this task_id to piggy back and can get to know the status of the request using the API '/bookingStatus/<task_id>'.

# Requirements:
All requiremnets are specified in the requirements.txt file.
To use celery we need to install RabbitMQ on the server. Use the link to install RabbitMQ.
https://www.rabbitmq.com/download.html

# Steps to run the code:
1. Start RabbitMQ server
2. Start the celery task using command : celery worker --app=track_rides_application --pool=gevent --concurrency=500 -l info
3. Start python application


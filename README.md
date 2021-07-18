# django_test_task_july_2021

Startup instructions:
- use "docker-compose up --build".
- application has Swagger. Go to your browser: http://localhost:8000/swagger/ to see docs.
- Endpoints "POST" accept arrays of items (product, orders).
- By default, reports are generated for all time.
  Use parameter /?date={mouth:2}-{day:2}-{year:4} to get reports from this date to today.
- When creating an order, the current quantity of the product and orders for it are checked.
- Order status can't be changed if it's completed, canceled or refunded.
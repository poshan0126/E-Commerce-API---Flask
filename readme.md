# E-Commerce API Mini Project

This project is a mini e-commerce API built using Flask and SQLAlchemy.

## Installation

1. Clone the repository:

   ```bash
   git clone git@github.com:poshan0126/E-Commerce-API---Flask.git
   ```

2. Navigate to the project directory:

   ```bash
   cd E-Commerce-API---Flask
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask application:

   ```bash
   flask run
   ```

2. Access the API endpoints using the base URL: `http://localhost:5000`

## Endpoints

### Customers

- **GET /customers**  
  Retrieve all customers.

- **GET /customers/{id}**  
  Retrieve a specific customer by ID.

- **POST /customers**  
  Create a new customer.

  Sample JSON payload:
  ```json
  {
      "name": "John Doe",
      "email": "john@example.com",
      "phone": "1234567890"
  }
  ```

- **PUT /customers/{id}**  
  Update an existing customer by ID.

- **DELETE /customers/{id}**  
  Delete a customer by ID.

### Products

- **GET /products**  
  Retrieve all products.

- **GET /products/{id}**  
  Retrieve a specific product by ID.

- **POST /products**  
  Create a new product.

  Sample JSON payload:
  ```json
  {
      "name": "Product Name",
      "price": 50.99
  }
  ```

- **PUT /products/{id}**  
  Update an existing product by ID.

- **DELETE /products/{id}**  
  Delete a product by ID.

### Orders

- **GET /orders**  
  Retrieve all orders.

- **GET /orders/{id}**  
  Retrieve a specific order by ID.

- **POST /orders**  
  Create a new order with multiple items.

  Sample JSON payload:
  ```json
  {
      "order_date": "2024-05-08",
      "customer_id": 1,
      "items": [
          {
              "product_id": 1,
              "quantity": 2
          },
          {
              "product_id": 2,
              "quantity": 1
          }
      ]
  }
  ```

- **DELETE /orders/{id}**  
  Delete an order by ID.


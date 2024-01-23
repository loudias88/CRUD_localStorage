# Product CRUD Application

## About the Project

This project is a simple web application for product inventory management. It allows users to add, edit, search, and delete products. Each product includes details such as name, description, price, and quantity. The application stores data locally in the browser using `localStorage`.

### Features

- **Add Product**: Allows adding a new product to the inventory with detailed information.
- **Edit Product**: Ability to change the details of an existing product.
- **Search Product**: Search functionality to quickly find products.
- **Delete Product**: Option to remove selected products from the inventory.

### Technologies Used

- HTML
- CSS
- JavaScript
- Python (for serving the application)

## Instructions for Use

1. Open the `index.html` file in a browser to start the application.
2. To add a product, fill in the text fields and click 'Save Product'.
3. To edit a product, click 'Edit' on the desired product line, change the information, and save.
4. Use the search bar to filter products by name.
5. To delete products, select them and click 'Delete Selected'.

## Python HTTP Server

A simple Python HTTP server is included to serve the application:

- It uses the `http.server` module from Python's standard library.
- Custom request handler is implemented to serve `index.html` as the default page.
- The server can be started by running the Python script.

### Running the Server

1. Ensure Python is installed on your system.
2. Navigate to the project directory.
3. Run the Python script: `python server_script.py` (replace `server_script.py` with the actual script file name).
4. Access the application at `localhost:8000` in your web browser.

## Contributions

Contributions are always welcome! 

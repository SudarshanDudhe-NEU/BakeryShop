# BakeryShop

BakeryShop is a Django-based web application designed to manage bakery products, sales, and customer interactions. It provides an intuitive interface for displaying bakery products, their prices, and detailed descriptions, allowing customers to browse and place orders seamlessly.

## Features

- **Product Management**: Easily manage bakery products with detailed descriptions and images.
- **Product Listing**: View a comprehensive list of all bakery products along with their prices.
- **Product Detail Page**: Individual pages for each product showcasing detailed information and images.
- **Back to Products**: Simple navigation to return to the product list.
- **Responsive Design**: Optimized for use on both desktop and mobile devices.

## Technologies Used

- **Django**: A high-level Python web framework for rapid development and clean design.
- **HTML/CSS**: For structuring and styling the web pages.
- **SQLite**: Default database for storing product data and orders.
- **Bootstrap**: For styling and ensuring the application is responsive.

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/SudarshanDudhe-NEU/BakeryShop.git
   cd BakeryShop
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv env
   source env/bin/activate  # For macOS/Linux
   env\Scripts\activate  # For Windows
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations to set up the database**:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser for accessing the Django admin panel**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Visit the application**:
   Open your web browser and go to `http://127.0.0.1:8000/` to view the application.

## Admin Panel

- Access the Django admin panel at `http://127.0.0.1:8000/admin/` using the superuser credentials created during setup.
- Manage products, prices, and other data from the admin interface.

## Contributing

Contributions are welcome! Feel free to fork this project, submit pull requests, and open issues for improvements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Sudarshan Dudhe

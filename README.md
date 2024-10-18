
# E-Commerce Website

An e-commerce platform built with Django, PostgreSQL, and HTMX. This application allows users to browse products, add items to a shopping cart, and complete purchases. It also features authentication, order management, and an admin dashboard for managing products and customers. The website is responsive and integrates Stripe for handling payments.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Running the Application](#running-the-application)
- [Database](#database)
- [Stripe Integration](#stripe-integration)
- [HTMX for Dynamic UI](#htmx-for-dynamic-ui)
- [Wishlist Feature](#wishlist-feature)
- [Admin Dashboard](#admin-dashboard)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This e-commerce platform allows users to view products by category (e.g., kitchen, electronics), add them to a shopping cart, and place orders. Staff users can manage product listings, track customer orders, and view purchase histories through an admin dashboard. The platform also allows users to create wishlists for their favorite products. Stripe has been integrated to handle payments securely.

## Features

- **User Authentication**: Users can sign up, log in, and log out. Authentication is handled using Django Allauth.
- **Product Listings**: Products are categorized for easy browsing (e.g., kitchen, electronics).
- **Shopping Cart**: Users can add items to their cart and proceed to checkout.
- **Order History**: Users can view their past orders.
- **Wishlist**: Users can add products to a wishlist for later consideration.
- **Admin Dashboard**: Admin users (staff) can manage products, customers, and orders.
- **Responsive Design**: The website is fully responsive, ensuring a seamless experience across devices.
- **Stripe Payment Integration**: Secure credit card payments are handled using Stripe.

## Technologies Used

- **Backend**: Django, PostgreSQL
- **Frontend**: HTML, CSS, JavaScript, HTMX
- **Payment Integration**: Stripe
- **Authentication**: Django Allauth
- **Caching**: Redis (optional)
- **Deployment**: Gunicorn, Nginx, Docker (optional)

## Setup and Installation

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- PostgreSQL
- Stripe account for payments (dev environment keys)

### Installation Steps

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/ecommerce-website.git
   cd ecommerce-website
   ```

2. **Create and Activate a Virtual Environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up PostgreSQL Database:**

   - Create a PostgreSQL database:

     ```sql
     CREATE DATABASE ecommerce_db;
     ```

   - Update `DATABASES` in `ecommerce/settings.py` with your PostgreSQL credentials:

     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'ecommerce_db',
             'USER': 'your_username',
             'PASSWORD': 'your_password',
             'HOST': 'localhost',
             'PORT': '5432',
         }
     }
     ```

5. **Apply Migrations:**

   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser:**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Server:**

   ```bash
   python manage.py runserver
   ```

   Now, the app should be available at `http://localhost:8000`.

## Running the Application

- **Login**: Use `/accounts/login/` to log in to the system.
- **Register**: Use `/accounts/signup/` to create a new user account.
- **Admin**: The Django admin interface is available at `/admin/`.

## Database

PostgreSQL is used as the database for this application. All models are located in the `products` and `accounts` apps.

### Key Models

- **Product**: Represents items available for sale.
- **Category**: Represents product categories (e.g., electronics, kitchen).
- **Order**: Represents customer orders.
- **Wishlist**: Represents the wishlist items for each user.

## Stripe Integration

Stripe is integrated to handle secure payments. To test payments:

1. Create a Stripe account and get the test keys from the dashboard.
2. Update `settings.py` with your Stripe keys:

   ```python
   STRIPE_TEST_PUBLIC_KEY = "your_test_public_key"
   STRIPE_TEST_SECRET_KEY = "your_test_secret_key"
   ```

3. Test payments in the checkout flow.

## HTMX for Dynamic UI

HTMX is used to create dynamic and responsive UI components, such as:

- **Updating the cart**: Items are added/removed from the cart without refreshing the page.
- **Wishlist**: Products can be added to the wishlist dynamically.

## Wishlist Feature

Each user can manage their own wishlist, adding or removing products. This feature is built into the user’s profile section and integrated with the HTMX dynamic UI framework.

## Admin Dashboard

Only admin users have access to the custom admin dashboard. Here, they can:

- Manage products (create, update, delete).
- View and manage customer orders.
- Access customer data for user management.

## Contributing

If you want to contribute to this project:

1. Fork the project.
2. Create a feature branch (`git checkout -b feature/my-new-feature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/my-new-feature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License.

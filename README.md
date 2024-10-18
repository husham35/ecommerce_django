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

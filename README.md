# Karkabou

> [!CAUTION]
> This application is intentionally designed with **privacy and security gaps** and does **not comply with data protection laws**. Karkabou serves as an educational tool to illustrate common mistakes in data protection and security in web applications, specifically highlighting areas of non-compliance with Algerian laws.
>
> This project is inspired by several security and privacy trainings (e.g. [Juice Shop](https://owasp.org/www-project-juice-shop/))

## Overview

Karkabou is a Django application where users can find and contact Karkabou music groups. Users can register their groups for free, but we intend to make this into a premium feature in the future.

For now, our application allows anyone to register their groups and manage their musicians.

Any musician can register to our application, and we can add them to their respective bands.

We had to rush creating this application since our innovative idea has to go to market before weddings & celebrations season, so we may overlooked some things.

> [!IMPORTANT]
> 
> Again, this app is **not designed for production use** and **does not respect user privacy**; instead, it is a demonstration project to help developers understand the importance of privacy compliance and secure coding practices.


- [Karkabou](#karkabou)
  - [Overview](#overview)
  - [Requirements](#requirements)
  - [Installation](#installation)

## Requirements
- Python 3.11+
- Django 5.0+
- Django REST Framework

## Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/karkabou.git
    cd karkabou
    ```
2. Install the dependencies:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
3. Run database migrations
    ```bash
    python manage.py migrate
    python manage.py seed_db
    ```
4. Run the development server:
    ```bash
    python manage.py runserver
    ```

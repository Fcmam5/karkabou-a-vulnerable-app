# Karkabou

> [!CAUTION]
> This application is intentionally designed with **privacy and security gaps** and does **not comply with data protection laws**. Karkabou serves as an educational tool to illustrate common mistakes in data protection and security in web applications, specifically highlighting areas of non-compliance with Algerian laws.
>
> This project is inspired by several security and privacy trainings (e.g. [Juice Shop](https://owasp.org/www-project-juice-shop/))

## Overview

Karkabou is a Django application where users can find and contact Karkabou music groups. This app is **not designed for production use**; instead, it is a demonstration project to help developers understand the importance of privacy compliance and secure coding practices.


> [!IMPORTANT] Disclaimer
> This app **does not respect user privacy**. Data is handled in ways that could lead to serious privacy breaches and security vulnerabilities if implemented in a real-world scenario.

- [Karkabou](#karkabou)
  - [Overview](#overview)
  - [Features](#features)
  - [Requirements](#requirements)
  - [Installation](#installation)


## Features
- **Browse Groups**: Users can search for Karkabou groups by location and genre.
- **Public Contact Info**: Group contact information is displayed without any access control.
- **Track and Log User Actions**: User actions are logged.

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

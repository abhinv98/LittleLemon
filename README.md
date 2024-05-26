# Little Lemon Restaurant API

This is a Django REST API for the Little Lemon Restaurant, which allows for table bookings and user management.

## Features

- **Menu API**: Manage restaurant menu items.
- **Booking API**: Handle table bookings.
- **User Registration and Authentication**: Register and authenticate users using JWT.

## Installation

1. **Clone the repository**:
    ```bash
    git clone <your_repository_url>
    cd LittleLemon
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Run the server**:
    ```bash
    python manage.py runserver
    ```

## API Endpoints

### Authentication

- **Register**: `POST /api/auth/users/`
- **Login**: `POST /api/auth/jwt/create/`

### Bookings

- **List Bookings**: `GET /api/bookings/`
- **Create Booking**: `POST /api/bookings/`
- **Retrieve Booking**: `GET /api/bookings/<id>/`
- **Update Booking**: `PUT /api/bookings/<id>/`
- **Delete Booking**: `DELETE /api/bookings/<id>/`

## Testing

You can test the API endpoints using tools like Insomnia or Postman

### Example Requests

**Create Booking**:
```json
POST /api/bookings/
{
    "name": "Ramlam lam",
    "email": "lamlam@example.com",
    "phone_number": "1234567890",
    "booking_date": "2023-01-01",
    "booking_time": "18:00:00",
    "number_of_guests": 4
}

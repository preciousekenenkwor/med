# Medic App

## Overview

Medic App is a comprehensive healthcare platform built using FastAPI and SQLAlchemy. It enables patients to create profiles and prefill their medical records, schedule appointments with doctors, and receive prescriptions or arrange doctor visitations. Doctors can register on the platform, manage appointments, and provide medical reports. This application is designed to be deployed on Heroku.

## Features

- **User Registration**: Patients and doctors can create accounts on the platform.
- **Patient Profile Management**: Patients can create and manage their profiles and medical records.
- **Doctor Registration**: Doctors can register and manage their accounts.
- **Appointment Scheduling**: Patients can schedule meetings with doctors.
- **Report Management**: Doctors can provide reports after meetings with patients.
- **Prescriptions and Visitations**: Doctors can either provide prescriptions or schedule visitations based on the appointment.

## Technologies Used

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.6+ based on standard Python type hints.
- **SQLAlchemy**: The Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.
- **Heroku**: A platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

## Installation

### Prerequisites

- Python 3.12+
- PostgreSQL
- Heroku CLI

### Local Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/preciousekene/medic-app.git
    cd medic-app
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    pip install pipenv
    pipenv --python 3.12
    pipenv shell
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    Create a `.env` file in the root directory and add the following variables:

    ```plaintext
    DATABASE_URL=postgresql+asyncpg://username:password@localhost/dbname
    ```

5. **Run the database migrations:**

    ```bash
    alembic upgrade head
    ```

6. **Start the development server:**

    ```bash
    uvicorn app.main:app --reload
    ```

    The API will be available at `http://127.0.0.1:8000`.

## Deployment to Heroku

1. **Log in to Heroku:**

    ```bash
    heroku login
    ```

2. **Create a new Heroku application:**

    ```bash
    heroku create medic-app
    ```

3. **Add Heroku Postgres to your application:**

    ```bash
    heroku addons:create heroku-postgresql:hobby-dev
    ```

4. **Set environment variables:**

    ```bash
    heroku config:set DATABASE_URL=your_heroku_database_url
    ```

5. **Deploy the application:**

    ```bash
    git push heroku main
    ```

6. **Run the database migrations on Heroku:**

    ```bash
    heroku run alembic upgrade head
    ```

## API Endpoints

### User Endpoints

- **Register User**: `POST /auth/register`
- **Login User**: `POST /auth/login`

### Patient Endpoints

- **Create Profile**: `POST /patients/profile`
- **Update Profile**: `PUT /patients/profile`
- **Get Medical Records**: `GET /patients/medical_records`

### Doctor Endpoints

- **Register Doctor**: `POST /doctors/register`
- **Login Doctor**: `POST /doctors/login`

### Appointment Endpoints

- **Schedule Appointment**: `POST /appointments`
- **Get Appointments**: `GET /appointments`
- **Update Appointment**: `PUT /appointments/{appointment_id}`

### Report Endpoints

- **Create Report**: `POST /reports`
- **Get Reports**: `GET /reports`
- **Update Report**: `PUT /reports/{report_id}`

## Database Models

### User Model

- **id**: Primary key
- **first_name**: String
- **last_name**: String
- **email**: String
- **password**: String
- **phone**: String
- **is_email_verified**: Boolean
- **created_at**: DateTime
- **updated_at**: DateTime

### Patient Model

- **user_id**: Foreign key to User
- **gender**: String
- **age**: Integer
- **medical_history**: JSON

### Doctor Model

- **user_id**: Foreign key to User
- **specialization**: String
- **years_of_experience**: Integer

### Appointment Model

- **id**: Primary key
- **patient_id**: Foreign key to Patient
- **doctor_id**: Foreign key to Doctor
- **appointment_time**: DateTime
- **status**: String

### Report Model

- **id**: Primary key
- **appointment_id**: Foreign key to Appointment
- **report_details**: Text
- **prescriptions**: JSON
- **visitation_required**: Boolean

## Contributing

1. **Fork the repository**
2. **Create a new branch** (`git checkout -b feature-branch`)
3. **Commit your changes** (`git commit -m 'Add some feature'`)
4. **Push to the branch** (`git push origin feature-branch`)
5. **Create a new Pull Request**

## License

This project is licensed under the MIT License.

## Contact

For any questions or feedback, please reach out to:

- **Email**: <support@medicapp.com>
- **Website**: [medicapp.com](https://medicapp.com)

## Acknowledgements

- Thanks to the FastAPI and SQLAlchemy communities for their amazing documentation and support.
- Special thanks to Heroku for providing a reliable deployment platform.

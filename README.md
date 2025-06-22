# Django Healthcare Backend

A secure and scalable backend system for managing doctors, patients, and their relationships, built using Django, Django REST Framework (DRF), PostgreSQL, and JWT authentication.

---

## 🔢 Tech Stack

* **Backend:** Django, Django REST Framework
* **Database:** PostgreSQL
* **Authentication:** JWT via `djangorestframework-simplejwt`

---

## 📆 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/ajeyajaz/whatbytes_assignment.git

```

### 2. Create Virtual Environment and Install Requirements

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file:

```
SECRET_KEY=your-secret-key
DB_NAME=your-db-name
DB_USER=your-db-user
DB_PASSWORD=your-db-password
DB_HOST=localhost
DB_PORT=5432
```

### 4. Setup the Database

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Server

```bash
python manage.py runserver
```

---

## Authentication APIs

### Register

**POST** `/api/auth/register/`

```json
{
  "name": "Ajay Kumar",
  "email": "ajay@example.com",
  "password": "securepassword123",
  "confirm_password": "securepassword123"
}
```

### Login

**POST** `/api/auth/login/`

```json
{
  "email": "ajay@example.com",
  "password": "securepassword123"
}
```

**Response:**

```json
{
  "access": "JWT_ACCESS_TOKEN",
  "refresh": "JWT_REFRESH_TOKEN"
}
```

---

## Doctor Management APIs

### Add Doctor

**POST** `/api/doctors/`

```json
{
  "name": "Dr. Vijay",
  "specialization": "Cardiologist",
  "phone": "9876543210"
}
```

### Get All Doctors

**GET** `/api/doctors/`

### Get Specific Doctor

**GET** `/api/doctors/1/`

### Update Doctor

**PUT** `/api/doctors/1/`

### Delete Doctor

**DELETE** `/api/doctors/1/`

---

## Patient Management APIs

### Add Patient

**POST** `/api/patients/`

```json
{
  "name": "Rahul",
  "age": 35,
  "gender": "Male",
  "phone": "9123456789"
}
```

### Get All Patients (for logged-in user)

**GET** `/api/patients/`

### Get Specific Patient

**GET** `/api/patients/1/`

### Update Patient

**PUT** `/api/patients/1/`

### Delete Patient

**DELETE** `/api/patients/1/`

---

## 🪜 Patient-Doctor Mapping APIs

### Assign Doctor to Patient

**POST** `/api/mappings/`

```json
{
  "doctor": 2,
  "patient": 1
}
```

### Get All Mappings

**GET** `/api/mappings/`

### Get All Doctors for a Patient

**GET** `/api/mappings/1/`  *(1 = patient ID)*

### Unassign a Doctor

**DELETE** `/api/mappings/5/` *(5 = mapping ID)*

---

## Expected Outcome

* Users can register and log in securely.
* Authenticated users can manage doctor and patient records.
* Doctors can be assigned/unassigned to/from patients.
* Data stored securely in PostgreSQL.


# Finance Tracker

This project is a **Finance Tracker** web application built using the Django framework and HTMX for frontend interactivity. The application allows users to manage their personal finances by tracking income and expenses, categorizing transactions, and generating insightful reports.

## Features

- **User Authentication:** Secure login and registration functionality.
- **Transaction Management:** Add, edit, and delete income and expense transactions.
- **Category Tracking:** Assign transactions to predefined or custom categories.
- **Form Validation:** Real-time form validation using HTMX.
- **Reports & Insights:** View summary reports of financial data.
- **Testing:** Unit and integration tests implemented to ensure app reliability.
- **Responsive Design:** Mobile-friendly UI with Bootstrap.

## Technologies Used

- **Backend:** Django (Python)
- **Frontend:** HTMX, HTML, CSS, Bootstrap
- Database: SqlAlchemy
- **Testing:** Django Test Framework
- **Deployment:** Docker, Gunicorn, Nginx

## Installation

Follow the steps below to set up the project locally:

### Prerequisites

Ensure you have the following installed:

- Python 3.8+
- pip (Python package manager)
- Virtualenv (optional but recommended)
- Docker (optional for deployment)

### Setup Instructions

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/RutujaGurav07/Finace_tracker.git)
   cd finance-tracker
   ```

2. **Create and Activate Virtual Environment:**

   ```bas
   python -m venv venv
   source venv/bin/activate   # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Create Superuser:**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run Development Server:**

   ```bash
   python manage.py runserver
   ```

7. **Access the Application:**
   Open your browser and go to `http://127.0.0.1:8000`

## Running Tests

To run unit tests, execute:

```bash
python manage.py test
```

## Deployment

To deploy using Docker, follow these steps:

1. **Build the Docker Image:**

   ```bash
   docker build -t finance-tracker .
   ```

2. **Run the Docker Container:**

   ```bash
   docker run -d -p 8000:8000 finance-tracker
   ```

## Resources

- [Django Documentation](https://docs.djangoproject.com/en/)
- [HTMX Documentation](https://htmx.org/docs)
- [Bootstrap](https://getbootstrap.com)

## Acknowledgments

Special thanks to the [YouTube Tutorial Series](https://www.youtube.com/watch?v=6OlILeP9GKg&list=PL-2EBeDYMIbSBjHGYJYl1WLUT-tbCLHOb) for guidance on building this project.


# Factory Monitor

This project is a web application for visualizing time-series data from factory sensors. It includes a Django-based backend and a React frontend.

## Setup Instructions

### Backend

1. Create and activate a virtual environment:

    On Windows:
    ```sh
    python -m venv env
    env\Scripts\activate
    ```

    On macOS/Linux:
    ```sh
    python -m venv env
    source env/bin/activate
    ```

2. Install the required packages:
    ```sh
    pip install django djangorestframework pymongo djongo
    ```

3. Create and configure the Django project:
    ```sh
    django-admin startproject factory_monitor
    cd factory_monitor
    django-admin startapp api
    ```

4. Update `factory_monitor/settings.py` as shown above.

5. Define models, serializers, views, and URLs as shown in the respective files.

6. Run the migrations and start the server:
    ```sh
    python manage.py migrate
    python manage.py runserver
    ```

### Frontend

1. Navigate to the project root directory and create a React app:
    ```sh
    npx create-react-app frontend
    cd frontend
    npm install axios chart.js react-chartjs-2
    ```

2. Create the necessary components (`DeviceList.js` and `DeviceDetails.js`) and set up the main component (`App.js`).

3. Add the proxy configuration to `frontend/package.json`:
    ```json
    "proxy": "http://localhost:8000"
    ```

4. Start the React development server:
    ```sh
    npm start
    ```

## Usage

1. Run the Django backend server:
    ```sh
    python manage.py runserver
    ```

2. Run the React frontend server:
    ```sh
    npm start
    ```

3. Open your browser and navigate to `http://localhost:3000` to view the application.

## Notes

- Ensure MongoDB is running and accessible.
- Adjust the MongoDB connection settings as needed in `factory_monitor/settings.py`.
- The application currently provides basic functionality for viewing device parameter data. Further enhancements can include better error handling, additional features, and more complex data visualizations.

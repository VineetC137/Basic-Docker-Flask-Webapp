# Basic Flask Docker Application

A simple Flask web application that displays a personalized dashboard with the current time and motivational quotes. This application is containerized using Docker for easy deployment.

## Features

- **Current Time Display**: Shows the current date and time
- **Random Motivational Quotes**: Displays one of several inspiring quotes on each page load
- **Responsive Design**: Clean, modern UI with gradient background
- **Docker Containerized**: Easy to build and run anywhere

## Prerequisites

- Docker installed on your system

## Getting Started

### Clone the Repository

```bash
git clone <repository-url>
cd "Basic Flask Docker Application"
```

### Build the Docker Image

```bash
docker build -t flask-dashboard .
```

### Run the Application

```bash
docker run -p 5000:5000 flask-dashboard
```

### Access the Application

Open your web browser and navigate to:
```
http://localhost:5000
```

You should see a dashboard with:
- A welcome message for Vineet
- The current date and time
- A random motivational quote
- Confirmation that the Flask Docker app is running

## Project Structure

```
.
├── app.py              # Main Flask application
├── Dockerfile          # Docker container configuration
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Technologies Used

- **Flask**: Python web framework
- **Docker**: Containerization platform
- **Python 3.10**: Programming language

## Customization

You can customize the application by:

1. **Changing the welcome message**: Edit the `h1` tag in `app.py`
2. **Adding more quotes**: Modify the `quotes` list in `app.py`
3. **Updating the styling**: Modify the CSS in the `html_template` string

## License

This project is for educational purposes.
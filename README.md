# Sentiment Analysis

This project is a Django-based web application for analyzing text sentiment, emotion, and moderation using various machine learning models from Hugging Face. The application allows users to input text and select a task (sentiment analysis, emotion analysis, or moderation radar) to get the analysis results.

You can access the live website [here](https://phrase-sentiment-analysis.up.railway.app/)

## Table of Contents

- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Environment Variables](#environment-variables)
- [Running the Application](#running-the-application)
- [Docker Support](#docker-support)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Technologies Used

- **Django**: Web framework for building the application.
- **HTMX**: For handling AJAX requests and updating parts of the web page.
- **Tailwind CSS**: For styling the application.
- **Whitenoise**: For serving static files.
- **Gunicorn**: WSGI HTTP server for running the application.
- **Hugging Face**: Pre-trained models for sentiment, emotion, and moderation analysis.
- **Python Decouple**: For managing environment variables.
- **Flowbite**: UI components built with Tailwind CSS.


## Setup and Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/Sheriff-AA/sentiment-analysis.git
    cd sentiment-analysis
    ```

2. **Create a virtual environment and activate it:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Install Tailwind CSS:**

    ```sh
    npm install
    ```

5. **Build Tailwind CSS:**

    ```sh
    npm run build
    ```

## Environment Variables

Create a .env file in the root directory and add the following environment variables:

```
DJANGO_SECRET_KEY=your_secret_key
DJANGO_DEBUG=True
ALLOWED_HOST=localhost
CSRF_TRUSTED_ORIGINS=http://localhost
HUGGING_FACE=your_hugging_face_api_key
```

## Running the Application

1. **Apply database migrations:**

    ```sh
    python manage.py migrate
    ```

2. **Pull static files:**

    ```sh
    python manage.py static_pull
    ```

3. **Collect static files:**

    ```sh
    python manage.py collectstatic --noinput
    ```

4. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

## Docker Support

1. **Build the Docker image:**

    ```sh
    docker build -t sentiment-analysis .
    ```

2. **Run the Docker container:**

    ```sh
    docker run -p 8000:8000 sentiment-analysis
    ```

## Usage

1. Open your web browser and navigate to 
    ```sh
    http://localhost:8000
    ```

2. Enter the text you want to analyze.
3. Select the task (Sentiment Analysis, Emotion Analysis, or Moderation Radar).
4. Click the "Submit" button to get the analysis results.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.


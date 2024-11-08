# Wallet

## Installation and Setup

Follow these instructions to run the project locally.

### Prerequisites

Make sure you have the following software components installed:

- Docker
- Docker Compose

### Clone the Repository

1. **Clone the repository:**

    ```bash
    git clone git@github.com:agmiloserdov/wallet.git
    cd wallet
    ```

### Running the Project using Docker Compose

1. **Build and start the containers:**

    ```bash
    docker compose up --build
    ```

2. **Apply database migrations (if exists):**

    In a new terminal window:

    ```bash
    docker compose exec web python manage.py migrate
    ```


3. **Load fixtures (if any):**

    ```bash
    docker compose exec web python manage.py loaddata fixtures/dump.json
    ```

### Testing

To run the tests, execute:

```bash
docker compose exec web pytest
```

### Usage

1. **Start the development server:**

    In the same terminal where you ran `docker-compose up`:

    ```plain text
    web_1  | Watching for file changes with StatReloader
    web_1  | Performing system checks...
    web_1  | 
    web_1  | System check identified no issues (0 silenced).
    web_1  | 
    web_1  | You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
    web_1  | Run 'python manage.py migrate' to apply them.
    web_1  | October 06, 2023 - 12:09:48
    web_1  | Django version 3.2.5, using settings 'your_project.settings'
    web_1  | Starting development server at http://0.0.0.0:8000/
    web_1  | Quit the server with CONTROL-C.
    ```

2. **Open your browser and go to:**
http://127.0.0.1:8000/

### Additional Information

#### Code Style

We use linters and formatters to maintain a consistent code style. Run them before creating a pull request:

```bash
docker compose exec web flake8
docker compose exec web black .
```

#### Swagger Documentation

This project also includes API documentation using Swagger. To access the Swagger UI, follow these steps:
rver, Swagger UI will be available at:

http://localhost:8000/api/schema/swagger-ui/

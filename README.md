# Summary service

## Prerequisites

The project relies on the following Python dependencies, also listed in `pyproject.toml`:

- Python => 3.7
- FastAPI
- Uvicorn
- Scikit-learn
- Pandas

## Running locally

To run the service locally, follow these steps:

### Step 1: Install dependencies

1. Create a virtual environment (optional but recommended). You can use `venv` or `conda` to create a virtual
   environment:

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```


2. Install the necessary dependencies from `pyproject.toml`:

   ```bash
   pip install -r requirements.txt 
   ```

3. Run the application locally by executing the following command:

```bash
uvicorn app.main:app --reload
```

Endpoints will be accessible at: `http://localhost:8000/`

## API Documentation

## TODOs

### Backend

- Setup database (Heroku, MongoDB)
- Save article ID
- Remove duplicate articles
- Store summarized articles, date, title, id, link
- Add endpoint for fetching new articles and store to DB
- Add tests and CI automation (Github actions)
- Setup CRON jobs for fetching articles, summarization and storing to DB
- Cache summarized articles (Redis)

### Frontend

- Add refresh button for fetching new articles
- Fix styling/aligning of header
- Setup pagination and "Load more" feature with infinite scrolling
- Add tests and CI automation (Github actions)
- Add search for filtering articles
- Display loading indicator while summarizing
- 

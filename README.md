# App Scraper

Scraper for steamcommunity

## Getting Started
1. Clone the repository:

    ```bash
    git clone https://github.com/alfredrumss/scraper.git
    ```

2. Install the project dependencies using poetry:

    ```bash
    cd scraper
    poetry install
    ```

3. Run the application:

    ```bash
    make run
    ```
    or using full command:
    ```bash
    docker compose up --build -d
    ``` 
   
   scraper is located in app/src/contrib/scraper.py
   it runs before FastApi application is initiated 

The application will start running on `http://localhost:8004/docs#/`.
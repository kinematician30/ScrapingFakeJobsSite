# Fake Jobs Data Scraper

## Project Description

This project is a Python script designed to scrape job listing data from the website [https://realpython.github.io/fake-jobs/](https://realpython.github.io/fake-jobs/). The script extracts key information about each job, including the job title, company name, location (city and state), and the date the job was posted. The date is processed to provide both a formatted date string (e.g., "Thursday, 8 April") and the year separately. The extracted data is then saved into a CSV file for further analysis or use.

## Objectives

* Scrape job data from [https://realpython.github.io/fake-jobs/](https://realpython.github.io/fake-jobs/).
* Extract the following information for each job listing:
    * Job Title
    * Company Name
    * Location (City)
    * Location (State)
    * Date Posted (formatted as "Day of Week, Day Month")
    * Year
* Convert the original date string into a Python `datetime` object.
* Save the extracted and processed data into a CSV file.
* Implement logging for script operations and error handling.

## Files

* `jobs_scraper.py`: The Python script containing the web scraping and data processing logic.
* `Jobs_Data.csv`: The output CSV file containing the extracted job data.
* `logs/bot.log`: The log file for script operations and errors.

## Dependencies

* Python 3.x
* `requests`
* `beautifulsoup4` (bs4)
* `pandas`

## Installation

1.  Clone the repository to your local machine:

    ```bash
    git clone [Your Repository URL]
    ```

2.  Navigate to the project directory:

    ```bash
    cd [Your Project Directory]
    ```

3.  Install the required Python packages:

    ```bash
    pip install requests beautifulsoup4 pandas
    ```

## How to Run the Script

1.  Ensure you have Python 3.x and the required packages installed.
2.  Navigate to the project directory in your terminal.
3.  Run the Python script:

    ```bash
    python jobs_scraper.py
    ```

4.  The script will:
    * Scrape the job data from the specified website.
    * Process the data and format the date.
    * Save the data to a CSV file named `Jobs_Data.csv`.
    * Log script operations and errors to `logs/bot.log`.

## Output

The script generates a CSV file named `Jobs_Data.csv` in the project directory. This file contains the extracted job data, including the formatted date and year.

## Logging

The script uses Python's `logging` module to log important information and potential errors. Logs are written to `logs/bot.log`.

## Notes

* Ensure you have a stable internet connection to run the script.
* The script assumes the website structure remains consistent. If the website's HTML structure changes, the script may need to be updated.
* The script handles basic connection errors using `requests.exceptions`.

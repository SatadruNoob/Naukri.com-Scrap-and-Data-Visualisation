![python](https://github.com/user-attachments/assets/8277b8a6-c22c-47d2-be0a-594111c9360b) ![chrome](https://github.com/user-attachments/assets/b97fca06-c67b-4eb2-8bda-90c113eda2dd) ![sele](https://github.com/user-attachments/assets/b248a567-3a6e-4462-967a-d1aad88f8d30) ![naukri](https://github.com/user-attachments/assets/f9d4f73a-072a-4ec9-9c85-03a530895ca8) 


**Project Description**

This repository contains code for a web scraping and data processing pipeline designed to extract job listings from a job portal, specifically focusing on data analyst positions. The project is divided into two main parts:

**Part 1: Web Scraping and Data Extraction**
**Objective:** Extract job listing data from the Naukri job portal.
**Process:**
**System Setup:** Install system dependencies for Google Chrome and Selenium.
**Dependencies:** Use system_dependencies.txt to install necessary system packages and requirements.txt for Python libraries.

**Code**:
Set up a Selenium WebDriver with Chrome to scrape job listings.
Extract relevant job details including company name, ratings, salary, experience, location, job posting days, description, and skills.
Save the extracted data into Excel files.
Data Cleaning: Perform data cleaning on the extracted job location information. The cleaning process includes:
Removing brackets and the words within them.
Handling words separated by the "/" symbol.
Removing text after the word "Hybrid".
Creating a final cleaned CSV file comparing the original and cleaned data.

**Part 2: Data Visualization**
**Objective:** Apply various data visualization techniques on the "combined_job_listings.xlsx" file obtained from the first process.
**Description:** This part of the project will involve analyzing and visualizing the job listing data to extract insights and trends.
Files
**system_dependencies.txt:** Lists the system packages required for setting up the environment.
**requirements.txt:** Lists the Python libraries required for both web scraping and data visualization.

**Instructions**
**Set Up the Environment:**

Use system_dependencies.txt to install the necessary system packages.

Install Python packages using requirements.txt:

bash
Copy code
pip install -r requirements.txt
Run the Code:

Execute the web scraping and data extraction script.
Clean the extracted data as described.
Apply data visualization techniques on the cleaned data.


**Contributing**
Forking: Feel free to fork the repository and create pull requests.


**Disclaimer**
This script is provided for educational and demonstration purposes only. The authors do not endorse or encourage any form of web scraping that violates the terms of service or policies of the targeted website.

Use this script responsibly and ensure compliance with the terms and conditions of the websites you intend to scrape. Web scraping can put a load on the server and may impact the performance for other users. Make sure to review and respect the website's robots.txt file and terms of service before scraping.

The authors are not responsible for any legal issues, damages, or misuse arising from the use of this script. It is your responsibility to ensure that your actions are in accordance with the applicable laws and regulations.

Always refer to the website's terms of service and legal guidelines to understand the limitations and permissions for web scraping activities.

Use this script at your own risk.
Issues: Report any issues or feature requests via GitHub Issues.

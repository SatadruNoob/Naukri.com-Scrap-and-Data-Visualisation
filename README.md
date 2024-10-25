![python](https://github.com/user-attachments/assets/8277b8a6-c22c-47d2-be0a-594111c9360b) ![chrome](https://github.com/user-attachments/assets/b97fca06-c67b-4eb2-8bda-90c113eda2dd) ![sele](https://github.com/user-attachments/assets/b248a567-3a6e-4462-967a-d1aad88f8d30) ![naukri](https://github.com/user-attachments/assets/f9d4f73a-072a-4ec9-9c85-03a530895ca8) 


**Project Description**

This repository contains code for a web scraping and data processing pipeline designed to extract job listings from a job portal called "www.naukri.com", specifically focusing on "Data Analyst" positions. 


**Target webpage and the target data points**

Company	Ratings	Salary	Years of Experience	Location	Days since Posted	Job Description	Skill Set
![image](https://github.com/user-attachments/assets/a98317d9-c395-447e-89e1-664209fb7849)




Required field for data extraction 
![naukri pointers](https://github.com/user-attachments/assets/8ec8b841-a90a-4820-8176-f05d651a21eb)





The project is divided into two main parts Part 1 and Part 2. A total of approx 1000 pages consisting of over 18,000 plus job postings for "Data Analyst" positions. This scraper can be modified to scrap any desired/valid position for any desired nuber of pages. To change the "Data Analyst" positions to any desired position that is valid and available in Naukri.com change the "data-analyst" in function def extract_job_data(page_num) present in script "Web_Scraping_Data_Extraction_Location_Cleaning.py" which is present in Part 1: Web Scraping_Data Extraction_Location Cleaning. As indicated in the image below.


![Untitled](https://github.com/user-attachments/assets/41ff5b92-28b5-4402-b249-91f25d3d0220)

In order to change the page numbers to any desired numbers, you can change the start and end page as shown in the image below. Pls make sure that the end page is valid and contains data with regards to you desired job position. As indicated to the image below present in script "Web_Scraping_Data_Extraction_Location_Cleaning.py" which is present in Part 1: Web Scraping_Data Extraction_Location Cleaning.
![Untitled](https://github.com/user-attachments/assets/fb886bea-c92d-4bb6-93d1-fe30a3b909e9)



**Part 1: Web Scraping_Data Extraction_Location Cleaning**
**Objective:** 
   Extract job listing data from the Naukri job portal.

**Process:**
 **System Setup:** 
   Install system dependencies for Google Chrome and Selenium.
 **Dependencies:** 
   Use system_dependencies.txt to install necessary system packages and requirements.txt for Python libraries.

 **Code**:
   Set up a Selenium WebDriver with Chrome to scrape job listings.
   Extract relevant job details including Company Name, Ratings, Salary, Experience, Location, Job Posting Days, Description, and Skills.
   Save the extracted data into Excel files.
   Data Cleaning: Perform data cleaning on the extracted job location information. The cleaning process includes:
   Removing brackets and the words within them.
   Handling words separated by the "/" symbol.
   Removing text after the word "Hybrid".
   Creating a final cleaned CSV file comparing the original and cleaned data. The CSV file produces at the end of the Part 1: Web Scraping and Data Extraction is called "Final_Cleaned_File.xlsx".
   The script named as "Web_Scraping_Data_Extraction_Location_Cleaning.py" contains the necessary code for Part 1: Web Scraping_Data Extraction_Location Cleaning.

**Part 2: Data Visualization**
**Objective:**
   Apply various data visualization techniques on the "Final_Cleaned_File.xlsx" file obtained from the first process of Part 1: Web Scraping and Data Extraction.
**Description:**
   This part of the project will involve analyzing and visualizing the job listing data to extract insights and trends.
   The script named as "Data_Visualization.py" contains the necessary code for Part 2: Data Visualization.

**system_dependencies.txt:**
   Lists the system packages required for setting up the environment.
**requirements.txt:**
   Lists the Python libraries required for both web scraping and data visualization.

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


![#Top Skill Set for Different bangalore](https://github.com/user-attachments/assets/3ad81595-d848-4984-8379-88fcc7ddb56c)
![#Top Roles by Location](https://github.com/user-attachments/assets/72322fad-4167-41d4-9c95-d72ef3360ac0)
![Top Locations Contributing to Data Skewness with 'Years of Experience' up to 8](https://github.com/user-attachments/assets/77d74179-2824-4a41-a6b8-f899853ec9a1)
![Most Skills by Location](https://github.com/user-attachments/assets/9ceb8ef2-0f04-42fb-a6b7-93abd9a08f76)
![abc](https://github.com/user-attachments/assets/51e9d05b-30d6-42b0-9647-8403af598b34)
![#Word clouds for each top location](https://github.com/user-attachments/assets/85712555-f96e-4279-86aa-69386abbb957)
![#Top Skill Set for Different Pune](https://github.com/user-attachments/assets/91255ce3-5bfd-4a11-8075-261f8989e17c)
![#Top Skill Set for Different Mum](https://github.com/user-attachments/assets/0697b7cc-1267-46e0-a803-127e4bcd56d1)
![#Top Skill Set for Different Hyd](https://github.com/user-attachments/assets/179d4ec6-7248-4340-aed5-56bfa35645f3)



**Contributing**
  Forking: Feel free to fork the repository and create pull requests.


**Disclaimer**
  This script is provided for educational and demonstration purposes only. The authors do not endorse or encourage any form of web scraping that violates the terms of service or policies of the targeted website.

  Use this script responsibly and ensure compliance with the terms and conditions of the websites you intend to scrape. Web scraping can put a load on the server and may impact the performance for other users. Make sure   to review and respect the website's robots.txt file and terms of service before scraping.

  The authors are not responsible for any legal issues, damages, or misuse arising from the use of this script. It is your responsibility to ensure that your actions are in accordance with the applicable laws and   regulations.

  Always refer to the website's terms of service and legal guidelines to understand the limitations and permissions for web scraping activities.

  Use this script at your own risk.
  Issues: Report any issues or feature requests via GitHub Issues.

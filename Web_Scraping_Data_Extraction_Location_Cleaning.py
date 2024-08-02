# Install required packages
!pip install chromedriver-autoinstaller
!pip install selenium
!pip install pandas

# Import necessary libraries
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import time
import os
import re

# Install the ChromeDriver version that matches the installed Chrome version
chromedriver_autoinstaller.install()

# Function to initialize the webdriver
def init_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    driver = webdriver.Chrome(options=options)
    return driver

# Function to extract job data from a single page
def extract_job_data(page_num):
    url = f"https://www.naukri.com/data-analyst-jobs-{page_num}?k=data+analyst&nignbevent_src=jobsearchDeskGNB"
    driver = init_driver()
    driver.get(url)
    time.sleep(5)  # Add a delay to ensure the page loads completely

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    job_listings = soup.find_all('div', {'class': 'cust-job-tuple layout-wrapper lay-2 sjw__tuple'})
    job_data = []

    for job in job_listings:
        company_name = job.find('a', {'class': 'comp-name'}).text.strip()
        ratings = job.find('span', {'class': 'main-2'})
        ratings = ratings.text.strip() if ratings else None
        salary = job.find('span', {'class': 'sal'})
        salary = salary.text.strip() if salary else None
        years = job.find('span', {'class': 'expwdth'}).text.strip()
        location = job.find('span', {'class': 'locWdth'}).text.strip()
        days_element = job.find('span', {'class': 'job-post-day'})
        days = days_element.text.strip() if days_element else None
        job_desc = job.find('span', {'class': 'job-desc ni-job-tuple-icon ni-job-tuple-icon-srp-description'}).text.strip()
        skill_set_elements = job.find('ul', {'class': 'tags-gt'}).find_all('li', {'class': 'dot-gt tag-li'})
        skill_set = ', '.join([skill.text.strip() for skill in skill_set_elements])

        job_data.append([company_name, ratings, salary, years, location, days, job_desc, skill_set])

    driver.quit()
    return job_data

# Function to save job data to an Excel file
def save_to_excel(job_data, start_page, end_page):
    columns = ['Company', 'Ratings', 'Salary', 'Years of Experience', 'Location', 'Days since Posted', 'Job Description', 'Skill Set']
    df = pd.DataFrame(job_data, columns=columns)
    df.to_excel(f"/content/job_listings_pages_{start_page}_to_{end_page}.xlsx", index=False)

# Main function for Procedure 1: Web Scraping
def scrape_job_data(start_page=1, end_page=10, pages_per_file=5):
    for i in range(start_page, end_page + 1, pages_per_file):
        all_job_data = []
        for page_num in range(i, min(i + pages_per_file, end_page + 1)):
            job_data = extract_job_data(page_num)
            all_job_data.extend(job_data)
        save_to_excel(all_job_data, i, min(i + pages_per_file - 1, end_page))

# Function to compile all Excel files into a single file
def compile_excel_files_to_single_sheet(directory, output_file):
    all_data = []

    for filename in os.listdir(directory):
        if filename.endswith(".xlsx") and filename.startswith("job_listings_pages"):
            filepath = os.path.join(directory, filename)
            print(f"Reading {filepath}")
            df = pd.read_excel(filepath)
            all_data.append(df)

    combined_df = pd.concat(all_data, ignore_index=True)
    combined_df.to_excel(output_file, index=False)
    print(f"Combined data saved to {output_file}")

# Function to clean the consolidated data
def clean_data(file_path):
    df = pd.read_excel(file_path)

    # Step 1: Remove brackets and the words within them
    def remove_brackets(location):
        return re.sub(r'\(.*?\)', '', location).strip()

    df['Location'] = df['Location'].apply(remove_brackets)
    df.to_excel('/content/Part1.xlsx', index=False)

    # Step 2: Handle words separated by the "/" symbol
    def remove_text_after_slash(location):
        parts = re.split(r'(\s*,\s*)', location)
        cleaned_parts = []
        for part in parts:
            if '/' in part:
                part = part.split('/')[0].strip()
            cleaned_parts.append(part)
        return ''.join(cleaned_parts).strip()

    df['Location'] = df['Location'].apply(remove_text_after_slash)
    df.to_excel('/content/Part2.xlsx', index=False)

    # Step 3: Remove text after the word "Hybrid"
    def remove_after_hybrid(location):
        if 'Hybrid' in location:
            return location.split('Hybrid')[0] + 'Hybrid'
        return location

    df['Location'] = df['Location'].apply(remove_after_hybrid)
    df.to_excel('/content/Part3.xlsx', index=False)

    # Create the final cleaned file with original and cleaned data
    original_data = pd.read_excel(file_path)
    final_df = pd.DataFrame({
        'Original Location': original_data['Location'],
        'Cleaned Location': df['Location']
    })
    final_df.to_excel('/content/Final_Cleaned_File.xlsx', index=False)

# Main function to run the entire workflow
def main():
    # Step 1: Web scraping
    scrape_job_data(start_page=102, end_page=1000, pages_per_file=50)
    
    # Step 2: Compile Excel files
    compile_excel_files_to_single_sheet(directory="/content", output_file="/content/combined_job_listings.xlsx")
    
    # Step 3: Data cleaning
    clean_data('/content/combined_job_listings.xlsx')

# Run the main function
if __name__ == "__main__":
    main()

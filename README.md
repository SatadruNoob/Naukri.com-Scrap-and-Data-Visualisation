![python](https://github.com/user-attachments/assets/8277b8a6-c22c-47d2-be0a-594111c9360b) ![chrome](https://github.com/user-attachments/assets/b97fca06-c67b-4eb2-8bda-90c113eda2dd) ![sele](https://github.com/user-attachments/assets/b248a567-3a6e-4462-967a-d1aad88f8d30) ![naukri](https://github.com/user-attachments/assets/f9d4f73a-072a-4ec9-9c85-03a530895ca8) 


**Project Description**

This repository contains code for a web scraping and data processing pipeline designed to extract job listings from a job portal called "www.naukri.com", specifically focusing on "Data Analyst" positions. 


**Target webpage and the target data points**

**Target Fields** 
Company	Ratings	Salary	Years of Experience	Location	Days since Posted	Job Description	Skill Set
![image](https://github.com/user-attachments/assets/b9114b10-ce0f-4a29-b923-49d3033b8192)


**Target Fields pointed out in the webpage**
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



  **Extracted Data Points for first 5 pages shown as example**

Company	Ratings	Salary	Years of Experience	Location	Days since Posted	Job Description	Skill Set
Peroptyx		Not disclosed	0-5 Yrs	Remote	1 Day Ago	For thousands of years, maps have provided humans with the knowledge they need to make ...	Data Analysis, English, Data Analytics, Data Mapping, Data, Analytics, Mapping, Analysis
Ilakku Tech Skills Academy		Not disclosed	0 Yrs	Chennai(Aminjikarai)	1 Day Ago	Female candidate only.	Data Analysis, data, Data Management, Data Extraction, Data Reporting, Extraction, Reporting, Management
Novel Office	4.0	2.5-3 Lacs PA	0-1 Yrs	Bengaluru	1 Day Ago	Only Male Candidates Shift timings (1pm - 9pm) Qualifications: . Bachelors / Undergradu...	Communication Skills, Excel, Analytical Skills, Data Interpretation, Problem Solving, Data Analysis, Data Collection, Reporting
DAT Solutions	4.0	Not disclosed	2-3 Yrs	Bengaluru	1 Day Ago	Perform detailed analysis on transportation data provided by clients, conduct extensi...	Supply chain management, Excel, Analytical, Industrial engineering, power bi, Data Analyst, Data analytics, Freight
USHA International	4.1	3.75-4 Lacs PA	1-3 Yrs	Gurugram	6 Days Ago	Role & responsibilities Preferred candidate profile Perks and benefits	Data Analytics, SAP, Countif, KPI, Data Management, analyse, Conditional Formatting, Formulas
MSCI Services	3.9	Not disclosed	0-2 Yrs	Mumbai	15 Days Ago	MSCI, Pride & Allies, Women in Tech, and Women s Leadership Forum. At MSCI we are passi...	c++, access, jsp, dbms, jdbc, bootstrap, research, sql
Volvo Penta		Not disclosed	3-6 Yrs	Bengaluru	1 Day Ago	List here the job requirements in terms of skills, knowledge, and experience but also m...	Supply chain, Database design, Construction equipment, data privacy, Business strategy, Data mining, microsoft, Financial services
Honeywell	4.0	Not disclosed	2-4 Yrs	Greater Noida, Bengaluru	1 Day Ago	Bachelor s degree or Advanced degree in Computer Science, Statistics, Mathematics, or r...	Computer science, Data analysis, Interpersonal skills, tableau, Statistical modeling, Development Manager, power bi, Pricing Analyst
Sheetal Group	3.4	3-5 Lacs PA	0-2 Yrs	Mumbai	3 Days Ago	Extract data from various market sources for analyzing it to the advantage of business....	Data Analytics, Data Science, Predictive Modeling, Power Bi, Data Analysis, Statistical Modeling, Data Visualization, Data Cleansing
Sustainext Digital Private Limited	4.0	Not disclosed	3-5 Yrs	Bengaluru	6 Days Ago	Preferred candidate profile  . We are looking for a Data Analyst with 3+ years of exper...	building ETL pipelines, Data Management And Analysis, PowerBI, Data Analytics, SaaS platform, Azure, data automation, Tableau
AIR INDIA SATS Private Ltd. (AISATS)	3.8	3-4.25 Lacs PA	0-1 Yrs	Mumbai	10 Days Ago	Job Purpose & Responsibilities:Create high-quality PowerPoint presentations that effec...	Power Bi, Advanced Excel, Power Point Presentation, Data Analysis, Data Visualization, Data Extraction, Bi, Data
Udaan Skills		Not disclosed	1-5 Yrs	Remote	1 Day Ago	Bachelor s degree in Statistics, Mathematics, Computer Science or equivalent	Analytical skills, Skill development, Data Analyst, Mathematics, Product research, Statistics, Monitoring, Testing
Myntra	4.0	Not disclosed	2-4 Yrs	Bengaluru	8 Days Ago	Qualifications & Experience: . Strong problem solving ability The candidate needs to ex...	Data Analytics, R, Excel, Tableau, SQL, Python, Analysis, Data
SPG Corporate		Not disclosed	3-5 Yrs	New Delhi	3 Days Ago	SPG Corporate is looking for Data Analyst to join our dynamic team and embark on a rewa...	master data, metadata, python, data analysis, data management, data analytics, data validation, configuration
Pearce Services Global	3.3	3-6 Lacs PA	2-5 Yrs	Mohali, Gurugram	6 Days Ago	You should be a sound professional and an individual who likes to take ownership of you...	Fleet Operations, Fleet Management, Data Analytics, LYTX, VLOOKUP, Department of Transportation, Manage WEX, Operations
Actalent Services	3.4	Not disclosed	5-10 Yrs	Hyderabad	7 Days Ago	Relevant Experience5+ years Desired Education QualificationMasters degree in computer s...	Data Science, Data Analytics, Machine Learning, Python, Science, Analytics, Data analysis, Machine
DUN BRADSTREET INFORMATION SERVICES INDIA PRIVATE LIMITED	3.3	Not disclosed	3-5 Yrs	Mumbai	1 Day Ago	Demonstrate strong domain knowledge on end-to-end Master Data Management (MDM)s process...	Business communication, Master data management, Data Analyst, HTML, Data quality, Business intelligence, Analytics, SQL
CGI	4.1	Not disclosed	4-8 Yrs	Hyderabad	1 Day Ago	Employment Type: Full Time Required qualifications to be successful in this role: Posit...	Computer science, Business process, Automation, Data analysis, CGI, Analytical, Business intelligence, Analytics
Muthoot FinCorp (MFL)	4.0	Not disclosed	2-5 Yrs	Thiruvananthapuram	1 Day Ago	Any Graduation2+ years of experience in data analytics preferably in financial services...	Data Analysis, Data Collection, Data Sourcing, Information Research, Data Research, Statistical Data Analysis, Data Reporting, Sourcing
Infinity learn	3.9	4-6 Lacs PA	1-6 Yrs	Bengaluru	8 Days Ago	Qualifications: . Bachelors degree from any stream Required Skills: . Proficiency in MS...	Data Analysis, Business Analytics, MIS, Data Extraction, Advanced Excel, Dashboarding, Tableau, Data Analytics
Bluestone.com	3.8	Not disclosed	2-4 Yrs	Bengaluru	14 Days Ago	Educational Qualifications: 2-4 years of experience in data analysis or related fields,...	Data Analysis, develop dashboards, Data Management, Data Visualization, Data Extraction, Data Analytics, Dashboard Development, Development
Vgen Software Solutions		Not disclosed	0-5 Yrs	Coimbatore	9 Days Ago	Timing: US Shift Timings . Advanced proficiency in Excel (including formulas, pivot tab...	Pivot Table, MS Excel, VLOOKUP, Advanced Excel, HLOOKUP, Communication Skills, Countif, MySQL
Koya Consulting Inc		Not disclosed	3-6 Yrs	Bengaluru	Just Now	Bachelor s degree in Computer Science, Mathematics, or related fieldExperience or speci...	Computer science, Usage, PDF, Senior Analyst, Analytical, Programming, Data Analyst, Management
Global Pharma Tek	3.1	Not disclosed	6-8 Yrs	Hyderabad	1 Day Ago	7+ years of experience building and managing data-related solutions, preferably in the ...	Alteryx, ecosystem management, ADLS, CRM Analytics, DBT, Snowflake, Tableau, Databricks
Quest Global Technologies	4.0	Not disclosed	2-5 Yrs	Bengaluru	1 Day Ago	Develop and maintain global quality dashboards that provide insight into product qual...	Product quality, Analytical skills, Data analysis, Agile development, Web development, data integrity, data visualization, SQL
Cowrks	3.6	Not disclosed	2-5 Yrs	Bengaluru	1 Day Ago	Bengaluru, Full Time. Bachelor s degree in Data Science, Statistics, Computer Science, ...	Analytical skills, Data analysis, Report writing, power bi, Data Analyst, Manager Quality Control, Monitoring, SQL
FedEx TSCS (India) Pvt Ltd	4.1	Not disclosed	2-4 Yrs	Gurugram, Karnal, Bengaluru	1 Day Ago	"> Description   At FedEx, a data analyst is a pivotal member of the core analytics t...	Computer science, Data analysis, fedex, Data modeling, Genetics, Wellness, Data Analyst, Business solutions
Quantiphi Analytics Solutions	3.1	Not disclosed	1-4 Yrs	Bengaluru	2 Days Ago	. Analytical Skills Required: . BigQuery, Tableau . Python OR Javascript OR Typescript ...	Automation, Data management, Sales operations, Javascript, power bi, data integrity, Forecasting, Catering
Indus Towers	3.9	4-6.5 Lacs PA	2-7 Yrs	Bhubaneswar	2 Days Ago	Preferred candidate profile . B Tech with DISCOM backgroundPreparing and circulating va...	Data Analysis, Telecom Infra Knowledge., MS-PowerPoint, MS-Excel, Analytical Skills, MS- word, Data Reporting, Word
Zbiz Solutions		Not disclosed	0-3 Yrs	Kolkata, Mumbai, New Delhi, Hyderabad, Pune, Chennai, Bengaluru	27 Days Ago	Bachelors degree in a relevant field (e.g., Linguistics, International Relations, Data ...	excelgoogle apps script, data analytics, writingdata science, communication skills, statistics, Application, Scripting, Science
Maneva Consulting is a one-stop HR solution		Not disclosed	5-10 Yrs	Hyderabad, Bengaluru	Few Hours Ago	Required Skills: . Analytical & Communication Skills: Ability to explain data findings ...	Data Analyst, Ai Techniques, KPI, Complex Data Management, Stakeholder Analysis, Data Cleansing, Data Collection, Framework Development
CGI	4.1	Not disclosed	5-7 Yrs	Bengaluru	6 Days Ago	Salesforce Background Preferred	Data analysis, Business consulting, French, Sales, CGI, Cloud, Manager Technology, Data Analyst
Abad Fisheries	4.3	Not disclosed	3-5 Yrs	Kochi(Thoppumpady )	2 Days Ago	Technical writing experience in relevant areas, including queries, reports, and present...	Data Visualizations, Data Management, Data Analysis, Data Analytics, Data Extraction, Data Reporting, Analytics, Analysis
Deloitte	3.9	Not disclosed	5-10 Yrs	Gurugram, Delhi / NCR	2 Days Ago	Skills required - Advanced SQL, Big Data, Hive, Experience working on big datasets, Que...	data analyst, Hive, Python, Data, Data analysis
E-solution Point		Not disclosed	1-3 Yrs	Chennai	7 Days Ago	E-SOLUTION POINT is looking for Data Analyst to join our dynamic team and embark on a r...	master data, metadata, python, data analysis, data management, data analytics, data validation, configuration
Sheer Analytics and Insights Private Limited	2.2	Not disclosed	2-5 Yrs	Kolkata	7 Days Ago	As a Data Analyst, you will be responsible for collecting, analyzing, and interpreting...	python, data analysis, data analytics, data mining, predictive analytics, business analysis, market research, machine learning
Ganesh housing corporation limited	5.0	6-15 Lacs PA	3-5 Yrs	Ahmedabad	8 Days Ago	Role & responsibilities  Role & responsibilitiesConduct thorough research by extracting...	Data Analysis, Data Quality, Data Management, Data Extraction, Data Cleansing, Market Analysis, Data Analytics, Data Reporting
Bm2k Global	3.5	Not disclosed	5-8 Yrs	Noida	8 Days Ago	Education: Bachelors degree in data science, Statistics, Mathematics, Computer Science,...	Power Bi, SQL Database, Data Analytics, Yardi, MRI, Data Extraction, Data Cleansing, property management tools
Nsight Consulting	3.4	Not disclosed	2-7 Yrs	Gurugram	9 Days Ago	Bachelors degree in a Computer Science, Mathematics or Scientific discipline . 2+ years...	Computer science, Analytical skills, MIS reporting, Data validation, PDF, Excel, Advanced Excel, Data analytics
Nsight Consulting	3.4	Not disclosed	2-7 Yrs	Gurugram	9 Days Ago	Bachelors degree in a Computer Science, Mathematics or Scientific discipline . 2+ years...	Computer science, Analytical skills, MIS reporting, Data validation, PDF, Excel, Advanced Excel, Data analytics
Armanino		Not disclosed	3-8 Yrs	Ahmedabad	10 Days Ago	Requirements: . BS / BA in IT, Data Science, related major or equivalent work experienc...	Data Analytics, Power BI, Alteryx, SQL, Data, Analytics, Bi, Data analysis
Newvision Software & Consultancy	3.7	Not disclosed	3-6 Yrs	Pune	8 Days Ago	Demonstrated experience in creating dashboards. Experience in automating repetitive tas...	hlookup, macros, data analysis, data management, data analytics, data validation, pivot table, power bi
NewVision Softcom &amp;amp;amp;amp; Consultancy	3.7	Not disclosed	3-6 Yrs	Pune	8 Days Ago	Demonstrated experience in creating dashboards. Experience in automating repetitive tas...	hlookup, macros, data analysis, data management, data analytics, data validation, pivot table, power bi
Successcatalyst Techservices		50,000-3 Lacs PA	1-3 Yrs	Pune	1 Day Ago	Job Descriptions: 1. Utilize SQL to extract, manipulate, and analyze data from various ...	Data Analytics, Python, SQL, Analytics, Data, Data analysis
Impetus		Not disclosed	3-6 Yrs	Hybrid - Pune, Gurugram	7 Days Ago	Experience Level . Post-Graduation : minimum 2 years of relevant work experience Gradua...	Excel, Tableau, Python, SQL, Power Bi, Regression Anaytics, Data Analytics, Bi
Cybernetic Management Professionals		6.5-8 Lacs PA	3-5 Yrs	Noida	1 Day Ago	Data experience, IT&D, various departments	Power Bi, Azure DataWarehouse, Data Analytics, Data, Analytics, Azure Data Warehouse, Bi, Data warehousing
Fortune Global 500 Company Engg. & Construction		Not disclosed	5-7 Yrs	Hybrid - Chennai	7 Days Ago	Qualifications: . Bachelors degree in Data Science, Computer Science, Statistics, or a ...	Tableau, AWS, Python, SQL, Data analysis, Data
Sumtotal Systems	4.0	Not disclosed	2-7 Yrs	Hyderabad	1 Day Ago	Bachelor s degree in quantitative field - engineering, finance, data science, statistic...	Leadership development, Sales operations, data science, Business analysis, Customer retention, Customer engagement, Operations, Salesforce
Maxverbal		Not disclosed	1-3 Yrs	Coimbatore	Just Now	Adequate experience working with large data files and comparing datasets. Ability to pr...	Rework, Automation, Service level, Quality improvement, VLOOKUP, Legal, Database, data integrity
RightWave InfoSolutions (Pvt) Ltd.	3.5	Not disclosed	3-8 Yrs	Noida	Just Now	Not only do we provide competitive compensation, but our employees have the opportunity...	Process design, Google Analytics, Linguistics, Market research, Data quality, Data Analyst, Reporting tools, CRM
BP INCORPORATE INTERNATIONAL.		Not disclosed	1-3 Yrs	Pune	Few Hours Ago	Responsible for providing customer service support to help to ensure maximum customer s...	Procurement, Excel, Business process improvement, Conflict management, Analytical, Customer service, Budgeting, Merchandising
BP INCORPORATE INTERNATIONAL.		Not disclosed	1-4 Yrs	Pune	Few Hours Ago	As bp transitions to an integrated energy company, we must adapt to a changing world an...	Procurement, Demand planning, Analytical, Budgeting, Customer service, Customer experience, Merchandising, Continuous improvement
Adesso India	4.0	Not disclosed	4-9 Yrs	Kochi, Pune, Chennai	1 Day Ago	adesso India is looking for an experienced Data Analyst with 4-6 years of expertis...	Mining, Data analysis, Architecture, Technical Expert, Data modeling, Analytical, Data Analyst, SQL
ION	3.5	Not disclosed	2-5 Yrs	Mumbai	2 Days Ago	Bachelor s degree in Finance, Computer Science or a related fieldRequired Skills  Other...	Supply chain, electronic trading, Fixed income, Finance, Reconciliation, Data processing, Analytics, Private equity
Bare Associates India		4-8 Lacs PA	2-5 Yrs	Remote	1 Day Ago	Company Profile: BARE International is a US-based, global customer experience consulti...	tabl, python, Excel, Power BI, Domo, powerpoint, Office, Data
Cbts	4.4	Not disclosed	3-8 Yrs	Remote	1 Day Ago	3 or 4 years of college resulting in a bachelors degree or equivalent Website visits to...	Excel, Power Bi, Hubspot, Salesforce, Data, Bi, Data analysis
Crescent Opto	3.9	3-5 Lacs PA	1-3 Yrs	Surat(Sachin)	2 Days Ago	Job Description: Data AnalystLocation: Surat, Gujarat, IndiaJob SummaryThe Data Analys...	Data Analysis, Data Mining, Data Extraction, Data Reporting, Extraction, Reporting, Analysis, Data
Marsh McLennan	4.1	Not disclosed	6-9 Yrs	Hybrid - Mumbai(Powai), Pune(Yerwada)	2 Days Ago	Required Skills: . Proficiency in Structured Query Language (SQL) The ideal candidate w...	R, Data Visualization, ETL, SQL, Python, Data analysis, Data
Lumax Industries	4.0	Not disclosed	3-5 Yrs	Gurugram	2 Days Ago	Academic qualification: Graduate in mathematics, statistics, and / or computer science ...	Data Validation, SAP, Data Visualization, Data Analyst, VLOOKUP, Power Point Presentation, Data analysis, Data
Envoy Global		Not disclosed	1-3 Yrs	Hyderabad	1 Day Ago	Bachelors degree in business, Finance, Data Analytics, or related fieldPresentations sh...	Business communication, Data analysis, Usage, Process improvement, Analytical, Account management, Data Analyst, Customer service
ICON plc	4.2	Not disclosed	2-3 Yrs	Chennai	1 Day Ago	To perform this job successfully, an individual must be able to perform each essential ...	Health insurance, Data analysis, Manager Quality Assurance, XML, Reconciliation, Healthcare, Clinical research, Data Analyst
ICON plc	4.2	Not disclosed	2-3 Yrs	Chennai	1 Day Ago	To perform this job successfully, an individual must be able to perform each essential ...	Health insurance, Data analysis, Manager Quality Assurance, XML, Reconciliation, Healthcare, Clinical research, Data Analyst
Celzene It Services	2.0	4-6.5 Lacs PA	0-1 Yrs	Remote	16 Days Ago	Bachelors degree in Data Science, Operations Management, Logistics, or a related fieldP...	Power Bi, Tableau, Data Analytics, SQL, Python, Data Visualization, Data Cleansing, Healthcare
Magic Infomedia		Not disclosed	0-2 Yrs	New Delhi	30+ Days Ago	Magic Infomedia is looking for Data Analyst to join our dynamic team and embark on a re...	master data, metadata, python, data analysis, data management, data analytics, data validation, configuration
Wipro	3.7	Not disclosed	2-5 Yrs	Hyderabad, Chennai, Bengaluru	10 Days Ago	Source Control system Git Experience. . .	Data Analysis, sql queries, java, oracle, c, git, exadata, golden gate
Volvo Financial Services	4.0	Not disclosed	2-4 Yrs	Bengaluru	8 Days Ago	Transport is at the core of modern society. Imagine using your expertise to shape susta...	Supply chain, Database design, Construction equipment, data privacy, Business strategy, Data mining, microsoft, Financial services
Boston Consulting Group	3.8	Not disclosed	2-4 Yrs	Bengaluru	9 Days Ago	Strong analytics skills with the ability to develop and codify knowledge and provide an...	Data analysis, Data management, Analytical, Consulting, Management consulting, Packaging, Business strategy, Project delivery
Siemens	4.1	Not disclosed	0-6 Yrs	Bengaluru	30+ Days Ago	Bachelor s degree in engineering or science Proficient in SQL for data extraction and m...	Data analysis, Manager Quality Assurance, Data modeling, Analytical, Trend analysis, power bi, Data quality, Forecasting
Response Informatics	3.9	Not disclosed	5-7 Yrs	Kolkata, Mumbai, New Delhi, Hyderabad, Pune, Chennai, Bengaluru	6 Days Ago	Understanding cloud-based data storage, processing, and analytics is a plus. Adaptabili...	Statistical analysis, MySQL, Machine learning, Senior Data Analyst, Hypothesis Testing, microsoft azure, data visualization, Regression analysis
George Bernard Consulting		Not disclosed	2-4 Yrs	Kolkata, Mumbai, New Delhi, Hyderabad, Pune, Chennai, Bengaluru	2 Days Ago	Bachelor s or master s degree in computer science, information systems or related field...	Computer science, Data analysis, Manager Quality Assurance, Coding, Project management, Machine learning, Financial services, SQL
Firstmeridian Global Services	4.0	50,000-3 Lacs PA	2-4 Yrs	Hyderabad	3 Days Ago	Proficient in managing and prioritizing workloads to meet deadlines and deliver results	Tableau, Sharepoint, Excel, Power Bi, power point, Bi, Data analysis, Data
Norstella	3.6	Not disclosed	1-3 Yrs	Kolkata, Mumbai, New Delhi, Hyderabad, Pune, Chennai, Bengaluru	3 Days Ago	Description. About Norstella. At Norstella, our mission is simple: to help our clients...	insurance, python, data analysis, business requirements, us healthcare, predictive analytics, documentation, business analysis
Celeros Flow Technology	3.7	Not disclosed	3-6 Yrs	Bengaluru	3 Days Ago	Excellent communication skills. Education and Experience . BE mechanical / industrial /...	Global sourcing, ERP, SAP, Google Analytics, Web analytics, Pumps, Production engineering, Valves
Ugam	3.6	7-11 Lacs PA	3-7 Yrs	Hybrid - Bengaluru, Mumbai (All Areas)	5 Days Ago	Cleaning and organising data to ensure accuracy and reliability using tools such as Dat...	Media Analytics, Power Bi, SQL Queries, Tableau, Python, Media, Analytics, Query
Apptad	3.7	Not disclosed	7-12 Yrs	Bengaluru, Delhi / NCR, Mumbai (All Areas)	7 Days Ago	Proven experience working as a Business System Analyst or similar role, with a focus on...	Azure, Data Analyst, SQL, MDM, Snowflake, customer matching techniques, GDPR, CCPA
Target	4.2	Not disclosed	2-4 Yrs	Bengaluru	2 Days Ago	The Data & Insights team s mission is to harness the power of data to inform critical d...	Data analysis, metadata, Data management, Business analytics, Analytical, Agile, Property management, Analytics
Bernhard Schulte Shipmanagement India	4.2	Not disclosed	1-5 Yrs	Kochi, Thrissur, Kozhikode, Thiruvananthapuram	10 Days Ago	Data (Experience in data analysis with programmingtool is an added advantage) . .	Health insurance, Career development, Data analysis, ERP, Operational excellence, RDBMS, Data quality, Data Analyst
Deutsche Bank	4.0	Not disclosed	1-5 Yrs	Jaipur	14 Days Ago	The KYC Analyst provides regular communication to senior bank stakeholders on changes i...	data analysis, AML, KYC, client onboarding, Client, Data, Analysis, Onboarding
Cognizant	3.8	Not disclosed	7-11 Yrs	Hybrid - Hyderabad, Bangalore Rural, Chennai	22 Days Ago	Ex- employee of cognizant(yes / no): . Will be validating the response and proceed it a...	Data Analysis, SQL, Data Analytics, Analysis, Data, Analytics
Nits Solutions	3.0	Not disclosed	2-7 Yrs	Hybrid - Delhi / NCR	4 Days Ago	*Develop and implement databases, data collection systems, data analytics and other str...	Data Analyst, Python, Data Analysis, Data Analytics, SQL, Data, Analytics, Analysis
Neura Monks		Not disclosed	1-4 Yrs	Ahmedabad	3 Days Ago	Job Description:We are looking for a Data Scientist who is proficient in data manipulat...	Data Analysis, BigQuery, PostgreSQL, AWS Glue, ETL, Python, Glue, Analysis
Sandoz	4.0	Not disclosed	2-4 Yrs	Hyderabad	6 Days Ago	The incumbent would be expected to demonstrate good business domain understanding, abil...	Supply chain, Procurement, Stakeholder Engagement, Data modeling, Analytical, Data quality, Digital marketing, MS Office
Invest4edu	3.0	Not disclosed	1-3 Yrs	Indore, Hyderabad	2 Days Ago	Managing master data, including creation, updates, and deletion.   Managing users and...	HTML, Data Analyst, Windows, Microsoft Windows, Data analysis, Data
Lab49	3.1	Not disclosed	2-5 Yrs	Mumbai	3 Days Ago	Solid experience with Microsoft Excel. . High monotony tolerance and ability to catch n...	Supply chain, data cleansing, Automation, electronic trading, Excel, Finance, Workflow, Data Analyst
Foundever	3.7	50,000-80,000 PA	3-6 Yrs	Remote	3 Days Ago	Preferred candidate profile . Experience with serverless processes and restAPIs. .	Power Query, Dax, SQL, Query, Data analysis, Data
NS Global Corporation		Not disclosed	3-5 Yrs	Rajkot	6 Days Ago	3-5 years of experience in EDI, with a focus on supply chain processes, supplier, and c...	Procurement, Supply chain, Webmethods, SAP, PDF, Analytical, EDI, Middleware
Tripstack	3.4	Not disclosed	4-5 Yrs	Mumbai	7 Days Ago	Willing to learn and adopt new technologies . Good with google spreadsheet/ Google tool...	Automation, Business reporting, data reporting, Strategic partnerships, Online sales, IFS, Data Analyst, Business modeling
Axa Xl	3.7	Not disclosed	2-4 Yrs	Hybrid - Bengaluru(Varthur +2)	1 Day Ago	What will your essential responsibilities include?- Helping Global DP team manage impo...	Excel, data protection, Data Security, Data Privacy, Data analysis, HP data protector, Analysis, Data
ION	3.5	Not disclosed	2-5 Yrs	Mumbai	3 Days Ago	Solid experience with Microsoft ExcelExperience with financial business . Good team pla...	front end, css, c++, python, software development, natural language processing, ui development, golang
Development Alternatives	2.7	Not disclosed	2-7 Yrs	New Delhi	4 Days Ago	Bachelor s degree in Data Science, Statistics, Social Sciences, or a related field . 2+...	Analytical skills, Data analysis, data science, data manipulation, Analytical, Strategic planning, Data collection, Data Analyst
Energy Aspects	4.3	Not disclosed	2-3 Yrs	Kolkata	4 Days Ago	Excellent command of written and spoken English . Master s or Bachelor s university deg...	data cleansing, Trade, Maritime, Commodity trading, Data quality, Data Analyst, SQL, Python
Simplotel Technologies	2.9	Not disclosed	0-1 Yrs	Bengaluru	28 Days Ago	Job Overview :As a Data Automation Analyst, you will work closely with stakeholders to ...	ETL, Data Integrity, Data Pipeline, RDBMS, Statistical Modeling, Data Mining, Data Analyst, Data Warehousing
Agilite Global Solutions	4.0	Not disclosed	0-3 Yrs	Kolkata, Mumbai, New Delhi, Hyderabad, Pune, Chennai, Bengaluru	30+ Days Ago	Experience and desire to work in a global delivery model from a permanent work from hom...	Health insurance, Claims, Provident fund, Pharma, Analytical, Machine learning, Agile, Life sciences
Hexaconcepts		Not disclosed	2-6 Yrs	Kolkata, Mumbai, New Delhi, Hyderabad, Pune, Chennai, Bengaluru	30+ Days Ago	Actively seeking talented Data Scientists & Analysts proficient in Python to join the t...	Computer science, Analytical skills, Data analysis, Artificial Intelligence, Consulting, Data Analyst, Silicon, Data analytics
Net2Source LLP		5-12 Lacs PA	4-7 Yrs	Chennai	7 Days Ago	Qualifications: Bachelors degree in Aeronautical or Mechanical Engineering or any speci...	NLP, Ecommerce, Natural language processing, SQL, Python, E-commerce, Data analysis, Processing
MNC Group		8-10 Lacs PA	6-9 Yrs	Hybrid - Gurugram	2 Days Ago	All our emails will be sent from official domain only - @persolkelly.com.We are not lia...	advance excel, Data Analysis, Bi Tools, Tableau, data analyst, Excel, Bi, Tools
Leading Client		Not disclosed	1-3 Yrs	Bengaluru	1 Day Ago	Qualifications: . Education level: Bachelors degree in finance, accounting, or a releva...	Data Classification Analysis, software development, UAT, SQL, Python, Data analysis, Software, Analysis
Provakil Technologies	3.6	2.5-4.5 Lacs PA	0-2 Yrs	Mumbai	10 Days Ago	0 - 2 years of experience as a Data Analyst or relevant roles. Collect, clean, and anal...	Excel, Data Analysis, Data Cleansing, Data Collection, Pivot Table, VLOOKUP, MS Office, Cleansing
Disha Consultant		Not disclosed	2-4 Yrs	Pune, Chennai, Jaipur, Bengaluru	30+ Days Ago	Key skills and Experience: Minimum 2 years of Data Analysis experience and SQL query wr...	Data analysis, Data validation, Data management, Data analytics, Advanced Excel, Data Analyst, data visualization, Management
Neuralix.ai		Not disclosed	2-6 Yrs	Bengaluru	9 Days Ago	Bachelor s degree in Data Science, Statistics, Computer Science, Mathematics, or a rela...	Computer science, Data analysis, Trend analysis, Machine learning, Data collection, Predictive modeling, Data quality, Forecasting
![image](https://github.com/user-attachments/assets/2946e8f0-72d5-4460-89b6-d89b9f5a6965)


  


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

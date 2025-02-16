# Description

A web-based project that simulates a hospital and its patients

## Functionalities

### Data Sources and Retrieval

- Retrieve data from an extensive, high-quality data set [MIMIC-IV](https://www.nature.com/articles/s41597-022-01899-x):
  - real data sourced from the electronic health record of the Beth Israel Deaconess Medical Center
  - very extensive data set that required advanced data cleaning and evaluation based on our requirements
  - can be adjusted to our custom database architecture
  - access is provided via PhysioNet
  - anonymised data set
- Generate a data set for the doctors

### Data Storage and Handling

- Store the data from the external source in an SQL database
  - create a concept for the database architecture and necessary information required for the software
- Store Log-In information by hashing passwords
  - use built-in library [hashlib](https://docs.python.org/3/library/hashlib.html)
  - because our passwords don't need to be moved or send to another server, hashing is a good choice to safeguard sensible information

### User Management

- Log-In system
  - Patients
    - [subject_id, gender, anchor_age, anchor_year, anchor_year_group, dod, firstname, surname]
    - view and modify **only** their data
    - view a doctors profile
  - Admins
    - [subject_id, firstname, surname, email]
    - view-only access to all profiles
    - able to modify data upon user request
    - also used for data analysis purposes
    - Create/Delete accounts upon request
  - Doctors
    - [subject_id, age, firstname, surname, department, dob]
    - view **only** their patients data and add medical data to their profile (patients that are assigned to them)
    - view a doctors profile
    - view and modify their own profile
- Timed Log-Out
  
### Interface

- Create a GUI
  - Log-In portal
  - Home screen, view profile, help page, analysis page
  - depending on user the home screen and available functions change
- Dashboard for results of data analysis

### Statistical Analysis

- Users can access a dashboard that displays analysed data
  - Patients can view data regarding their own medical conditions and medications
  - Doctors can view data about all patients

### Visualizations

- Display the data from [Statistical Analysis](#statistical_analysis) with simple graphs
  - add an interactive graph to filter for $${\color{pink}(Low \space priority)}$$
    - patient profiles (age, gender, etc.)
    - time periods
    - medical conditions, medications, etc. 

## Installation and Usage

### SQL Server Setup

The system requires a working instance of our database running on your local machine. Restore the [database backup](database1.zip) according to the official [Quickstart guide](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/quickstart-backup-restore-database?view=sql-server-ver16&tabs=ssms).  

## Timeline

![screenshot](Timeline.png)

## Group Details

- Group name: Lank
- Group code: G12
- Group repository: <https://github.com/lefischerander/Lank>
- Tutor responsible: Jonas Rieling
- Group team leader: Leander Fischer
- Group members: Konstantin Kolbek, Erik Schäfer, Nantenaina Razafindraibe
- Contributions
  - Leander Fischer:
    - Data Source and Retrieval
    - Data Storage and Handling
    - User Management
      - Database related functions
    - Statistical Analysis
      - Data retrieval into pandas DataFrames
  - Konstantin Kolbek
    - Statistical Analysis
    - Visualization
    - User Management
      - Log-In
      - Actions
  - Nantenaina Razafindraibe
    - User Management
  - Erik Schäfer
    - Interface

## Acknowledgements

### MIMIC-IV

- MIMIC-IV Clinical Database Demo <https://physionet.org/content/mimic-iv-demo/2.2/>
- Johnson, A., Bulgarelli, L., Pollard, T., Gow, B., Moody, B., Horng, S., Celi, L. A., & Mark, R. (2024). MIMIC-IV (version 3.1). PhysioNet. <https://doi.org/10.13026/kpb9-mt58>
- MIMIC Online Documentation <https://mimic.mit.edu/>

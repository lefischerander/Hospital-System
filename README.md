# Description

A GUI-based project that simulates a hospital and its patients

## Functionalities

### Data Sources and Retrieval

- Retrieved data from the extensive, high-quality data set [MIMIC-IV](https://www.nature.com/articles/s41597-022-01899-x):
  - real data sourced from the electronic health record of the Beth Israel Deaconess Medical Center
  - very extensive data set that required data cleaning and evaluation based on our requirements
  - can be adjusted to our custom database architecture
  - anonymised data set

### Data Storage and Handling

- The MIMIC-IV data is stored in an SQL database (SQL Server)
- Log-In information stored securely by hashing passwords
  - used built-in library [hashlib](https://docs.python.org/3/library/hashlib.html)
  - because our passwords don't need to be moved or sent to another server, hashing is a good choice to safeguard sensible information

### User Management

- Log-In system
  - All users can
    - view basic visualizations of analysis made on all patients
    - change their password
  - Patients
    - [subject_id, gender, anchor_age, anchor_year, anchor_year_group, dod, firstname, surname]
    - view and download **only** their data
  - Admins
    - [subject_id, firstname, surname, email]
    - view-only access to all profiles
    - view patients data
    - create/delete accounts
  - Doctors
    - [subject_id, age, firstname, surname, department, dob]
    - view patients data and add medical data to their profiles
    - view their profile
- Timed Log-Out
  
### Interface

- Created a GUI
  - log-In portal
  - home screen, view profile, help page, analysis page, change password, delete/create user
  - depending on user the home screen and available functions change
- various visualizations of data can be accessed on the analysis page

### Statistical Analysis

- Users can access a dashboard that displays analysed data
  - patients can view data regarding their own medical conditions and medications
  - doctors can view data about all patients
  - all users can view non-identifying visualizations of analysis made on all patients

### Visualizations

- Display the data from [Statistical Analysis](#statistical-analysis) with simple graphs

## Installation and Usage

### SQL Server Setup

The system requires a working instance of our database running on your local machine. Install SQL Server and SQL Server Management Studio accoring to the offical [Installation guide](https://learn.microsoft.com/de-de/sql/database-engine/install-windows/install-sql-server?view=sql-server-ver16). After establishing a connection to your local database, restore the [database backup](Miscellaneous/database_final.zip) according to the official [Quickstart guide](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/quickstart-backup-restore-database?view=sql-server-ver16&tabs=ssms).

Go to the object explorer and right-click on your server to open the Property window. Move to the Security tab and allow SQL-Authentication. Then right click on the Security folder and create a New Login. Input your desired User name and password (Use "LANK_USER" as a User name and "Lank1." to mirror our setup) and unselect "Enforce password policy". Under Server Roles, give the user the public role. Under User Mapping, check the box next to your database (LANK) and grant the db_datareader and db_datawriter role to the user. Click on OK and restart your server.

Adjust [db.access](Backend/Database/db_access.py) with your local instance's database information. The program will now use your local database. The program can now be started by running main.py.

## Data Flow Diagram

![screenshot][dfd]
## Timeline

![screenshot][timeline]

## Group Details

- Group name: Lank
- Group code: G12
- Group repository: <https://github.com/lefischerander/Lank>
- Tutor responsible: Jonas Rieling
- Group team leader: Leander Fischer (subsequently L)
- Group members: Konstantin Kolbek (subsequenly K), Erik Schäfer (subsequenly E), Nantenaina Razafindraibe (subsequenly N)
- Contributions
  - Leander Fischer: Sourced and cleaned the data from PhysioNet and developed the storage solution. Helped K and N by providing SQL queries for their functions accessing the database. Supported K and N by writing some utility functions in database_service and analyse. Helped E fix Interface bugs when accessing and displaying data from the database. Refactored the entire project to adhere to the final project structure. Developed unit tests.
  - Konstantin Kolbek: Supported L to determine what data should be sourced from MIMIC-IV. Worked with N on the login functionalities. Developed the data analysis and visualization. 
  - Nantenaina Razafindraibe: Developed the interface between the program and database (database_service). Worked with K on the login functionalities. Helped L develop the unit tests.
  - Erik Schäfer: Developed the User Interface. Edited Backend code to make it compatible with user inputs.

## Acknowledgements

### MIMIC-IV

- MIMIC-IV Clinical Database Demo <https://physionet.org/content/mimic-iv-demo/2.2/>
- Johnson, A., Bulgarelli, L., Pollard, T., Gow, B., Moody, B., Horng, S., Celi, L. A., & Mark, R. (2024). MIMIC-IV (version 3.1). PhysioNet. <https://doi.org/10.13026/kpb9-mt58>
- MIMIC Online Documentation <https://mimic.mit.edu/>

[timeline]: Miscellaneous/Timeline.png
[dfd]: Miscellaneous/lank_dfd.png

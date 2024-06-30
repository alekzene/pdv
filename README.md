# On-Premise H1B Visa Data Analysis Tool  

### Tools Used  
* Python  
* Git / GitHub  
* Visual Studio Code  
* Windows Subsystem for Linux  
* SQL Server 2022 (Developer)  
* SQL Server Integration Servcies (SSIS)    

### Concepts  
* Domain Knowledge: Employment, Immigration, H1B Visas  
* FTP: File Transfer Protocol  
* ETL: Extract-Transform-Load Pipeline

### ETL Project Specifications
* **Project Source**: Dashboard, report  
* **Data Source**: H1B Employer Data Hub (United States Citizenship and Immigration Services - USCCIS) .CSV  
* **Data Load Type**: Full load
* **Data Refresh**: Yearly

### Recommendations  
* Migrate to cloud  
* Use API for data extraction  

### Log  
* Jun 19: set up environment  
* Jun 24: data gathering, setup wsl  
* Jun 25: set up ftp server  
* Jun 26: schedule data retrieval pipeline   
* Jun 30: connect ftp to postgresql  
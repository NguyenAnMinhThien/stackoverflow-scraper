# Stackoverflow-Scraper
Stackoverflow is a very popular website for all common questions in programming, coding tips, shared knowledge. If you have a look at many common questions when you start to learn about a subject, that may reduce your time when you deploy the project later.

This script will scrape the questions on stackoverflow and sort base on the number of votes. The user can scrape multiple tags or one tag and it will output a file csv contain all info about the questions relate to these tags.
# How to use:
Clone the repository and navigate to stackoverflow-scraper dir:
```
git clone https://github.com/NguyenAnMinhThien/stackoverflow-scraper.git
```
```
cd stackoverflow-scraper
```
If you want to use virtual env, follow these steps:
  
  1. Create virtual env
  ```
  python -m venv venv
  ```
  2. Activate the venv:

  - For WindowPowerShell terminal:
  ```
  .\venv\Scripts\activate.ps1
  ```
  - Or Bash terminal:
  ```
  source venv/bin/activate
  ```
  3. Install the required packages:
   ```
     pip install -r requirement.txt
   ```
   
Run the code:
```
python main.py
```
Example:

![input-example](https://github.com/user-attachments/assets/3b19f2e6-47e1-4a9f-9347-6e88c78e5112)

![windows-javascript-2p](https://github.com/user-attachments/assets/992ae06f-a42e-421e-be97-fcd0eb243c10)

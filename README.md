# Stackoverflow-Scraper
Stack Overflow is a very popular website for all common questions in programming, coding tips, shared knowledge. If you have a look at many common questions when you start to learn about a subject, that may reduce your time when you deploy the project later.

This script will scrape the questions on Stack Overflow and sort base on the number of votes. The user can scrape multiple tags or one tag and it will output a file CSV contain all info about the scraped questions.
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
> [!NOTE]
> If you can not excute the script, it may dueto you still not change the excution policy. Reference [about_Execution_Policies](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.4) to know more.
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

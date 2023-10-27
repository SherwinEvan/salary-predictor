# Full Stack Developer Salary Estimator: Project Overview 
* Created a tool that estimates full stack developer salaries (MAE ~ Rs. 80K) to help full stack developers negotiate their income when they get a job.
* Scraped 1200+ job descriptions from glassdoor using Python and Selenium.
* Engineered features from the text of each job description to quantify the value companies put on TypeScript, React, Angular, Vue, SCSS/SASS,
  PHP, Laravel, WordPress, Ruby, Ruby on Rails, .NET, Node.Js, Spring, Spring Boot, MySQL, NoSQL, PostgreSQL, MongoDB, and Django. 
* Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model. 
* Built a client facing API using flask.

## Code and Resources Used 
**Python Version:** 3.9  
**Packages:** pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle  
**For Web Framework Requirements:**  ```pip install -r requirements.txt```  

## Web Scraping
I bulit a python selenium web scraper as the ones available on the internet already did not work as they were outdated since GlassDoor updated their website.
Web scraped 1200+ job postings from glassdoor.com. With each job, we got the following:
*	Job title
*	Salary Estimate
*	Job Description
*	Rating
*	Company 
*	Location
*	Company Size
*	Company Founded Year
*	Type of Ownership 
*	Industry
*	Sector
*	Revenue
*	Career Opportunities
*	Comp & Benifits
*	Culture & Values
*	Senior Management
*	Work/Life Balance

## Data Cleaning
After scraping the data, I needed to clean it up so that it was usable for our model. I made the following changes and created the following variables:

*	Parsed numeric data out of salary 
*	Made columns for employer provided salary and hourly wages 
*	Removed rows without salary 
*	Parsed rating out of company text 
*	Made a new column for company age
*	Made columns for if different skills were listed in the job description:
    * TypeScript 
    * React
    * Angular  
    * Vue
    * SCSS/SASS
    * PHP
    * Laravel
    * WordPress
    * Ruby
    * Ruby on Rails
    * .NET
    * Node.js
    * Spring
    * Spring Boot
    * MySQL
    * NoSQL
    * PostgreSQL
    * MongoDB
    * Django
*	Added a column for simplified job title and Seniority 
*	Added a column for description length 

## EDA
I looked at the distributions of the data and the value counts for the various categorical variables. Below are a few highlights from the pivot tables. 

![alt text](https://github.com/SherwinEvan/salary-predictor/blob/78bd386ca4a0ebabbe7d4e6369f1fb90daf41e5f/Images/avg_sal_table.png)
![alt text](https://github.com/SherwinEvan/salary-predictor/blob/78bd386ca4a0ebabbe7d4e6369f1fb90daf41e5f/Images/correlation.png)
![alt text](https://github.com/SherwinEvan/salary-predictor/blob/78bd386ca4a0ebabbe7d4e6369f1fb90daf41e5f/Images/heatmap.png)
![alt text](https://github.com/SherwinEvan/salary-predictor/blob/78bd386ca4a0ebabbe7d4e6369f1fb90daf41e5f/Images/location_graph.png)

## Model Building 

First, I transformed the categorical variables into dummy variables. I also split the data into train and tests sets with a test size of 20%.   

I tried three different models and evaluated them using Mean Absolute Error. I chose MAE because it is relatively easy to interpret and outliers aren’t particularly bad in for this type of model.   

I tried three different models:
*	**Multiple Linear Regression** – Baseline for the model
*	**Lasso Regression** – Because of the sparse data from the many categorical variables, I thought a normalized regression like lasso would be effective.
*	**Random Forest** – Again, with the sparsity associated with the data, I thought that this would be a good fit. 

## Model performance
The Random Forest model far outperformed the other approaches on the test and validation sets. 
*	**Linear Regression**: MAE = 4.02
*	**Lasso Regression**: MAE = 3.23
*	**Random Forest** : MAE = 0.80

## Productionization 
In this step, I built a flask API endpoint that was hosted on a local webserver. The API endpoint takes in a request with a list of values from a job listing and returns an estimated salary. 



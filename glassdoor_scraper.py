# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 16:14:20 2023

@author: Sherwin
"""


from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import time
import pandas as pd


def get_jobs(keyword, num_jobs, verbose, driver_path):
    
    '''Gathers jobs as a dataframe, scraped from Glassdoor'''
    
    #Initializing the webdriver
    options = webdriver.ChromeOptions()
    
    #Uncomment the line below if you'd like to scrape without a new Chrome window every time.
    #options.add_argument('headless')

    #Change the path to where chromedriver is in your home folder.
    driver = webdriver.Chrome(executable_path=driver_path, options=options)
    driver.set_window_size(1120, 1000)

    
    #url = 'https://www.glassdoor.co.in/Job/india-' + keyword + '-jobs-SRCH_IL.0,5_IN115_KO6,26.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=full&typedLocation=India&context=Jobs&dropdown=0'
    #url = 'https://www.glassdoor.co.in/Job/india-full-stack-developer-jobs-SRCH_IL.0,5_IN115_KO6,26_IP16.htm?minRating=1.0&includeNoSalaryJobs=true&pgc=AB4AAYEAHgAAAAAAAAAAAAAAAf6711cARQEAAUpPhrIqlyl3%2FyKHZteqlVVKT%2F995OLc7X8%2BVV2T6ZPrl2BvENhyVySMU93yKOhoKvi9caXdbVmddubv6xVMkPXo4AAA'
    url = 'https://www.glassdoor.co.in/Job/india-full-stack-engineer-jobs-SRCH_IL.0,5_IN115_KO6,25.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=full%2520stack%2520e&typedLocation=India&context=Jobs&dropdown=0'
    driver.get(url)
    jobs = []

    while len(jobs) < num_jobs:  #If true, should be still looking for new jobs.

        #Let the page load. Change this number based on your internet speed.
        #Or, wait until the webpage is loaded, instead of hardcoding it.
        time.sleep(4)

        
        #Going through each job in this page
        job_buttons = driver.find_elements_by_css_selector("li.react-job-listing")  #These are the buttons we're going to click.
        print(len(job_buttons))
        
        for job_button in job_buttons:  

            print("\nProgress: {}\n".format("" + str(len(jobs)) + "/" + str(num_jobs)))
            if len(jobs) >= num_jobs:
                break

            job_button.click() 
            time.sleep(3)
            collected_successfully = False
            
            #Test for the "Sign Up" prompt and get rid of it.
            try:
                driver.find_element_by_css_selector('[alt="Close"]').click()  #clicking to the X.
            except NoSuchElementException:
                pass
            
            #Expands the Description section by clicking on Show More
            try:
                driver.find_element_by_xpath('//*[@id="JobDescriptionContainer"]/div[2]').click()
                time.sleep(3)
            except NoSuchElementException:
                print("Error! Cannot find 'Show More' element.\n")
            
            while not collected_successfully:
                try:
                    company_name = driver.find_element_by_xpath('//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[1]/div').text
                    location = driver.find_element_by_xpath('//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[3]').text
                    job_title = driver.find_element_by_xpath('//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[2]').text
                    job_description = driver.find_element_by_xpath('//*[@id="JobDescriptionContainer"]').text
                    collected_successfully = True
                except:
                    time.sleep(5)
                    try:
                        element = driver.find_element_by_xpath('//*[@id="JDCol"]')
                        driver.execute_script("arguments[0].scrollTop = 0;",element)
                        
                        company_name = driver.find_element_by_xpath('//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[1]/div').text
                        location = driver.find_element_by_xpath('//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[3]').text
                        job_title = driver.find_element_by_xpath('//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[2]').text
                        job_description = driver.find_element_by_xpath('//*[@id="JobDescriptionContainer"]').text
                        collected_successfully = True
                    except:
                        pass
            
            #Retreving salary data
            try:
                salary_estimate = driver.find_element_by_xpath('//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[4]/span').text
            except NoSuchElementException:
                salary_estimate = -1
            

            #Printing for debugging
            if verbose:
                print("Job Title: {}".format(job_title))
                print("Salary Estimate: {}".format(salary_estimate))
                print("Job Description: {}".format(job_description[:50]))
                print("Company Name: {}".format(company_name))
                print("Location: {}".format(location))

            #Retreving company data
            try:
                rating = driver.find_element_by_xpath('//*[@id="employerStats"]/div[1]/div[1]').text
            except NoSuchElementException:
                rating = -1
            
            try:
                size = driver.find_element_by_xpath('//*[@id="EmpBasicInfo"]/div[1]/div/div[1]/span[2]').text
            except NoSuchElementException:
                size = -1
            
            try:
                founded = driver.find_element_by_xpath('//*[@id="EmpBasicInfo"]/div[1]/div/div[2]/span[2]').text
            except NoSuchElementException:
                founded = -1
            
            try:
                type_of_ownership = driver.find_element_by_xpath('//*[@id="EmpBasicInfo"]/div[1]/div/div[3]/span[2]').text
            except NoSuchElementException:
                type_of_ownership = -1
                
            try:
                industry = driver.find_element_by_xpath('//*[@id="EmpBasicInfo"]/div[1]/div/div[4]/span[2]').text
            except NoSuchElementException:
                industry = -1
            
            try:
                sector = driver.find_element_by_xpath('//*[@id="EmpBasicInfo"]/div[1]/div/div[5]/span[2]').text
            except NoSuchElementException:
                sector = -1
            
            try:
                revenue = driver.find_element_by_xpath('//*[@id="EmpBasicInfo"]/div[1]/div/div[6]/span[2]').text
            except NoSuchElementException:
                revenue = -1
                
            if verbose:
                print("Size: {}".format(size))
                print("Founded: {}".format(founded))
                print("Type of Ownership: {}".format(type_of_ownership))
                print("Industry: {}".format(industry))
                print("Sector: {}".format(sector))
                print("Revenue: {}".format(revenue))
            
            #Retreving company rating
            try:
                career_opportunities_element = driver.find_element_by_xpath('//*[@id="JDCol"]/div/article/div/div[2]/div[1]/div[4]/div/ul/span[3]')
                career_opportunities = career_opportunities_element.text
            except NoSuchElementException:
                try:
                    career_opportunities_element = driver.find_element_by_xpath('//*[@id="JDCol"]/div/article/div/div[2]/div[1]/div[3]/div/ul/span[3]')
                    career_opportunities = career_opportunities_element.text
                except:
                    career_opportunities = -1
            
            try:
                comp_and_benefits_element = driver.find_element_by_xpath('//*[@id="JDCol"]/div/article/div/div[2]/div[1]/div[4]/div/ul/span[6]')
                comp_and_benefits = comp_and_benefits_element.text
            except NoSuchElementException:
                try:
                    comp_and_benefits_element = driver.find_element_by_xpath('//*[@id="JDCol"]/div/article/div/div[2]/div[1]/div[3]/div/ul/span[6]')
                    comp_and_benefits = comp_and_benefits_element.text
                except:
                    comp_and_benefits = -1
            
            try:
                culture_and_values_element = driver.find_element_by_xpath('//*[@id="JDCol"]/div/article/div/div[2]/div[1]/div[4]/div/ul/span[9]')
                culture_and_values = culture_and_values_element.text
            except NoSuchElementException:
                try:
                    culture_and_values_element = driver.find_element_by_xpath('//*[@id="JDCol"]/div/article/div/div[2]/div[1]/div[3]/div/ul/span[9]')
                    culture_and_values = culture_and_values_element.text
                except:
                    culture_and_values = -1
                
            try:
                senior_management_element = driver.find_element_by_xpath('//*[@id="JDCol"]/div/article/div/div[2]/div[1]/div[4]/div/ul/span[12]')
                senior_management = senior_management_element.text
            except NoSuchElementException:
                try:
                    senior_management_element = driver.find_element_by_xpath('//*[@id="JDCol"]/div/article/div/div[2]/div[1]/div[3]/div/ul/span[12]')
                    senior_management = senior_management_element.text
                except:
                    senior_management = -1
            
            try:
                work_life_balance_element = driver.find_element_by_xpath('//*[@id="JDCol"]/div/article/div/div[2]/div[1]/div[4]/div/ul/span[15]')
                work_life_balance = work_life_balance_element.text
            except NoSuchElementException:
                try:
                    work_life_balance_element = driver.find_element_by_xpath('//*[@id="JDCol"]/div/article/div/div[2]/div[1]/div[3]/div/ul/span[15]')
                    work_life_balance = work_life_balance_element.text
                except:
                    work_life_balance = -1
            
            if verbose:
                print("Career Opportunities: {}".format(career_opportunities))
                print("Comp & Benefits: {}".format(comp_and_benefits))
                print("Culture & Values: {}".format(culture_and_values))
                print("Senior Management: {}".format(senior_management))
                print("Work/Life Balance: {}".format(work_life_balance))
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            

            jobs.append({"Job Title" : job_title,
            "Salary Estimate" : salary_estimate,
            "Job Description" : job_description,
            "Rating" : rating,
            "Company Name" : company_name,
            "Location" : location,
            "Size" : size,
            "Founded" : founded,
            "Type of ownership" : type_of_ownership,
            "Industry" : industry,
            "Sector" : sector,
            "Revenue" : revenue,
            "Career Opportunities" : career_opportunities,
            "Comp & Benefits" : comp_and_benefits,
            "Culture & Values" : culture_and_values,
            "Senior Management" : senior_management,
            "Work/Life Balance" : work_life_balance})
            #add job to jobs

        #Clicking on the "next page" button
        try:
            driver.find_element_by_xpath('//*[@id="MainCol"]/div[2]/div/div[1]/button[7]').click()
        except NoSuchElementException:
            print("Scraping terminated before reaching target number of jobs. Needed {}, got {}.".format(num_jobs, len(jobs)))
            break
    
    df = pd.DataFrame(jobs)
    
    df.to_csv('{}_2_min_rating_1.csv'.format(keyword))

    return df
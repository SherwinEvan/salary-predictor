# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 22:43:39 2023

@author: Sherwin
"""

import pandas as pd

df = pd.read_csv('full-stack.csv')

#Deleting the Unnamed first column
df.columns
df = df.drop(['Unnamed: 0'], axis = 1)

#Count duplicate rows
df.duplicated().value_counts()

dups = df.groupby(df.columns.tolist()).size().reset_index().rename(columns={0:'count'})
dups['count'].sum() - dups.shape[0]

df.groupby(df.columns.tolist(),as_index=False).size()
len(df)-len(df.drop_duplicates())

#Removing rows with no 'Salary Estimate'
df = df[df['Salary Estimate'] != '-1']

#Cleaning 'Salary Estimate' column
df['Per Hour'] = df['Job Description'].apply(lambda x : 1 if 'per hour' in x.lower() else 0)
df['Monthly'] = df['Job Description'].apply(lambda x : 1 if 'per month' in x.lower() else 0)
df['Employer Provided'] = df['Salary Estimate'].apply(lambda x : 1 if 'employer provided salary' in x.lower() else 0)

salary = df['Salary Estimate'].apply(lambda x : x.split('(')[0])
minus_Lr = salary.apply(lambda x : x.replace(' Per hour','').replace('Employer Provided Salary:','').replace('L', '').replace('T','').replace('₹', ''))

df['Min Salary'] = minus_Lr.apply(lambda x : int(float(x.split(' - ')[0].replace(',',''))))
df['Max Salary'] = minus_Lr.apply(lambda x : int(float(x.split(' - ')[1].replace(',',''))) if ' - ' in x else int(float(x)))
df['Avg Salary'] = (df['Min Salary'] + df['Max Salary']) / 2

#Removing Rating from 'Company Name'
df['Company'] = df.apply(lambda x : x['Company Name'] if x['Rating'] < 0 else x['Company Name'][: -3], axis = 1)

#Age of Company
df['CFounded'] = df['Founded'].str.replace('^(?!-1|\d{4}$).+', '', regex = True)
df['CFounded'] = pd.to_numeric(df['CFounded'])
df['CFounded'] = df['CFounded'].fillna(-1)
df['Age'] = df['CFounded'].apply(lambda x : x if x < 1 else 2023 - x)

#Parsing 'Job Description'
df['Need TypeScript'] = df['Job Description'].apply(lambda x : 1 if 'typescript' in x.lower() else 0)
df['Need React'] = df['Job Description'].apply(lambda x : 1 if 'react' in x.lower() or 'reactjs' in x.lower() or 'react.js' in x.lower() else 0)
df['Need Angular'] = df['Job Description'].apply(lambda x : 1 if 'angular' in x.lower() or 'angularjs' in x.lower() or 'angular.js' in x.lower() else 0)
df['Need Vue'] = df['Job Description'].apply(lambda x : 1 if 'vue' in x.lower() or 'vuejs' in x.lower() or 'vue.js' in x.lower() else 0)
df['Need SCSS/SASS'] = df['Job Description'].apply(lambda x : 1 if 'scss' in x.lower() or 'sass' in x.lower() else 0)

df['Need PHP'] = df['Job Description'].apply(lambda x : 1 if 'php' in x.lower() else 0)
df['Need Laravel'] = df['Job Description'].apply(lambda x : 1 if 'laravel' in x.lower() else 0)
df['Need WordPress'] = df['Job Description'].apply(lambda x : 1 if 'wordpress' in x.lower() else 0)
df['Need Ruby'] = df['Job Description'].apply(lambda x : 1 if 'ruby' in x.lower() else 0)
df['Need Ruby on Rails'] = df['Job Description'].apply(lambda x : 1 if 'ruby on rails' in x.lower() else 0)
df['Need .NET'] = df['Job Description'].apply(lambda x : 1 if '.net' in x.lower() else 0)

df['Need Node.js'] = df['Job Description'].apply(lambda x : 1 if 'node.js' in x.lower() or 'nodejs' in x.lower() else 0)
df['Need Spring'] = df['Job Description'].apply(lambda x : 1 if 'spring' in x.lower() or 'springmvc' in x.lower() else 0)
df['Need Spring Boot'] = df['Job Description'].apply(lambda x : 1 if 'spring boot' in x.lower() or 'springboot' in x.lower() else 0)

df['Need MySQL'] = df['Job Description'].apply(lambda x : 1 if 'mysql' in x.lower() else 0)
df['Need NoSQL'] = df['Job Description'].apply(lambda x : 1 if 'nosql' in x.lower() else 0)
df['Need PostgreSQL'] = df['Job Description'].apply(lambda x : 1 if 'postgresql' in x.lower() else 0)
df['Need MongoDB'] = df['Job Description'].apply(lambda x : 1 if 'mongodb' in x.lower() else 0)
df['Need Django'] = df['Job Description'].apply(lambda x : 1 if 'django' in x.lower() else 0)

#Saving parsed dataframe to a csv file
df.to_csv('full-stack-cleaned.csv', index = False)

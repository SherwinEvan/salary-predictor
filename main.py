# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 21:40:59 2023

@author: Sherwin
"""

import glassdoor_scraper as gs
import pandas as pd

driver_path = "F:/Code/salary_predictor/chromedriver"

#gs.get_jobs("full-stack", 300, False, driver_path)

df = pd.read_csv('full-stack.csv')

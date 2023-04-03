# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 21:40:59 2023

@author: Sherwin
"""

import glassdoor_scraper as gs
import pandas as pd

driver_path = "F:/Code/salary_predictor/chromedriver"

df = gs.get_jobs("full-stack-developer", 4, True, driver_path)

df

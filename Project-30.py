# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import pandas


df = pd.read_csv("C:/Users/Jeet Das/Desktop/Project-30.csv",encoding="utf-8")

print("\n----------------------- output data :---------------------\n")
print("Project-30 : Men who have sex with men (MSM) with active syphilis (%) [By WHO]");
print("\n------------------------------------------------------------\n")


# Question – A : get row and column numbers 

print('---------------------------------------------')
print("Dimension of the data frame = ",df.shape)
print('---------------------------------------------')

# Question – B : print column names :

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# Question - C : print available country

country = df.groupby(['Location'])[['Period']].count()
print("---------------------------------")
print("\tAvailable country names : ")
print("-------------------------------")
print(country)
print("-------------------------------")
count = 0
for row in range(len(country)): 
        count = count+1
print("total no. of country = ",count)        
print("-----------------------------\n")


# Question - D : Available years data for which data is available

years = df.groupby(['Period'])[['Location']].count()
print("---------------------------------")
print("\tAvailable years data : ")
print("-------------------------------")
print(years)
print("-------------------------------")
count = 0
for row in range(len(years)): 
        count = count+1
print("total no. of years = ",count)        
print("-----------------------------\n")



# Question - E :Types of available indicators

indicator = df.groupby(['Indicator'])[['Period']].count()
print("---------------------------------")
print("\tAvailable types of indicators : ")
print("-------------------------------")
print(indicator)
print("-------------------------------")
count = 0
for row in range(len(indicator)): 
        count = count+1
print("total no. of indicators = ",count)        
print("-----------------------------\n")


# Question - 01 : Afghanistan

Afghanistan = df[df.Location == 'Afghanistan']
print("\n\n--------------[ OUTPUT ]----------------------\n\n")
print(Afghanistan[['Location','Period','First Tooltip']])
                                                                  
# Question - 02 : Algeria  

Algeria  = df[df.Location == 'Algeria']
print("\n\n--------------[ OUTPUT ]----------------------\n\n")
print(Algeria[['Location','Period','First Tooltip']])                                                                         
                                                                                                                                                                                                                           
# Question - 03 : Argentina 

Argentina  = df[df.Location == 'Argentina']
print("\n\n--------------[ OUTPUT ]----------------------\n\n")
print(Argentina[['Location','Period','First Tooltip']])                                  
                                                                                                      
# Question - 04 : Armenia 

Armenia = df[df.Location == 'Armenia']
print("\n\n--------------[ OUTPUT ]----------------------\n\n")
print(Armenia[['Location','Period','First Tooltip']])

# Question - 05 : Bangladesh

Bangladesh = df[df.Location == 'Bangladesh']
print("\n\n--------------[ OUTPUT ]----------------------\n\n")
print(Bangladesh[['Location','Period','First Tooltip']])

# Question - 06 : Central African Republic

Central_African_Republic = df[df.Location == 'Central African Republic']
print("\n\n--------------[ OUTPUT ]----------------------\n\n")
print(Central_African_Republic[['Location','Period','First Tooltip']])

# Question - 07 : Chad

Chad = df[df.Location == 'Chad']
print("\n\n--------------[ OUTPUT ]----------------------\n\n")
print(Chad[['Location','Period','First Tooltip']])

# Question - 08 : China

China = df[df.Location == 'China']
print("\n\n--------------[ OUTPUT ]----------------------\n\n")
print(China[['Location','Period','First Tooltip']])

# Question - 09 : India

India = df[df.Location == 'India']
print("\n\n--------------[ OUTPUT ]----------------------\n\n")
print(India[['Location','Period','First Tooltip']])

# Question - 10 : Indonesia

Indonesia = df[df.Location == 'Indonesia']
print("\n\n--------------[ OUTPUT ]----------------------\n\n")
print(Indonesia[['Location','Period','First Tooltip']])

# Question - 11 : Thailand

Thailand = df[df.Location == 'Thailand']
print("\n\n--------------[ OUTPUT ]----------------------\n\n")
print(Thailand[['Location','Period','First Tooltip']])

# Question - 12 : United Arab Emirates

UAE = df[df.Location == 'United Arab Emirates']
print("\n\n--------------[ OUTPUT ]----------------------\n\n")
print(UAE[['Location','Period','First Tooltip']])

# Question - 13 : Saudi Arabia

Saudi_Arabia = df[df.Location == 'Saudi Arabia']
print("\n\n--------------[ OUTPUT ]----------------------\n\n")
print(Saudi_Arabia[['Location','Period','First Tooltip']])

# Question - 14 : South Africa

South_Africa = df[df.Location == 'South Africa']
print("\n\n--------------[ OUTPUT ]----------------------\n\n")
print(South_Africa[['Location','Period','First Tooltip']])

# Question - 15 : Chile

Chile = df[df.Location == 'Chile']
print("\n\n--------------[ OUTPUT ]----------------------\n\n")
print(Chile[['Location','Period','First Tooltip']])

# Question - 16 : Brazil

Brazil = df[df.Location == 'Brazil']
print("\n\n--------------[ OUTPUT ]----------------------\n\n")
print(Brazil[['Location','Period','First Tooltip']])

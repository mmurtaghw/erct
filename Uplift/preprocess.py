import pandas as pd
import re

countries = pd.read_csv("countries.csv")
trials = pd.read_csv("trials.csv")
countriesOutput = []
countryCodes = []
i = 0
for trialCountry in trials.Country:
    #print(trials.iloc[i,12])
    codeOut = None
    out = "private"
    for country, code in zip(countries.Name, countries.Code):
        if str(country) in str(trialCountry):
            #print(str(country))
            #trials.iloc[i,12] = str(country)
            out = country
            codeOut = code
            

    countriesOutput.append(out)    
    countryCodes.append(codeOut)            
    i += 1



subDivisions = pd.read_csv("IP2.CSV")
print(subDivisions)
subDivisionOutput = []
subDivisionCodes = []
i = 0
for trialCountry in trials.Country:
    #print(trials.iloc[i,12])
    codeOut = None
    out = "private"
    for country, code in zip(subDivisions.subdivision_name, subDivisions.code):
        if str(country) in str(trialCountry):
            #print(str(country))
            #trials.iloc[i,12] = str(country)
            out = country
            codeOut = code
            

    subDivisionOutput.append(out)    
    subDivisionCodes.append(codeOut)            
    i += 1
        
trials["processedCountries"] = countriesOutput
trials["COUNTRYISO"] = countryCodes
trials["SUBDIVISION"] = subDivisionOutput
trials["SUBDIVISIONISO"] = subDivisionCodes
print(countriesOutput)
trials.to_csv("trials.csv")

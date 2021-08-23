from typing import Sequence
import pandas as pd
import re
import numpy as np

#/Users/matt/Documents/CompSci/UpliftFolder/erct/Uplift/RIDIEMerge/combined_csv_all.csv
countries = pd.read_csv("countries.csv")
countriesAplha3 = pd.read_csv("country-codes_csv.csv")
trials = pd.read_csv("RIDIEMerge/combined_csv_all.csv")
Ridie = pd.read_csv("combined_csv_RIDIE.csv")
HDIdata = pd.read_csv("HDI.csv")

countriesOutput = []
countryCodes = []
i = 0
for trialCountry in trials.Country:
    print(trialCountry)
    codeOut = None
    outHDI = None
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

HDIValues = []
for trialCountry in countriesOutput:
    hdiOut = None
    for hdiCountry, hdiValue in zip(HDIdata.Country, HDIdata.HDI):
        outHDI = None
        if str(trialCountry) in str(hdiCountry):
            hdiOut = hdiValue
    HDIValues.append(hdiOut)
            
  

codesAlpha3 = []
for code2 in countryCodes:
    alpha3 = ""

    for codeAlpha3, codeAlpha2 in zip(countriesAplha3["ISO3166-1-Alpha-3"], countriesAplha3["ISO3166-1-Alpha-2"]):
        if codeAlpha2 == code2:         
            alpha3 = codeAlpha3
            break

    codesAlpha3.append(alpha3)
        
    
   
subDivisions = pd.read_csv("IP2.CSV")
#print(subDivisions)
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

wb = pd.read_csv("wb_data.csv")

wb = wb[wb["Time"] == 2016]

#(["'])(?:(?=(\\?))\2.)*?\1

all = []

for keyword in trials.Keywords:

    #print(type(keyword))
    seperatedKeywords = re.findall(r'"(.*?)"', str(keyword))
    for word in seperatedKeywords:
        if word != "":
            all.append(word)    

all = np.unique(all)

a = {}
k = 0

for val in np.unique(all):
    keywords = [None] * (len(trials.Keywords,))
    #print(keywords)
    

    for count, each in enumerate(trials.Keywords):
        # print((val in each))
        if type(each) == str:
            keywords[count] = val in each
            if (keywords[count] == True):
                keywords[count] = str(val)


    trials[val] = keywords

# for keyword in trials.Keywords:

#     for word in all:
#         if word in keyword:
#             key == word
            
trials["INDICATORID"] = (list(range(0,len(countriesOutput))))
trials["HDI"] = HDIValues
trials["processedCountries"] = countriesOutput
trials["COUNTRYISOALPHA2"] = countryCodes 
trials["COUNTRYISOALPHA3"] = codesAlpha3
trials["SUBDIVISION"] = subDivisionOutput
trials["SUBDIVISIONISO"] = subDivisionCodes
trials["SUBDIVISIONISO"] = subDivisionCodes

trials = trials.rename({"firms_and_productivity": "FIRMS", 
                        "agriculture": "AGRICULTURE", 
                        "behavior": "BEHAVIOR", 
                        "crime_violence_and_conflict": "CRIME",
                        "education" : "EDUCATION", 
                        "electoral": "ELECTORAL",
                        "environment_and_energy" : "ENVIRONMENT",
                        "finance": "FINANCE",
                        "gender": "GENDER",
                        "governance" : "GOVERNANCE",
                        "health" : "HEALTH",
                        "lab": "LAB",
                        "labor": "LABOR",
                        "other": "OTHER",
                        "post-conflict": "POSTCONFLICT",
                        "welfare":  "WELFARE"}, axis='columns')

#trials.rename(columns={"firms_and_productivity": "FIRMS"})

print(wb.PHYSICIANS)
merged = trials.merge(wb, left_on="COUNTRYISOALPHA3", right_on = "CODE")

merged.to_csv("merged.csv")
#print(countriesOutput)
trials.to_csv("trials.csv")

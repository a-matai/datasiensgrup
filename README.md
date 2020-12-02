# datasiensgrup

## installing requirements
requirements.txt is the list of requirements for a venv, easiest way to set up the installation of python

use pip install -r requirements.txt to set up the venv once activated

## notes 

### Done: 

**Crime data**

Grouped by month:
- Segmented crime data into year-month, figured out count of crimes/community area and totals for each month
- Further grouped data by community area in a dictionary (lol who needs pd) and then grouped 2015-2019 vs 2020.
- NOTE: this is currently paused. waiting to better understand how to understand general time trends in crime rate and how they affect our "average" rate

Crime rates:
- contains crime rates by community area: old_rate (2010 - 2019) and new_rate (2020)

**Greenspace Data**

- We’ve added up all the area (sqft) of greenspace/community area

**L-Stops Data**

- Added up number of lstops in each community area

**pop weights**

- 2010 data of each community area population compared to total population (weights)

### Data summary

- conditions: community area, pop weights, lstops, greenspace data
- df: community area, old_rate, new_rate, percent change
- df_final: df merged with conditions

### Analysis Summary:

- linear regressions:
    - we did individual regressions on greenspace acres, number of lstops and population share (weight) versus old/new crime rates
    - nothing interesting, but Lstops might be interesting...?
- multiple linear regression:
    - all factors vs old/new crime rate
    - nothing interesting here either

### Next steps:

- We are stuck, maybe more granular community by community analysis because there is no correlation (or seems to be no correlation barring questions below) from preliminary analysis on individual material conditions vs old_rates/new_rates

### Questions for Xi/Sanjay:

- linear regressions are not good fits (at all). Should we attempt a different type of regressor or, given the scatter, does it not make sense at all?
- how to bucket (can we further cluster community areas to avoid analysing all 77?)
- old_rate is an average from the last X years so how do we predict a new rate from the data and account for the crime rate change over time while also taking into account season variation? (which seems a separate analysis)
- what more do we need to do to infer from the material condition graphs?

### Questions for us:

- what are we doing lol
- add population density to measurements (we did weight by accident, should be density?)


import pandas as pd

# 1: Daily call center data is summarized in three CSV files, one for 2013, 2014 and 2015. Read the three files into Python and answer the following questions.

data_2013 = pd.read_csv("assets/2013.csv")
data_2014 = pd.read_csv("assets/2014.csv")
data_2015 = pd.read_csv("assets/2015.csv")
    
all_data = pd.concat([data_2013, data_2014, data_2015])

## a. What are the total number of calls per month from 2013 to 2015?

answer_1_a = all_data.groupby(["MONTH"]).size().reset_index(name="Count")

## b. What is the average number of calls per Month regardless of year? Which month has usually the highest traffic?
### Average
answer_1_b_1 = all_data.groupby(["MONTH"]).size().reset_index(name="Average")
answer_1_b_1["Average"] /= 3
### Highest Traffic
answer_1_b_2 = answer_1_b_1.sort_values(by="Average", ascending=False)

#### March is the month with highest traffic

## c. For three years, how many invalid calls were made? How many where made on each type?
### Total invalid calls
answer_1_c_1 = all_data[all_data["TRANSTYPE"] == "INVALID"].shape[0]
### Invalid and valid calls
answer_1_c_2 = all_data.groupby(["TRANSTYPE"]).size().reset_index(name="Count")

## d. How many times on average did a subscriber call all throughout the period?

answer_1_d = all_data.groupby(["SUBID"]).size().reset_index(name="Count")
answer_1_d["Count"] /= 3

## e. What were the top 5 transactions availed by the subscribers when calling?

answer_1_e = all_data.groupby(["TRANS"]).size().reset_index(name="Count").sort_values(by="Count", ascending=False).head(5)

#### The five highest transaction count are the ff:
####            TRANS              Count
####    DEVICE CONFIGURATION       29053
####       BILLING INQUIRY         27643
####          SHORT CALL           23100
####      MECHANICS PROCEDURE      21687
####        UNCOMPLETED CALL       18079

## f. A repeat call is when a customer calls the hotline again for the same transaction (assume time between calls does not matter. Given that the first call is not a repeat call, what is the average number of repeat calls per subscriber?

all_data_by_trans_repeat = all_data.groupby(["SUBID", "TRANS"]).size().reset_index(name="Count")
answer_1_f = all_data_by_trans_repeat["Count"].mean()

# 2. Analyze the SF Salaries dataset and answer the following questions:
salaries = pd.read_csv("assets/Salaries.csv", low_memory=False)

## a. Count the number of entries in the dataset.

answer_2_a = salaries.shape[0]

## b. What is the average BasePay?

salaries.loc[salaries["BasePay"] == "Not Provided", "BasePay"] = 0
answer_2_b = print(salaries["BasePay"].agg(lambda x: x.astype(float).mean()))

## c. What is the highest amount of OvertimePay in the dataset ?

salaries.loc[salaries["OvertimePay"] == "Not Provided", "OvertimePay"] = 0
salaries["OvertimePay"] = pd.to_numeric(salaries["OvertimePay"])
answer_2_c = salaries.sort_values(by="OvertimePay", ascending=False)

#### Highest overtime pay is 245131.88

## d. What is the job title of JOSEPH DRISCOLL ? Note: Use all caps, otherwise you may get an answer that doesn't match up (there is also a lowercase Joseph Driscoll)

answer_2_d = salaries[salaries["EmployeeName"] == "JOSEPH DRISCOLL"]["JobTitle"]
#### Job title for JOSEPH DISCOLL is "CAPTAIN, FIRE SUPPRESSION"

## e. How much does JOSEPH DRISCOLL make (including benefits)?
answer_2_e = salaries[salaries["EmployeeName"] == "JOSEPH DRISCOLL"]["TotalPayBenefits"]
#### Total pay with benefits for JOSEPH DRISCOLL is 270324.91

## f. What is the name of highest paid person (including benefits)?

salaries["TotalPayBenefits"] = pd.to_numeric(salaries["TotalPayBenefits"])
answer_2_f = salaries.sort_values(by="TotalPayBenefits", ascending=False)
#### The employee with highest pay w/ benefits is NATHANIEL FORD
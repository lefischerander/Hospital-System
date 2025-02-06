import pandas as pd
pd.options.mode.chained_assignment = None

#df = pd.read_csv(r"C:\Users\leand\Downloads\mimic-iv-clinical-database-demo-2.2\hosp\omr.csv")
df = pd.read_csv('/mnt/c/Users/Konst/Desktop/Uni/Python/Kurs Projekt/Lank/Datenbank/mimic/mimic-demo/hosp/omr.csv.gz')

df5 = df[ df['result_name'] == "Blood Pressure"]
df = df[ df['result_name'] != "Blood Pressure"] 

df['result_value'] = pd.to_numeric(df['result_value'], errors="coerce")

##Check if Weight-value is higher than 1500Lbs (> than highest recorded weight) or lower than 1 (< than smallest baby)
##Check if Height-value is higher than 110 (> than highest recorded height) or lower than 15 (< than smallest baby)
##Check if BMI-value is higher than 250 (> than highest recorded BMI) or lower than 7 (< than lowest recorded BMI)
deleteCondition = df[ ((df['result_name'] == "Weight (Lbs)") & ((df['result_value'] >= 1500) | (df['result_value'] <= 1))) | 
                    ((df['result_name'] == "Height (Inches)") & ((df['result_value'] >= 110) | (df['result_value'] <= 15))) | 
                    (df['result_name'] == "BMI (kg/m2)") & ((df['result_value'] >= 250) | (df['result_value'] <= 7)) |
                    df['result_value'].isnull()].index
df.drop(deleteCondition, inplace=True)
df['result_value'] = df['result_value'].astype(object)
df = pd.concat([df, df5], ignore_index=True) 

print(df)

#df.to_csv(r"E:\Studium\Gö\PDS\Projekt\db_tables\\new_omr.csv", index=False, encoding="utf-8", header=True)

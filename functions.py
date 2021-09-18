"""
create functions here :)
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


# air quality
aq_df = pd.read_csv('static/datasets/airquality.csv')

to_drop_aq = ["Good Days", "Moderate Days", "Unhealthy for Sensitive Groups Days", "Days CO","Days NO2","Days Ozone","Days SO2","Days PM2.5","Days PM10"]
aq_df.drop(to_drop_aq, inplace=True, axis=1)

aq_df['County'] = aq_df['County'].str.replace('"', '')

# median income
inc_df = pd.read_csv('static/datasets/income.csv')

to_drop_inc = ["FIPS_Code"]
inc_df.drop(to_drop_inc, inplace=True, axis=1)

inc_df = inc_df[inc_df["Attribute"] == 'Median_Household_Income_2019']

inc_df = inc_df[inc_df['Area_name'].str.contains("County")]
inc_df['County'] = inc_df['Area_name'].str.split(' County').str[0]

# demographics
dem_df = pd.read_csv('static/datasets/demographics.csv', encoding='latin-1')

to_drop_dem = ["WAC_MALE", "WAC_FEMALE", "BAC_MALE", "BAC_FEMALE", "IAC_MALE", "IAC_FEMALE", "AAC_MALE", "AAC_FEMALE", "NAC_MALE", "NAC_FEMALE", "NH_MALE", "NH_FEMALE", "NHWA_MALE"
 , "NHWA_FEMALE", "NHBA_MALE", "NHBA_FEMALE", "NHIA_MALE", "NHIA_FEMALE", "NHAA_MALE", "NHAA_FEMALE", "NHNA_MALE", "NHNA_FEMALE", "NHTOM_MALE", "NHTOM_FEMALE", "NHWAC_MALE", "NHWAC_FEMALE"
 , "NHBAC_MALE", "NHBAC_FEMALE", "NHIAC_MALE", "NHIAC_FEMALE", "NHAAC_MALE", "NHAAC_FEMALE", "NHNAC_MALE", "NHNAC_FEMALE", "HWA_MALE", "HWA_FEMALE", "HBA_MALE", "HBA_FEMALE"
 , "HIA_MALE", "HIA_FEMALE", "HAA_MALE", "HAA_FEMALE", "HNA_MALE", "HNA_FEMALE", "HTOM_MALE", "HTOM_FEMALE", "HWAC_MALE", "HWAC_FEMALE", "HBAC_MALE", "HBAC_FEMALE"
 , "HIAC_MALE", "HIAC_FEMALE", "HAAC_MALE", "HAAC_FEMALE", "HNAC_MALE", "HNAC_FEMALE", "H_MALE", "H_FEMALE", "TOT_MALE", "TOT_FEMALE"]

dem_df.drop(to_drop_dem, inplace=True, axis=1)
dem_df = dem_df[dem_df["YEAR"] == 12]
dem_df = dem_df[dem_df["AGEGRP"] == 0]

columns = []
to_drop_dem2 = [] 

for col in dem_df.columns:
    columns.append(col)

columns = columns[8:]
for i in range(0, len(columns), 2):
    sum_column = dem_df[columns[i]] + dem_df[columns[i+1]]
    edited_column = columns[i][:(len(columns[i]) - 5)] 
    dem_df[edited_column] = sum_column

    to_drop_dem2.append(columns[i])
    to_drop_dem2.append(columns[i+1])

to_drop_dem2.append("SUMLEV")
dem_df.drop(to_drop_dem2, inplace=True, axis=1)

# print(dem_df.head())



# education

# population

#graphs

aq_df = aq_df[aq_df['State'] == 'Alabama']

# print(aq_df.head())

inc_df = inc_df[inc_df['State'] == 'AL']

# print(inc_df.head())

aq_v_inc = aq_df.merge(inc_df, on='County')

print(aq_v_inc.head())

# data = pd.DataFrame(aq_v_inc, columns=["County","Median AQI","Median Household Income"])
# data_sorted = data.sort_values(by="Median Household Income", ascending=False)
# data_sorted.set_index("County", inplace=True)
# ranking = data_sorted.head(10)
# ranking

# first_bar = ranking["State"]
# first_bar_label = 'Revenue, USD million'
# first_bar_color = '#32628d'
# second_bar = ranking['budget']
# second_bar_label = 'Budget, USD million'
# second_bar_color = '#cde01d'
# labels = ranking.index
# width = 0.4  # the width of the bars
# plot_title = 'Top 10 movies by revenue, USD million'
# title_size = 18
# subtitle = 'Source: Kaggle / The Movies Dataset'
# filename = 'barh-plot'


# texas_counties = []

# index = ["Autugua"]
# dem_df_values = pd.DataFrame({"Median Household Income":[60], "Air Quality Index":[30]}, index=index)
# ax = dem_df_values.plot.bar(rot=0)


# join on airquality & income: by county (filter by state first -- can have same counties)
# aq_df = aq_df[aq_df['State'] == 'Alabama']
# inc_df = inc_df[inc_df['State'] == 'AL']
# aq_v_inc = pd.merge(aq_df, inc_df)
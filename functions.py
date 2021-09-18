"""
create functions here :)
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import math
mpl.use('Agg')


# air quality dataset cleaning
aq_df = pd.read_csv('static/datasets/airquality.csv')

to_drop_aq = ["Good Days", "Moderate Days", "Days CO","Days NO2","Days Ozone","Days SO2","Days PM2.5","Days PM10"]
aq_df.drop(to_drop_aq, inplace=True, axis=1)

aq_df['County'] = aq_df['County'].str.replace('"', '')

aq_df['Bad Days'] = aq_df.iloc[:, -7:-4].sum(axis=1)


# median income dataset cleaning
inc_df = pd.read_csv('static/datasets/income.csv')

to_drop_inc = ["FIPS_Code"]
inc_df.drop(to_drop_inc, inplace=True, axis=1)

inc_df = inc_df[inc_df["Attribute"] == 'Median_Household_Income_2019']

inc_df = inc_df[inc_df['Area_name'].str.contains("County|Parish")]
inc_df['County'] = inc_df['Area_name'].str.split(' County').str[0]
inc_df['County'] = inc_df['County'].str.split(' Parish').str[0]


# demographics data cleaning (currently unused)
"""
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
"""

# graphs

# filter datasets by STATE (air quality uses full name, income uses state code)

# graph variables

first_bar_label = '90th Percentile AQI'
first_bar_color = '#365367'

second_bar_label = 'Median Household Income (1000s)'
second_bar_color = '#F494AB'

width = 0.4  # the width of the bars
title_size = 14
filename = 'barh-plot'

state_codes = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
}

def create_figure(state):
    """
    Creates plot based on current selected U.S. state
    """
    plot_title = 'Median Household Income vs. 90th Percentile AQI by County (' + state + ')'

    # filters datasets by state
    aq_df_state = aq_df[aq_df['State'] == state]
    inc_df_state = inc_df[inc_df['State'] == state_codes[state]]

    # merge datasets based on county name
    aq_v_inc = aq_df_state.merge(inc_df_state, on='County')

    # sort by median income
    aq_v_inc.sort_values(by='Value', inplace=True, ascending=True)

    first_bar = aq_v_inc['90th Percentile AQI']
    second_bar = aq_v_inc['Value'] / 1000
    labels = aq_v_inc['County']

    fig, ax = plt.subplots(figsize = (8,6))
    plt.tight_layout()

    # Plot double bars
    x = np.arange(len(labels))  # Label locations
    ax.bar(x + width/2, first_bar, width, label=first_bar_label, color=first_bar_color)
    ax.bar(x - width/2, second_bar, width, label=second_bar_label, color=second_bar_color)


    # Set title
    title = plt.title(plot_title, pad=20, fontsize=title_size)
    title.set_position([.5, 1])

    # Adjust subplots
    plt.subplots_adjust(left=0.1, top=0.85, bottom=0.3)

    # Set y-labels and legend
    ax.set_xticklabels(labels)
    ax.legend()

    # To show each x-label, not just even ones
    print(x)
    plt.xticks(np.arange(min(x), max(x)+1, 1.0), rotation=90, fontsize=(24 / math.log(len(x))))

    return fig
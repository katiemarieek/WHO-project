import streamlit as st
import numpy as np
import pandas as pd

import pickle
from geopy.geocoders import Nominatim

# Please ensure the file Region_Dictionary is saved in the same directory

st.set_page_config(page_title="Life Expectancy Predictor",
                   page_icon=":skull:",
                   layout="centered")
# banner
st.image("https://interprofessional.global/wp-content/uploads/2018/11/who-logo-world-health-organization-logo.png", use_column_width=True)

# title
st.title("Life Expectancy Prediction")

def regression(region_dict):
    '''function for producing a prediction on life expectancy from a given set      of data, using linear regression.'''

    # User consent to use sensitive data
    consent = st.radio("Do you consent to using sensitive data such as immunisation rates, GDP information and location?", ("Yes", "No"))
    if consent == "Yes":
        model_type = st.radio("Would you prefer the most accurate model, or most robust?", ("Accurate", "Robust"))

        if model_type == "Accurate":
            Year = st.number_input("Please input Year", 0, 5000)
            Infant_deaths = st.number_input("Please input Number of Infant Deaths per 1000 population", 0, 1000)
            Under_five_deaths = st.number_input("Please input Number of under-five deaths per 1000 population", 0, 1000)
            Adult_mortality = st.number_input("Please input Adult Mortality Rates of both sexes (probability of dying between 15 and 60 years per 1000 population)", 0, 1000)
            Hepatitis_B = st.number_input("Please input Hepatitis B (HepB) immunization coverage among 1-year-olds (%)", 0, 100)
            BMI = st.number_input("Please input Average Body Mass Index of entire population", 0, 1000)
            Schooling = st.number_input("Please input Number of years of Schooling (years)", 0, 50)
            Economy_status_Developed = st.number_input("Please input 1 for Developed Status Economy, or 0 for Developing Status Economy", 0, 1)
            Incidents_HIV = st.number_input("Please input Deaths per 1 000 live births HIV/AIDS (0-4 years)", 0, 1000)
            GDP_per_capita = st.number_input("Please input your Country's GDP per Capita", 0, 100000000000)
            Country = st.text_input("Please input your Country")
                                                          
            if Country not in region_dict:
                print('Your Country could not be found')
                return False
            
            geolocator = Nominatim(user_agent="my_geocoder")
            location = geolocator.geocode(Country)  
                                           
            Region = region_dict[Country]
            long = location.longitude
            lat = location.latitude
                
            if Region == 'Asia':
                Region_Asia_Long = long
            else:
                Region_Asia_Long = 0
                                           
            if Region == 'Central_America_and_Caribbean':
                Region_Central_America_and_Caribbean_Lat = lat
                Region_Central_America_and_Caribbean_Long = long
            else:
                Region_Central_America_and_Caribbean_Lat = 0
                Region_Central_America_and_Caribbean_Long = 0
                                           
            if Region == 'European Union':
                Region_European_Union_Lat = lat
                Region_European_Union_Long = long
            else:
                Region_European_Union_Lat = 0
                Region_European_Union_Long = 0
                                           
            if Region == 'Middle East':
                Region_Middle_East_Lat = lat
                Region_Middle_East_Long = long
            else:
                Region_Middle_East_Lat = 0
                Region_Middle_East_Long = 0
                                           
            if Region == 'North America':
                Region_North_America_Lat = lat
                Region_North_America_Long = long
            else:
                Region_North_America_Lat = 0
                Region_North_America_Long = 0
                                           
            if Region == 'Oceania':
                Region_Oceania_Lat = lat
            else:
                Region_Oceania_Lat = 0
                                           
            if Region == 'South America':
                Region_South_America_Lat = lat
                Region_South_America_Long = long
            else:
                Region_South_America_Lat = 0
                Region_South_America_Long = 0
            

            HIV_log =  np.log(Incidents_HIV) # feature engineering for log.
            robust_GDP =  (GDP_per_capita - 4217.000000)/(12557.000000-1415.750000)  # feature engineering for robust scaling.                  

            if st.button("Predict Life Expectancy"):
                # Perform calculation and display result
                y_pred = (3.032960 + (Year * 0.040213) - (Infant_deaths * 0.057378) - (Under_five_deaths * 0.052745) - (Adult_mortality * 0.042581) 
                    - (Hepatitis_B * 0.007456) - (BMI * 0.173197) + (Schooling * 0.141658) + (Economy_status_Developed * 2.570668) - (HIV_log  * 0.098766) 
                    + (robust_GDP * 0.299015) + (Region_Asia_Long * 0.003260) - (Region_Central_America_and_Caribbean_Lat * 0.033608) 
                    - (Region_Central_America_and_Caribbean_Long * 0.037585) - (Region_European_Union_Lat  * 0.013740) - (Region_European_Union_Long * 0.024288) 
                    + (Region_Middle_East_Lat * 0.018903) - (Region_Middle_East_Long * 0.006130) - (Region_North_America_Lat *  0.063491) 
                    - (Region_North_America_Long  *  0.030893) + (Region_Oceania_Lat  * 0.020383) - (Region_South_America_Lat * 0.018519)
                    - (Region_South_America_Long* 0.026055))
               
                y_pred_round = round(y_pred, 2)
                
                st.write("Life expectancy prediction (2dp): ", y_pred_round)

        elif model_type == "Robust":
            # Similar input handling as accurate model
            Adult_mortality = st.number_input("Please input Adult Mortality Rates of both sexes (probability of dying between 15 and 60 years per 1000 population)", 0, 1000)
            Economy_status_Developing = st.number_input("Please input 1 for Developing Status Economy, or 0 for Developed Status Economy", 0, 1)
            Under_five_deaths = st.number_input("Please input Number of under-five deaths per 1000 population", 0, 1000)
            Incidents_HIV = st.number_input("Please input Deaths per 1 000 live births HIV/AIDS (0-4 years)", 0, 1000)
            Thinness_ten_nineteen_years = st.number_input("Please input Prevalence of Thinness among children and adolescents for Age 10 to 19 (%)", 0, 100)
                           
            if st.button("Predict Life Expectancy"):
                # Perform calculation and display result
                y_pred = (83.6189652770035 - (Adult_mortality * 0.04822813878970732) - (Economy_status_Developing * 2.2384826866603986) - 
                (Under_five_deaths * 0.08908986733007661) + (Incidents_HIV * 0.11383671753880499))
                y_pred_round = round(y_pred, 2)
                # The calculation here would be the same as in your original function
                st.write("Life expectancy prediction (2dp): ", y_pred_round)

    else:
        st.write("You have chosen not to use sensitive data.")
        # Similar input handling as accurate model for remaining inputs
        Adult_mortality = st.number_input("Please input Adult Mortality Rates of both sexes (probability of dying between 15 and 60 years per 1000 population)", 0, 1000)
        Economy_status_Developing = st.number_input("Please input 1 for Developing Status Economy, or 0 for Developed Status Economy", 0, 1)
        Under_five_deaths = st.number_input("Please input Number of under-five deaths per 1000 population", 0, 1000)
        Incidents_HIV = st.number_input("Please input Deaths per 1 000 live births HIV/AIDS (0-4 years)", 0, 1000)
        Thinness_ten_nineteen_years = st.number_input("Please input Prevalence of Thinness among children and adolescents for Age 10 to 19 (%)", 0, 100)
                           
        if st.button("Predict Life Expectancy"):
            # Perform calculation and display result
            y_pred = (83.6189652770035 - (Adult_mortality * 0.04822813878970732) - (Economy_status_Developing * 2.2384826866603986) - 
            (Under_five_deaths * 0.08908986733007661) + (Incidents_HIV * 0.11383671753880499))
            y_pred_round = round(y_pred, 2)
            # The calculation here would be the same as in your original function
            st.write("Life expectancy prediction (2dp): ", y_pred_round)

# Call the function
with open('Region_Dictionary.pkl', 'rb') as f:
    region_dict = pickle.load(f)

regression(region_dict)

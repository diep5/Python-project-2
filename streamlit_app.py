
# from app import *

# st.title('My first app')

# st.write("Here's our first attempt at using data to create a table:")

# st.pyplot(plot_sleep())
  
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from app import *
from app2 import *
from app3 import *

# Set the page config to wide layout
st.set_page_config(layout="wide")

# Create a sidebar for navigation using streamlit-option-menu
with st.sidebar:
    selected = option_menu(
        "Navigation", ["Home", "Dataset", "Graph", "Contact"],
        icons=['house', 'table', 'activity', 'envelope'], menu_icon="cast", default_index=0)

# Define the different pages
def home():
    st.title("Home")
    st.write("Welcome to our home page!")

def datasetPage():
    st.title("Dataset")
    st.write("The Health Dataset is a collection of data about people's health.")
    # Read the CSV file into a DataFrame
    try:
        df = pd.read_csv('health.csv')
        st.write('Here is the health data:')
        st.dataframe(df)
    except FileNotFoundError:
        st.error("File 'health.csv' not found. Please upload the file to continue.")

def graph():
    st.title("Graph")
    st.write("This is the graph page.")

    graph_titles = [
        "Relationship between Gender, Occupation, and Sleep Duration",  
        "Density of Sleep Duration by Gender and Stress Level",
        "Heatmap of Stress Level vs Sleep Disorder",
        "Count of Gender across Physical Activity Levels",
        "Distribution of BMI by Gender",
        "Relationship between Occupation and BMI Category",
        "Daily Steps: Trends by Age and Gender",
        "Daily Steps Distribution by Gender: A Look at the Violin Plot",
        "Stress Level by Occupation and Age",
        "Distribution of Stress Levels by Age Group",
        "Relationship Between Sleep Quality and Heart Rate Among Surveyed Individuals",
        "Distribution of Quality of Sleep",
    ]

    selected_titles = st.multiselect("Select the graph to display", graph_titles)

    # Plot the selected graph
    for title in selected_titles:
        if title == "Relationship between Gender, Occupation, and Sleep Duration":
            st.write("Relationship between Gender, Occupation, and Sleep Duration")
            st.pyplot(plot1())
            st.write("The plot illustrates the average sleep duration across different genders and occupations. Females tend to sleep slightly longer than males, with healthcare professionals having the highest average sleep durations. On average, females sleep between 7.2 to 8.5 hours, while males sleep between 5.8 to 7.4 hours. Healthcare professionals average around 7.5 hours of sleep, followed by educators and IT professionals. Interestingly, there's some variation within occupations based on gender, though less pronounced among IT professionals.")

            st.code(open("app.py").read(), language='python')
        elif title == "Density of Sleep Duration by Gender and Stress Level":
            st.write("Density of Sleep Duration by Gender and Stress Level")
            st.pyplot(plot2())
            st.write("The graphics show gender distribution, sleep duration variances, and stress level impacts on sleep. Sleep analysis by gender indicates females average 7 hours of sleep, slightly more than males at 6.5 hours. High-stress individuals sleep 5.5 hours, significantly less than low-stress counterparts averaging 7.5 hours. Further examination reveals high-stress individuals, regardless of gender, sleep about 30 minutes less than low-stress individuals. High-stress females sleep roughly 6.8 hours, while high-stress males sleep approximately 6.5 hours, highlighting stress as a key factor in sleep deprivation.")
            st.code(open("app2.py").read(), language='python')
        elif title == "Heatmap of Stress Level vs Sleep Disorder":
            st.write("Heatmap of Stress Level vs Sleep Disorder")
            st.pyplot(plot3())
            st.write("The heatmap illustrates the relationship between stress levels and sleep disorders. The data suggests that individuals with high stress levels are more likely to have sleep disorders. The most common sleep disorder among high-stress individuals is insomnia, followed by sleep apnea and restless leg syndrome. In contrast, low-stress individuals are less likely to have sleep disorders, with insomnia being the most common sleep disorder. This heatmap provides insights into the relationship between stress levels and sleep disorders.")
            st.code(open("app3.py").read(), language='python')

def contact():
    st.title("Contact")
    st.write("This is the contact page.")

# Display the selected page
if selected == "Home":
    home()
elif selected == "Dataset":
    datasetPage()
elif selected == "Contact":
    contact()
elif selected == "Graph":
    graph()




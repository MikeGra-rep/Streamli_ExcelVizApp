# Core Pkgs
from logging import exception
from sre_constants import SUCCESS
import streamlit as st

## Layout and Config
st.set_page_config(
     page_title="Profiler V6",
     page_icon="🗂",
     layout="wide",
     initial_sidebar_state="expanded",
     
 )

image1 = 'logosmall.png'
image2 = 'example_sheet.PNG'
image3 = 'normalized_sheet.PNG'
with st.sidebar:
    st.image(image1, width=110)
    st.title('Profiler Version 6')    
    st.caption('Lite Profiler & Vizualizer')
    st.caption('Developed for selected users ')
    st.write("Choose Profiler or Vizualiser")


import codecs

# EDA Pkgs
import pandas as pd
import pandas_profiling

#Components
import streamlit.components.v1 as components


# EDA Profiling
from streamlit_pandas_profiling import st_profile_report
from pandas_profiling import ProfileReport

#Custom Component Fxn
import sweetviz as SV

##


### Function for sweetviz - using the profiler to create vizualization.

def st_display_sweetviz(report_html, width=2200, height=1000 ):
    report_file = codecs.open(report_html, 'r')
    page = report_file.read()
    components.html(page,width=width,height=height,scrolling=True)


def main():
    """EDA Component Excel Parser"""

    menu = ["Instructions", "Profiler","Vizualizer"]
    choice = st.sidebar.radio("Section", menu)

## PROFILER
    if choice == "Profiler":
        st.subheader("Data Profiler")
        st.text('The Profiler will give you a overview of your data')
        st.text('The data structure in the excel file will dictate the result. ')
        st.info('Note: The results are correct but might not be what you where after.')
        data_file = st.file_uploader("Drag & Drop or Brows for .xlsx file. File Size Cap 200mb", type=['xlsx'])
        if data_file is not None:
            df = pd.read_excel(data_file)
            st.success('Data Loaded')
            st.text("Preview of 5 first rows")
            st.dataframe(df.head())
            profile = df.profile_report()
            if st.button ('Execute Profiling'):
               st_profile_report(profile)
        



## Vizualizer
    elif choice == "Vizualizer":
        st.subheader("Vizualization Generator")
        st.info('Vizualises the data by first profiling it and running it trough SweetViz Library')
        
        data_file = st.file_uploader("Drag & Drop or Brows for .xlsx file. File Size Cap 200mb", type=['xlsx'])
        if data_file is not None:
            df = pd.read_excel(data_file)
            st.success('Data Loaded')
            st.text("Preview of 5 first rows")
            st.dataframe(df.head())
            if st.button('Generate Report'):
                st_display_sweetviz('SWEETVIZ_REPORT.html')
        

            ## Not to Be used -- Separate Tab + Save Workflow
            # report = SV.analyze(df)
            # report.show_html("Reportfile.html")

## Home - Instructions
    else:
        st.header("Instructions - Errors - Feedback")
        st.write(""" The purpouse of this app is for the user to get a quick overview of the data they are handling. Basically give insight about the uploaded dataset. """ )
        st.write(""" It will help you understand in what "shape" the dataset is in """ )
        st.write(""" At the moment it accepts Excel files with extension .xlsx.""" )
        st.write(""" Read the instructions section below and 'If Errors' section """ )
        if st.button('Instructions'):
          
            st.subheader('Workflow')
            st.write('- Prepare your data')
            st.write('- Upload the data')
            st.write('- Wait for the check mark " Data Loaded"')
            st.write('- Press Execute Profiling / Generate Report')

            st.subheader('Data Preparation')
            st.info('The structural data requirement is that the first row of the dataset is populated and on Sheet 1. For best results start with the data in A1:A1')
            st.warning(' Content limitation : Cells linking to another WorkBOOK (on sharepoint eg.) will not work.')
            st.success('The excel sheet can include: Formatting,Conditional formatting, Charts, Formulas & inconsistancies - Note that it will disregard them and transform all data to its basic form. (Eg. 2,25% -> 0,0225 ) ')      
            st.write('Both the Profiler and the Vizualistion uses the first row to determen the columns. The tools create a dataframe with a Columnar principle.')
            st.write('The columns are then analyzed and correlated with each other.')
            st.write('Below you see a example sheet')
            st.image(image2)
            st.caption('The input sheet with formating')
            st.image(image3)
            st.caption('The "Normalized" sheet')



        if st.button('If Errors'):
            st.write('If errors occur please check that the first row of the excel sheet is populated')
            st.write('If error presists copy the message and send it to me')
            st.write('Errors are presented in red')
            st.error('Propper error handling has not been implememted in this POC (Version 6)')

        if st.button('Feedback'):
            st.success('Feedback is always welcome!')
            st.write('Call me (+46701619565) or send me an email (mikael.granberg@aw.com) and we can discuss future improments')
            st.info('You should expect limited support, this is only a POC - IF this is something of good use I can probalby do more with it :) ')




if __name__ == '__main__':
    main()
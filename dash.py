import streamlit as st
import plotly.express as px
import pandas as pd
import warnings
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import time

# Set Streamlit page config
st.set_page_config(layout="wide")

# Suppress warnings
warnings.filterwarnings('ignore')

# Load data
fl = st.file_uploader(":file_folder: Upload a file", type=(["csv"]))

if fl is not None:
    # Read the CSV file
    df = pd.read_csv(fl, encoding="ISO-8859-1")

    # Display page title
    st.markdown("<h2 style='text-align: center; padding-top: 1rem;'>Study of Studies</h2>", unsafe_allow_html=True)

    # Display success message upon file upload
    success_message = st.empty()
    success_message.success("File successfully uploaded!")
    time.sleep(3)
    success_message.empty()

    # Sidebar layout
    st.sidebar.header("Choose your filters:")

    # Sidebar filters
    filters = {
        "Document Type": "DOCUMENT TYPE (book, Journal article, Report, Statutes, Newspaper)",
        "Applicable Nomenclature": "APPLICABLE NOMENCLATURE(KEY NAME USED)",
        "Section of Article Analysed": "SECTION OF THE ARTICLE ANALYSED",
        "Nationality of Author": "NATIONALITY/ORIGIN/EXTRACTION OF AUTHOR",
        "Year of Publication": "YEAR OF PUBLICATION",
        "Positionality of Articles": "POSITIONALITY OF ARTICLE",
        "Categorization of Publication": "CATEGORISATION OF PUBLICATION( descriptive, diagnostic(identify problems), Prescriptive, theoretical)",
        "Continent of Study": "CONTINENT OF STUDY",
        "Use of Statistics": "USE OF STATISTICS",
        "UN-Habitat Citation": "CITE 'UN-habitat 2003 STUDY ON SLUMS'"
    }

    selected_filters = {}
    for filter_name, column_name in filters.items():
        selected_filters[filter_name] = st.sidebar.multiselect(filter_name, df[column_name].unique())

    # Apply filters to DataFrame
    filtered_df = df
    for filter_name, selected_values in selected_filters.items():
        if selected_values:
            filtered_df = filtered_df[filtered_df[column_name].isin(selected_values)]

    # Display home page
    page = st.sidebar.selectbox("Select a page", ["Home", "Word Cloud"])

    if page == "Home":
        st.markdown("<p style='text-align: center; padding: 1rem; color: Green;'>This is the home page.<br/> Use the sidebar to navigate between pages.</p>", unsafe_allow_html=True)

        # Check if the filtered DataFrame is not empty before proceeding with visualizations
        if not filtered_df.empty:
            # Display the filtered data
            st.markdown("<h3 style='text-align: center;'>Filtered Data</h3>", unsafe_allow_html=True)
            st.write(filtered_df)

            # Display visualizations
            st.markdown("<h2 style='text-align: center; padding-top: 1rem; padding-bottom: 2rem;'>Column Graphs</h2>", unsafe_allow_html=True)

            col1, col2 = st.columns(2)

            # Visualization 1 - DOCUMENT TYPE (Bar Graph)
            fig1 = px.bar(filtered_df['DOCUMENT TYPE (book, Journal article, Report, Statutes, Newspaper)'].value_counts(),
                          x=filtered_df['DOCUMENT TYPE (book, Journal article, Report, Statutes, Newspaper)'].value_counts().index,
                          y=filtered_df['DOCUMENT TYPE (book, Journal article, Report, Statutes, Newspaper)'].value_counts().values,
                          labels={'x': 'DOCUMENT TYPE', 'y': 'Count'}, title='Document Type Distribution')
            fig1.update_layout(height=500, width=600)
            fig1.update_layout(margin=dict(l=20, r=20))
            fig1.update_layout(title=dict(x=0.5, y=1, xanchor='center', yanchor='top'))
            col1.plotly_chart(fig1)

            # Visualization 2 - APPLICABLE NOMENCLATURE (Bar Graph)
            fig2 = px.bar(filtered_df['APPLICABLE NOMENCLATURE(KEY NAME USED)'].value_counts(),
                          x=filtered_df['APPLICABLE NOMENCLATURE(KEY NAME USED)'].value_counts().index,
                          y=filtered_df['APPLICABLE NOMENCLATURE(KEY NAME USED)'].value_counts().values,
                          labels={'x': 'APPLICABLE NOMENCLATURE(KEY NAME USED)', 'y': 'Count'}, title='Nomenclature Distribution')
            fig2.update_layout(height=500, width=550)
            fig2.update_layout(margin=dict(l=155, r=10))
            fig2.update_layout(title=dict(x=0.5, y=1, xanchor='center', yanchor='top'))
            col2.plotly_chart(fig2)

            # Visualization 3 - SECTION OF ARTICLE ANALYSED (Bar Graph)
            fig3 = px.bar(filtered_df['SECTION OF THE ARTICLE ANALYSED'].value_counts(),
                          x=filtered_df['SECTION OF THE ARTICLE ANALYSED'].value_counts().index,
                          y=filtered_df['SECTION OF THE ARTICLE ANALYSED'].value_counts().values,
                          labels={'x': 'SECTION OF THE ARTICLE ANALYSED', 'y': 'Count'}, title='Section of Article Analyzed Distribution')
            fig3.update_layout(height=500, width=600)
            fig3.update_layout(margin=dict(l=20, r=20))
            fig3.update_layout(title=dict(x=0.5, y=1, xanchor='center', yanchor='top'))
            col1.plotly_chart(fig3)

            # Visualization 4 - NATIONALITY OF AUTHOR (Bar Graph)
            fig4 = px.bar(filtered_df['NATIONALITY/ORIGIN/EXTRACTION OF AUTHOR'].value_counts(),
                          x=filtered_df['NATIONALITY/ORIGIN/EXTRACTION OF AUTHOR'].value_counts().index,
                          y=filtered_df['NATIONALITY/ORIGIN/EXTRACTION OF AUTHOR'].value_counts().values,
                          labels={'x': 'NATIONALITY/ORIGIN/EXTRACTION OF AUTHOR', 'y': 'Count'}, title='Nationality of Author Distribution')
            fig4.update_layout(height=500, width=550)
            fig4.update_layout(margin=dict(l=155, r=10))
            fig4.update_layout(title=dict(x=0.5, y=1, xanchor='center', yanchor='top'))
            col2.plotly_chart(fig4)

            # Visualization 5 - YEAR OF PUBLICATION (Line Graph)
            fig5 = px.line(filtered_df['YEAR OF PUBLICATION'].value_counts().sort_index(),
                           x=filtered_df['YEAR OF PUBLICATION'].value_counts().sort_index().index,
                           y=filtered_df['YEAR OF PUBLICATION'].value_counts().sort_index().values,
                           labels={'x': 'YEAR OF PUBLICATION', 'y': 'Count'}, title='Year of Publication Distribution')
            fig5.update_layout(height=500, width=600)
            fig5.update_layout(margin=dict(l=20, r=20))
            fig5.update_layout(title=dict(x=0.5, y=1, xanchor='center', yanchor='top'))
            col1.plotly_chart(fig5)

            # Visualization 6 - POSITIONALITY OF ARTICLE (Bar Graph)
            fig6 = px.bar(filtered_df['POSITIONALITY OF ARTICLE'].value_counts(),
                          x=filtered_df['POSITIONALITY OF ARTICLE'].value_counts().index,
                          y=filtered_df['POSITIONALITY OF ARTICLE'].value_counts().values,
                          labels={'x': 'POSITIONALITY OF ARTICLE', 'y': 'Count'}, title='Positionality of Articles Distribution')
            fig6.update_layout(height=500, width=550)
            fig6.update_layout(margin=dict(l=155, r=10))
            fig6.update_layout(title=dict(x=0.5, y=1, xanchor='center', yanchor='top'))
            col2.plotly_chart(fig6)

            # Visualization 7 - CATEGORIZATION OF PUBLICATION (Pie Chart)
            fig7 = px.pie(filtered_df['CATEGORISATION OF PUBLICATION( descriptive, diagnostic(identify problems), Prescriptive, theoretical)'].value_counts(),
                          values=filtered_df['CATEGORISATION OF PUBLICATION( descriptive, diagnostic(identify problems), Prescriptive, theoretical)'].value_counts().values,
                          names=filtered_df['CATEGORISATION OF PUBLICATION( descriptive, diagnostic(identify problems), Prescriptive, theoretical)'].value_counts().index,
                          title='Categorization of Publication Distribution')
            fig7.update_layout(height=500, width=600)
            fig7.update_layout(margin=dict(l=20, r=20))
            fig7.update_layout(title=dict(x=0.5, y=1, xanchor='center', yanchor='top'))
            col1.plotly_chart(fig7)

            # Visualization 8 - CONTINENT OF STUDY (Bar Graph)
            fig8 = px.bar(filtered_df['CONTINENT OF STUDY'].value_counts(),
                          x=filtered_df['CONTINENT OF STUDY'].value_counts().index,
                          y=filtered_df['CONTINENT OF STUDY'].value_counts().values,
                          labels={'x': 'CONTINENT OF STUDY', 'y': 'Count'}, title='Continent of Study Distribution')
            fig8.update_layout(height=500, width=550)
            fig8.update_layout(margin=dict(l=155, r=10))
            fig8.update_layout(title=dict(x=0.5, y=1, xanchor='center', yanchor='top'))
            col2.plotly_chart(fig8)

            # Visualization 9 - USE OF STATISTICS (Bar Graph)
            fig9 = px.bar(filtered_df['USE OF STATISTICS'].value_counts(),
                          x=filtered_df['USE OF STATISTICS'].value_counts().index,
                          y=filtered_df['USE OF STATISTICS'].value_counts().values,
                          labels={'x': 'USE OF STATISTICS', 'y': 'Count'}, title='Use of Statistics Distribution')
            fig9.update_layout(height=500, width=600)
            fig9.update_layout(margin=dict(l=20, r=20))
            fig9.update_layout(title=dict(x=0.5, y=1, xanchor='center', yanchor='top'))
            col1.plotly_chart(fig9)

            # Visualization 10 - UN-Habitat Citation (Bar Graph)
            fig10 = px.bar(filtered_df["CITE 'UN-habitat 2003 STUDY ON SLUMS'"].value_counts(),
                           x=filtered_df["CITE 'UN-habitat 2003 STUDY ON SLUMS'"].value_counts().index,
                           y=filtered_df["CITE 'UN-habitat 2003 STUDY ON SLUMS'"].value_counts().values,
                           labels={'x': "CITE 'UN-habitat 2003 STUDY ON SLUMS'", 'y': 'Count'},
                           title='UN-Habitat Citation Distribution')
            fig10.update_layout(height=500, width=550)
            fig10.update_layout(margin=dict(l=155, r=10))
            fig10.update_layout(title=dict(x=0.5, y=1, xanchor='center', yanchor='top'))
            col2.plotly_chart(fig10)

            # ... (repeat for other visualizations)

        else:
            st.warning("No data found for the selected filters.")

    elif page == "Word Cloud":
        st.markdown("<h2 style='text-align: center; padding-top: 1rem;'>Word Clouds</h2>", unsafe_allow_html=True)

        # Word Clouds
        wordcloud_titles = [
            'Adjectival Phrases Word Cloud',
            'Descriptive Studies Word Cloud',
            'Prescriptive Studies Word Cloud',
            'Diagnostic Studies Word Cloud',
            'Theoretical Studies Word Cloud'
        ]

        col3, col4 = st.columns(2)

        for i in range(5):
            col = col3 if i < 3 else col4
            col.subheader(wordcloud_titles[i])
            text_data = df.iloc[:, i + 18]  # Assuming the descriptive terms start from the 18th column
            wordcloud = WordCloud(width=400, height=400, background_color='#3498db', mode='RGBA').generate(' '.join(text_data.dropna()))
            plt.figure(figsize=(10, 5))
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis('off')
            st.set_option('deprecation.showPyplotGlobalUse', False)
            col.pyplot()

    else:
        st.warning('No Data Available')
else:
    st.warning("Please upload a CSV file.")




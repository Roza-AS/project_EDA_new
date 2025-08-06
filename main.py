import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt


def run_basic_eda(df):
    """This function takes a DataFrame,
            and creates a basic Exploratory Data Analysis (EDA) report,
            displaying it using Streamlit."""

    #if the user uploads an empty dataset:
    if df.empty:
        st.warning("The uploaded dataset is empty.")
        return

    #basic info
    st.subheader("Basic Info")
    st.write(f"Shape: {df.shape}") #give us the num of rows and columns of our df
    st.write("Data Types:")
    st.write(df.dtypes) #give us the data types of our variables

    st.subheader("Summary Statistics")
    st.write(df.describe()) #descriptive statistics (mean,std, max, min...)

    st.subheader("Missing Values")
    st.write(df.isnull().sum()) #counts how many missing values in the df

    #lets start exploring categorical columns
    categorical_cols = df.select_dtypes(include="object").columns.tolist() #extract all categorical columns, so we can plot

    if len(categorical_cols) > 0: # "if categorical_cols:" could have also work
        st.subheader("Bar Plots for Categorical Columns")
        for col in categorical_cols:
            num_categories = df[col].nunique()

            # on second thought, to many categories could make a messy plot, so lets limit
            if num_categories <= 4:
                fig, ax = plt.subplots() #create a figure and axis
                df[col].value_counts().plot(kind="bar", ax=ax)
                ax.set_title(f"Value Counts of {col}")
                ax.set_xlabel(col)
                ax.set_ylabel("Count")
                st.pyplot(fig)
            else:
                st.warning(f"Too many categories in '{col}' ({num_categories}). Skipping plot.")

    #now we explore numeric columns
    numeric_cols = df.select_dtypes(include="number").columns.tolist() #extract all numeric columns, so we can plot

    if len(numeric_cols) > 0: #histogram plot to show distribution
        st.subheader("Histograms")
        for col in numeric_cols:
            fig, ax = plt.subplots()
            sns.histplot(df[col].dropna(), kde=True, ax=ax) #KDE curve to smooth the distribution
            ax.set_title(f"Distribution of {col}")
            st.pyplot(fig)

        if len(numeric_cols) > 1:
            st.subheader("Correlation Heatmap") # to show relationships between numeric variables
            fig, ax = plt.subplots()
            sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="coolwarm", ax=ax)
            ax.set_title("Correlation Heatmap")
            st.pyplot(fig)

            st.subheader("Pair Plot") #scatterplots for numeric column, and histograms, to see relationships and distributions
            fig = sns.pairplot(df[numeric_cols].dropna())
            st.pyplot(fig)

        if len(numeric_cols) > 0: #box plots to detect outliers
            st.subheader("Box Plots for Numeric Columns")
            for col in numeric_cols:
                fig, ax = plt.subplots()
                sns.boxplot(x=df[col], ax=ax)
                ax.set_title(f"Box Plot of {col}")
                st.pyplot(fig)

        #a cool idea is to let users select what columns do they want to plot
        selected_cols = st.multiselect("Select numeric columns to visualize", numeric_cols, default=numeric_cols)

        if selected_cols:
            st.subheader("Histograms of Selected Columns")
            for col in selected_cols:
                fig, ax = plt.subplots()
                sns.histplot(df[col].dropna(), kde=True, ax=ax)
                ax.set_title(f"Distribution of {col}")
                st.pyplot(fig)

            st.subheader(
                "Pair Plot")
            fig = sns.pairplot(df[selected_cols].dropna())
            st.pyplot(fig)





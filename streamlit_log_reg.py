import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import accuracy_score, mean_squared_error
from sklearn.model_selection import train_test_split
import seaborn as sns 
import streamlit as st 
import matplotlib.pyplot as plt 

uploaded_file = st.file_uploader("Please, choose a file:")

if uploaded_file != None:
    df = pd.read_csv(uploaded_file).drop('Unnamed: 0', axis=1)

    st.write(f'Column names: {", ".join(df.columns)}')
    target = st.text_input("Target column name:", 'y')
    columns = df.drop(target, axis = 1).columns

    scaler = StandardScaler()
    y = df[target]

    X = df.drop(target, axis = 1)
    X = scaler.fit_transform(X)
    test_size = st.text_input("Enter test size:", 0.5)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=float(test_size), random_state=42)

    st.write('Choose a model:')
    linear_regression = st.checkbox('Linear Regression')
    logistic_regression = st.checkbox('Logistic Regression')

    if linear_regression:
        linreg = LinearRegression().fit(X_train, y_train)
        summary_df = pd.DataFrame(linreg.coef_, columns).transpose()
        summary_df['w0'] = linreg.intercept_
        st.write(summary_df)
        st.write(mean_squared_error(y_test, linreg.predict(X_test)))


    if logistic_regression:
        logreg = LogisticRegression().fit(X_train, y_train)
        summary_df = pd.DataFrame(logreg.coef_, columns = columns)
        summary_df['w0'] = logreg.intercept_
        st.dataframe(summary_df)
        st.write(f'The accuracy score of the model is {accuracy_score(y_test, logreg.predict(X_test))}')
        
    st.write('## Please choose any two columns you want to plot:')

    checkboxes = [st.checkbox(f"Column {i}") for i in range(X.shape[1])]
    selected_cols = [i for i, checkbox in enumerate(checkboxes) if checkbox]


    if len(selected_cols) == 2:
        st.write('Please choose the type of plot:')
        scatterplot = st.checkbox('Scatterplot')
        barplot = st.checkbox('Barplot')
        kde_plot = st.checkbox('KDE Plot')
        line_plot = st.checkbox('Line plot')

        fig, ax = plt.subplots()
        x_col = selected_cols[0]
        y_col = selected_cols[1]

        if (kde_plot, scatterplot, barplot, line_plot).count(True) == 1:
            if scatterplot and not (barplot or kde_plot):
                sns.scatterplot(x = X[:, x_col], y= X[:, y_col])
            if barplot and not(scatterplot or kde_plot or line_plot):
                sns.barplot(x = X[:, x_col], y = X[:, y_col])
                plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False) 
            if kde_plot and not(barplot or scatterplot or line_plot):
                sns.kdeplot(x = X[:, x_col], y = X[:, y_col])
            if line_plot and not(barplot or scatterplot or kde_plot):
                sns.lineplot(x = X[:, x_col], y = X[:, y_col])
            plt.xlabel(f"Column {x_col}")
            plt.ylabel(f"Column {y_col}")
            st.pyplot(fig)
        if (kde_plot, scatterplot, barplot, line_plot).count(True) > 1:
            st.write('Please choose only one plot type at once')
    if len(selected_cols) != 2 and len(selected_cols) != 0:
        st.write("Please select exactly 2 columns.")
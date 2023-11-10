import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st

housing = pd.read_csv("E:\\vx\\WeChat Files\\wxid_xo7lo8jh5wqz32\\FileStorage\\File\\2023-11\\archive\\housing.csv")

def one():
    plt.figure(figsize=(12, 6))
    sns.histplot(data=housing, x='median_income', color='blue', alpha=0.6, label='Median Income')
    sns.histplot(data=housing, x='median_house_value', color='red', alpha=0.6, label='Median House Value')
    plt.legend()
    st.pyplot(plt)

def two():
    avg_values = housing.groupby('ocean_proximity')['median_house_value'].mean().reset_index()
    plt.figure(figsize=(10, 6))
    sns.barplot(x='ocean_proximity', y='median_house_value', data=avg_values)
    plt.xlabel('Ocean Proximity')
    plt.ylabel('Average Median House Value')
    st.pyplot(plt)

def three():
    age_value_relation = housing.groupby('housing_median_age')['median_house_value'].mean().reset_index()
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='housing_median_age', y='median_house_value', data=age_value_relation)
    plt.xlabel('Housing Median Age')
    plt.ylabel('Average Median House Value')
    plt.title('House Value over House Age')
    st.pyplot(plt)

def four():
    plt.figure(figsize=(10, 8))
    sns.scatterplot(x='median_income', y='median_house_value', data=housing, hue='housing_median_age',
                    palette='viridis')

    # 绘制回归线
    sns.regplot(x='median_income', y='median_house_value', data=housing, scatter=False, color='black')

    plt.title('House Value vs. Median Income')
    plt.xlabel('Median Income (tens of thousands)')
    plt.ylabel('Median House Value')
    plt.legend(title='Median Age')
    st.pyplot(plt)

# st.subheader('Title')

col1,col2 = st.columns([3,3])

with col2:
    num = st.selectbox("index",[0,1,2,3])
    if num == 1:
        st.markdown(
            '<span style="font-size:20px;"><font color=red >*What is the relationship between median income and median house price?*</font></span>',
            unsafe_allow_html=True)
        one()
        st.write(
            "According to the multivariate histogram, we can see that the distribution of the median income is relatively concentrated on the lower income level, while the distribution of the median house price is relatively broad, including the range of low to high house prices. This shows that in this data set, most people's income is low, but the range of house prices is wide.")
        st.write(
            "In addition, we can also observe that there may be a positive correlation between median income and median house price. In the range of low median income, the median house price is also relatively low; In the range of high median income, the median house price is also relatively high. This may mean that people with higher income levels are more able to buy houses with higher prices.")
    if num == 2:
        st.markdown(
            '<span style="font-size:20px;"><font color=red >How does housing age affect the average median house price?*</font></span>',
            unsafe_allow_html=True)
        two()
        st.write('According to the multivariate bar chart, we can see the average median house price under different ocean proximity. It can be observed from the figure that the average median house price shows a downward trend with the increase of housing age . This means that the housing age has a negative impact on the average median housing price, that is, the older the housing age, the lower the average median housing price. This may be because the value of old houses is low, while the value of new houses is high. Therefore, housing age is an important factor affecting the average median housing price.')

    if num == 3:
        st.markdown(
            '<span style="font-size:20px;"><font color=red >*Can people with higher median income buy houses with higher prices?*</font></span>',
            unsafe_allow_html=True)
        three()
        st.write('It can be observed from the figure that the average median house price shows a downward trend with the increase of housing age. This means that the price of older houses is lower. Therefore, it can be concluded that there is a negative correlation between housing age and housing price in California.')

with col1:
    button = st.button('knock')
    if button:
        st.markdown(
            '<span style="font-size:20px;"><font color=red >*What’s the relationship between housing price and average income in California?*</font></span>',
            unsafe_allow_html=True)
        four()
        st.write('It can be seen that there is a certain positive correlation between housing prices and average income in California. The slope of the regression line is positive, indicating that with the increase of average income, housing prices also show an upward trend [3]. This means that in California, higher income areas tend to have higher house prices.')
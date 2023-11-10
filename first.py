import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st

housing = pd.read_csv("C:\\Users\\L\\Documents\\WeChat Files\\wxid_skzvxu67aw9n32\\FileStorage\\File\\2023-11\\housing.csv")

def pic_fir():
    plt.figure(figsize=(10, 8))
    sns.scatterplot(x='longitude', y='latitude', data=housing,
                    hue='median_house_value', size='population',
                    alpha=0.5, palette='viridis', legend="brief")

    plt.title('California Housing Prices and Population by Location')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.legend(title='House Value / Population')
    st.pyplot(plt)

def pic_sec():
    # 绘制热力图
    plt.figure(figsize=(10, 8))
    # sns.kdeplot(data=housing, x='longitude', y='latitude', shade=True, cmap='coolwarm')
    # 绘制散点图
    sns.scatterplot(x='longitude', y='latitude', data=housing,
                    size='population', hue='median_house_value',
                    alpha=0.5, palette='viridis', legend="brief")
    plt.title('Population Density and Housing Prices in California')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.legend(title='House Value / Population')
    st.pyplot(plt)

# st.subheader('California House')
st.markdown(
            '<span style="font-size:20px;"><font color=red >*What’s the relationship between California housing prices and popularity and geographical location (longitude and latitude)?*</font></span>',
            unsafe_allow_html=True)
pic_fir()
option = st.button('Description')
if option:
    st.write('First of all, we can observe that there is a certain correlation between housing prices and popularity and geographical location. In the figure, we can see that some points of high housing prices and popularity are concentrated in some specific geographical locations in California, such as coastal areas and near large cities . This may be because these regions have better economic development, educational resources and employment opportunities, attracting more population and investment, thus promoting the rise of house prices and the promotion of popularity. In addition, we can also observe that some points of low house prices and popularity are concentrated in some remote areas or sparsely populated areas in California . This may be because these areas are relatively remote, their economic development is relatively weak, and they lack the conditions to attract population and investment, resulting in low house prices and low popularity. In general, there is a certain correlation between the housing price and popularity in California and its geographical location (longitude and latitude). The housing price and popularity in coastal areas and near large cities are relatively high, while those in remote areas or sparsely populated areas are relatively low.')
with st.expander('view'):
    st.markdown(
        '<span style="font-size:20px;"><font color=red >*What’s the relationship between housing price and population density in California?*</font></span>',
        unsafe_allow_html=True)
    pic_sec()
    st.write('It can be seen that there is a certain positive correlation between housing prices and average income in California. The slope of the regression line is positive, indicating that with the increase of average income, housing prices also show an upward trend [3]. This means that in California, higher income areas tend to have higher house prices.')
import streamlit as st

url = ['https://ts1.cn.mm.bing.net/th/id/R-C.e24d9babff398f3aa1d4e194f05aefab?rik=%2bNwywY5%2b56zVCg&riu=http%3a%2f%2fwww.beimeigoufang.com%2fPhoto%2fimages%2fnews%2f2017%2f05%2f1221%2f6_webp.jpg&ehk=atY%2bzm0cFGpXzEbPw%2fohH%2b6OTun3qkWTatzU6Sc3qMU%3d&risl=&pid=ImgRaw&r=0&sres=1&sresct=1','https://ts1.cn.mm.bing.net/th/id/R-C.f777c078f24fe61aaef5f96717471a2a?rik=MumN9hvUrgQUZA&riu=http%3a%2f%2fimages3.ctrip.com%2fwri%2fimages%2f200707%2fROMAN99_CN18140422734.jpg&ehk=ZOHby%2bapNVbAeqHv4CHgwnWLsw%2fHpKZF4Qr9MVxLM8o%3d&risl=&pid=ImgRaw&r=0','https://www.beimeigoufang.com/Photo/images/news/2017/05/1221/640_webp%20(1).jpg','https://ts1.cn.mm.bing.net/th/id/R-C.67d9ccfb84aa7ec7ec4cd08881663f93?rik=jioJtJ%2fZNw7fQw&riu=http%3a%2f%2fe-images.juwaistatic.com%2f2017%2f05%2fshutterstock_405835483.jpg&ehk=IoF%2fb0dOCem9N6luJ%2b7v3b4XEGgeW1%2bYY8jYRBB56do%3d&risl=&pid=ImgRaw&r=0','https://ts1.cn.mm.bing.net/th/id/R-C.94f9fcba68e2cc01631d9cce8502f3d1?rik=pGEYS9fVTntDmg&riu=http%3a%2f%2fpic.shejiben.com%2fcase%2f1209%2f02%2f20120902_04c2f3a8e53d4937f33eqvkurysAzUch.jpg&ehk=CPQRooQ60gAnhvgh0qbgOEnsMgPLXPh4qEkctPNfNkc%3d&risl=&pid=ImgRaw&r=0']
# 标题
st.markdown('<span style="font-size:20px;"><font color=blue >*Calidornia housing*</font></span>',
            unsafe_allow_html=True)

# 写入描述
st.write("This program is designed to analyze and visualize various aspects of the California housing market using Python libraries such as pandas, matplotlib, seaborn, and Streamlit. It reads housing data from a CSV file and provides interactive data visualizations to explore relationships between housing prices, population density, and geographical location. Users can view scatter plots of housing prices against location, histograms comparing median income and house values, and bar plots of average house values by ocean proximity. Additionally, there's a line plot showing the relationship between the age of houses and their values, as well as a scatter plot with a regression line illustrating the correlation between median income and house values. The program is interactive and web-friendly, leveraging Streamlit to display data and images on a user-friendly dashboard.")

expender = st.expander('Picture')

with expender:
    for i in url:
        st.image(i)
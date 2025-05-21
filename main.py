import pandas
import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/profile_img.jpg")

with col2:
    st.title("Mohamed Farveez")
    st.info("""A passionate and self-driven Computer Science Engineering graduate with a strong foundation in full stack web development using Python. 
    Skilled in leveraging powerful frameworks such as Django, Flask, and Streamlit to build robust, scalable, and user-friendly web applications. 
    I thrive in collaborative environments where innovation meets problem-solving and continuously seek opportunities to learn and grow in real-world development projects.

My academic background is backed by hands-on experience in building full-stack solutions, integrating front-end interfaces with efficient back-end logic and databases. 
I’m enthusiastic about clean code, automation, and creating seamless user experiences. Whether it’s building a REST API with Django, 
designing a lightweight web app with Flask, or crafting interactive dashboards using Streamlit, I aim to deliver impactful software that solves real problems.

Eager to join a forward-thinking team where I can contribute fresh ideas, adapt quickly, and grow as a Python full stack developer.""")

st.write("Here are some of my projects that showcase my Python skill set")

df = pandas.read_csv("data.csv", sep=";")

col3, col4 = st.columns(2)

with col3:
    for index, row in df[:10].iterrows():
        st.title(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[source code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.title(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[source code]({row['url']})")
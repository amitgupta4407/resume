import streamlit as st
import requests

from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
from streamlit_extras.add_vertical_space import add_vertical_space 

st.set_page_config(initial_sidebar_state ="expanded")

with open("style.css") as f:
    st.markdown(f'<style>{f.read()}<style>', unsafe_allow_html=True)

def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        print("Failed to load lottie animation")
        return None
    return r.json()

lottie_coder = load_lottie_url('https://lottie.host/63ee9a86-e370-4ec9-8267-378adf7d9f02/aMjXDnjrKb.json')
lottie_pdf = load_lottie_url("https://lottie.host/2f91a4da-fb76-428c-8bfd-1f0913214008/1IWHBtsSRH.json")
lottie_searchImg = load_lottie_url("https://lottie.host/cae84fb8-6438-4e6a-8383-82bfae4a7adc/ni6XMP7tno.json")
st.write("##")

st.subheader("Hey Guys :wave:")
st.title("My Portfolio Website")
# st.write("<div class='my-class'>Hello, world!</div>", unsafe_allow_html=True)
st.write("I am an enthusiastic final-year B.Tech graduate with a strong foundation in computer science and a passion for problem-solving. Proficient in various programming languages and experienced in projects, I am eager to contribute my skills and knowledge to exciting opportunities in technology and engineering.")

st.write("---")

with st.container():
    selected = option_menu(
        menu_title=None,
        options=["About", "Projects", "Blog", "Contact"],
        icons=["person", "code-slash","pencil", "chat-left-text-fill"],
        orientation='horizontal'
    )

if selected=="About":
    with st.container():
        col1,col2 = st.columns(2)
        with col1:
            st.write("##")
            st.subheader("I am Amit Kumar Gupta")
            st.title("Undergrade at BIT")
        with col2:
            st_lottie(lottie_coder)
    st.write("---")

    with st.container():
        col3,col4 = st.columns(2)
        with col3:
            st.subheader("""
                        Education
                         - **Birsa Institute of Technology, Sindri**
                            - B.Tech in Electronics and Communication Engineering
                            - CGPA: 9.09 
                        - **Sardar Patel Public School (Senior Secondary)**
                            - Senior Secondary - XII
                            - Percentage (CBSE): 94% (2018 - 2020)
                        - **Sardar Patel Public School (Secondary)**
                            - Secondary School - X
                            - Percentage (CBSE): 89.4% (2018)      
            """)
        with col4:
            st.subheader("""
                        Experience
                            - Grain Bazar ~ Internship
                            - Duration
                            - Raipur
            """)
if selected=="Projects":
    col5, col6 = st.columns([3,1])
    with col6:
        add_vertical_space(3)
        st_lottie(lottie_pdf)
    with col5:
        st.write("""

        ### AllAboutPDF       &nbsp;  (Date: Aug 2023 )
        - TrainWithPDF is an online application designed for handling PDF files.
        - It offers a range of functionalities, including extracting metadata, images, text, and annotations from PDFs.
        - One of the standout features of this application is ChatPDF, which utilizes LangChain's natural language processing technology and OpenAI to enable users to interact with their PDFs.
        """)
    st.caption("---")

    col6, col5 = st.columns([1,3])
    with col6:
        add_vertical_space(3)
        st_lottie(lottie_searchImg)
    with col5:
        st.write("""
        ### LSB-Stenography &nbsp;  (Date: March 2023 )
        - Python project for performing basic stenography on images using the Python Imaging Library (PIL).
        - Allows hiding a message within an image without visibly altering its appearance
        - Written in Python using the PIL library.
        """)
    st.caption("---")

    col5, col6 = st.columns([3,1])
    with col6:
        add_vertical_space(3)
        st_lottie(lottie_pdf)
    with col5:
        st.write("""

        ### AllAboutPDF       &nbsp;  (Date: Aug 2023 )
        - TrainWithPDF is an online application designed for handling PDF files.
        - It offers a range of functionalities, including extracting metadata, images, text, and annotations from PDFs.
        - One of the standout features of this application is ChatPDF, which utilizes LangChain's natural language processing technology and OpenAI to enable users to interact with their PDFs.
        """)
    st.caption("---")






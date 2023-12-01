from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from st_on_hover_tabs import on_hover_tabs

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# use local Css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
local_css("style/style.css")

# --- Load Assets ---
lottie_coding = load_lottieurl("https://lottie.host/6eeeaac3-110b-46f6-b949-b85a3977add6/GaWiYaYx0A.json")
lottie_email = load_lottieurl("https://lottie.host/cf262121-a926-4935-b875-de2f0c5e1443/egpAV4JoPj.json")
img_project1 = Image.open("images/Basketball_Counter_App.png")
img_lottie_animation = Image.open("images/webpageImage2.png")

# --- Side Bar Section ---
with st.sidebar:
        tabs = on_hover_tabs(tabName=['Home', 'Project' ,'About', 'Feedback'], 
                             iconName=['home', 'link', 'info', 'mail'],
                             styles = {'navtab': {'background-color':'#111',
                                                  'color': '#818181',
                                                  'font-size': '18px',
                                                  'transition': '1s',
                                                  'white-space': 'nowrap',
                                                  'text-transform': 'uppercase'},
                                       'tabOptionsStyle': {':hover :hover': {'color': 'red',
                                                                      'cursor': 'pointer'}},
                                       'iconStyle':{'position':'fixed',
                                                    'left':'7.5px',
                                                    'text-align': 'left'},
                                       'tabStyle' : {'list-style-type': 'none',
                                                     'margin-bottom': '30px',
                                                     'padding-left': '30px'}},
                             key="1" ,default_choice=0)

# --- Home Section ---
if tabs =='Home':
    with st.container():
        st.write("---")
        st.title("This is my sample webpage")
        st.subheader("Hi :wave:, I am Jemaica Jhade O. Centino")
        st.write("I am a Computer Engineering students from SNSU")
        st.write("To know my projects visit my github link below.")
        st.write("[Github Link Here](https://github.com/YourEnemy1)")

# --- Projects Section ---
elif tabs == 'Project':
    with st.container():
        st.write("---")
        st.header("My Project")
        st.write("##")
        image_column, text_column = st.columns((1,2)) # (image_column size, text_column size)
        with image_column:
            # insert image
            st.image(img_project1)
        with text_column:
            st.subheader("Basketball Score Counter App")
            st.write(
                """ 
                This is a Basketball Score Counter made in Html, Css and Java Script. 
                """
                """ 
                This web app is not fully finish. 
                """
                """
                This is a sample for fun web app only. 
                """
            )
            st.markdown("[Github Link](https://github.com/YourEnemy1/Basketball-Score-Counter)")
    with st.container():
        image_column, text_column = st.columns((1,2)) # (image_column size, text_column size)
        with image_column:
            st.image(img_lottie_animation) # insert image
        with text_column:
            st.subheader("How to add a contact form in your Streamit App")
            st.write(
                """
                Want to add a contact form to your streamlit website.
                In this video, I'm going to show you how to implement a contact form in your Streamlit app using the free service 'Form Submit'.
                """
            )
            st.markdown("[Watch Here](https://youtu.be/FOULV9Xij_8)")

# --- About Section ---
elif tabs == 'About':
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("About Me")
            st.write("##")
            st.write("""
                I am a computer engineering student in Surigao del Norte State University.
                - I am currently studying Python, Java, Html and Css.
                - All of my projects is not final and currently ongoing.
                - I'm going to finish this soon.
            """)
            st.write("For the meantime you can watch this youtube video to learn more about how to make a webpage!")
            st.write("[Youtube](https://youtube.com/c/CodingIsFun)")
        with right_column:
            st_lottie(lottie_coding, height=500, key="coding")

# --- Feedback form Section ---
elif tabs == 'Feedback':
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("Get in touch with me!")
        st.write("##")
        contact_form = """
        <form action="https://formsubmit.co/jemaicajhade.30@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st_lottie(lottie_email, height=200, key="email")
import streamlit as st
from groq import Groq

st.set_page_config(page_title='AI Interview Assistant', layout='centered')
st.title('AI Interview Assistant')
st.caption('practice interviews with AI-generated questions and constructive feedback.')
st.caption("lunched by ajay")
st.write("department of AI&DS")
TRY:
Client = GROQ(api_key=st.secrets['GREQ_API_KEY'])
Except (key, FillNotFoundRrror):
st.error('GROQ_API_KEY is missing. Add it to streamlit cloud
         st.stop()
         

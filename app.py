import os
from apikey import apikey
import streamlit as st
from langchain.llms import OpenAI
import tiktoken
import gradio as gr
import openai
import time

os.environ['OPENAI_API_KEY'] = apikey

# Set your OpenAI API key
openai.api_key = apikey        

st.title("Spiral Demo")

# Get the prompt from the user
prompt = st.text_area("Enter your thoughts:")

# Check the safety of the prompt
if st.button("Post"):
    response = openai.Moderation.create(
        model="text-moderation-stable",
        input=[prompt],
    )
    
    if response["results"][0]["flagged"] == True:
        st.warning("This content is not safe and should be moderated.", icon="⚠️")
        category_scores = response["results"][0]["category_scores"]
        highest_category_score = max(category_scores.values())

        for category, score in category_scores.items():
            if score == highest_category_score:
                stg = "The content is blocked since it contains a category of violation: " + category
                st.warning(stg, icon="⚠️")
        
        # Clear the text input and hide the button
        button_clicked = st.button("Submit for admin check")
            
        
    else:
        st.write("My post:")
        #st.write(response)
        st.write(prompt)


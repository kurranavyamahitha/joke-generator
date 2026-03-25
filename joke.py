import streamlit as st
import requests
st.title("😆 Random Joke Generator")
if st.button("get joke"):
    url="https://official-joke-api.appspot.com/random_joke"
    with st.spinner("Fetching a funny joke... 😄"):
        response=requests.get(url)
        if response.status_code==200:
            data=response.json()
            st.write("### Here's your joke:")
            st.success(data["setup"])
            st.info(data["punchline"])
        else:
            st.error("Failed to fetch joke. Try again!")
    

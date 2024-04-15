import streamlit as st
import time
import datetime

# Create an empty placeholder
text_placeholder = st.empty()

# Text to be displayed
text = "Hello, World!"

def getTime():
    return datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')
localtime = time.localtime()


# Loop to repeatedly update the text
while True:

    result = datetime.datetime.now().strftime("%I:%M:%S %p")
    # Update the text in the placeholder
    text_placeholder.text(result)
   
    # Wait for a few seconds before updating again
    time.sleep(1)



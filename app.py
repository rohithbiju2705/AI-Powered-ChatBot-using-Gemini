import streamlit as st
from dotenv import load_dotenv
import os
from PIL import Image
import google.generativeai as genai


# Load API key from .env
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the model
model = genai.GenerativeModel("gemini-pro")

# Define helper function for generating a response
def get_gemini_response(question, image=None):
    # You can extend this logic to use image input if needed
    response = model.generate_content(question)
    return response.text

# Streamlit app configuration
st.set_page_config(page_title="Gemini AI ChatBot")
st.header("Gemini AI ChatBot")

# Input fields
name = st.text_input("Ante Per entha: ", key="name")
input_prompt = st.text_input("Ask a question: ", key="input")
uploaded_file = st.file_uploader("Upload an image (optional):", type=["jpg", "jpeg", "png"])

# Show the uploaded image
image = None
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

# Submit button
submit = st.button("Get Response")

# Generate response on button click
if submit:
    if name.strip() == "":
        st.warning("Please enter your name.")
    elif input_prompt.strip() == "":
        st.warning("Please enter a question.")
    else:
        st.write(f"Hello, {name}!")
        response = get_gemini_response(input_prompt, image)
        st.subheader("Gemini AI Response:")
        st.write(response)




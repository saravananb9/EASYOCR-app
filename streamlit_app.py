import streamlit as st
import easyocr
import cv2

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])  # Specify language(s) if needed

# Title and image upload
st.title("Text Extraction from Image")
uploaded_file = st.file_uploader("Choose an image")

if uploaded_file is not None:
    image = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), 1)

    # Perform text extraction
    result = reader.readtext(image)

    # Display image and extracted text
    st.image(image, caption="Uploaded Image")
    st.write("Extracted Text:")
    for text in result:
        st.write(text[1])

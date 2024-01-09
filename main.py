import streamlit as st
from PIL import Image, ImageTk
import numpy as np
from io import BytesIO

def encrypt_image(original_image, key):
    try:
        encrypted_image = original_image.copy()

        original_pixels = original_image.load()
        encrypted_pixels = encrypted_image.load()

        # Iterate through each pixel and apply the Caesar cipher to all RGB channels
        width, height = encrypted_image.size
        for i in range(width):
            for j in range(height):
                current_pixel_value = original_pixels[i, j]
                encrypted_pixel = tuple((val + key) % 256 for val in current_pixel_value)  # Encrypt each channel of the pixel using the Caesar cipher
                encrypted_pixels[i, j] = encrypted_pixel  # Update the pixel value in the encrypted image

        return encrypted_image

    except Exception as e:
        st.error(f"Error: {str(e)}")
        return None

def main():
    st.title("Image Cypher")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "gif"])

    key = st.number_input("Please Enter Key:", min_value=0, step=1)

    if uploaded_file and key is not None:
        original_image = Image.open(uploaded_file)
        encrypted_image = encrypt_image(original_image, key)

        if encrypted_image:
            col1, col2 = st.columns(2)
            col1.image(original_image, caption="Original Image", use_column_width=True)
            col1.subheader("Original Image Pixels")
            col1.text(str(np.array(original_image.getdata())))

            col2.image(encrypted_image, caption="Encrypted Image", use_column_width=True)
            col2.subheader("Encrypted Image Pixels")
            col2.text(str(np.array(encrypted_image.getdata())))

            st.subheader("Download Images")
            button_col1, button_col2 = st.columns(2)
            
            original_download_button = button_col1.button("Original Image")
            encrypted_download_button = button_col2.button("Encrypted Image")

            if original_download_button:
                original_bytes = BytesIO()
                original_image.save(original_bytes, format='PNG')
                st.download_button(label="Download Original Image", data=original_bytes.getvalue(), file_name="original_image.png", key="original")

            if encrypted_download_button:
                encrypted_bytes = BytesIO()
                encrypted_image.save(encrypted_bytes, format='PNG')
                st.download_button(label="Download Encrypted Image", data=encrypted_bytes.getvalue(), file_name="encrypted_image.png", key="encrypted")
        else:
            st.warning("Encryption failed.")

if __name__ == "__main__":
    main()

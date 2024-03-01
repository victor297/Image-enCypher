# Image enCypher 🖼️

## Introduction 🚀

The Image Cypher application allows users to encrypt images using a simple Caesar cipher algorithm. This tool can be used for basic image encryption and serves as an example of image manipulation with Streamlit.

## Features ✨

- Upload an image in JPG, JPEG, PNG, or GIF format.
- Enter a key to encrypt the image using a Caesar cipher.
- View both the original and encrypted images side by side.
- Download the original and encrypted images for further analysis.

## Usage ℹ️

1. Upload Image: Click on the "Choose an image..." button and select an image file from your local device.
2. Enter Key: Input a numeric key value to apply the Caesar cipher for encryption.
3. View Results: Observe the original and encrypted images along with their pixel values.
4. Download Images: Download the original and encrypted images for offline use or analysis.

## How It Works 🛠️

- The application uses the Streamlit library for the user interface.
- Uploaded images are encrypted using a Caesar cipher algorithm, where each RGB channel of every pixel is shifted by the specified key value.
- Encrypted images are displayed alongside the original images for comparison.
- Users can download the original and encrypted images in PNG format for further examination.

## Future Enhancements 🌟

- Implement additional encryption algorithms for increased security.
- Add decryption functionality to reverse the encryption process.
- Enhance the user interface with more customization options and visualizations.

## Dependencies 📦

- Streamlit: `pip install streamlit`
- PIL (Python Imaging Library): Included in most Python distributions

## Running the Application ▶️

1. Clone the repository or download the source code.
2. Install the necessary dependencies.
3. Run the script.
4. Access the application via the provided URL in your web browser.

## About the Author ℹ️

This application was created by ME.

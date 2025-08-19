import streamlit as st
from PIL import Image
import io

# Page config
st.set_page_config(
    page_title="Image ReQuality App",
    page_icon="📸",
    layout="centered"
)

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main {
        background-color: #f9fafc;
        padding: 20px;
        border-radius: 12px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 20px;
    }
    .stDownloadButton>button {
        background-color: #2196F3;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.title("📸 Image ReQuality App")
st.write("Easily increase or decrease image quality and resolution.")

# File uploader
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Open image
    img = Image.open(uploaded_file)
    st.image(img, caption="🖼️ Original Image", use_column_width=True)

    st.subheader("⚙️ Adjust Quality Settings")

    # Slider for JPEG quality
    quality = st.slider("Select JPEG Quality", 1, 100, 80)

    # Resize options
    resize_factor = st.slider("Resize Factor", 0.1, 3.0, 1.0, step=0.1)

    # Process image
    new_width = int(img.width * resize_factor)
    new_height = int(img.height * resize_factor)
    resized_img = img.resize((new_width, new_height))

    # Convert RGBA/Palette to RGB if saving as JPEG
    if resized_img.mode in ("RGBA", "P"):
        resized_img = resized_img.convert("RGB")

    if st.button("✨ Process Image"):
        buf = io.BytesIO()
        resized_img.save(buf, format="JPEG", quality=quality)
        byte_im = buf.getvalue()

        # Download button
        st.download_button(
            label="📥 Download Processed Image",
            data=byte_im,
            file_name="processed.jpg",
            mime="image/jpeg"
        )
        st.success("✅ Image processed successfully!")

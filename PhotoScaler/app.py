import streamlit as st
from PIL import Image
import io

st.set_page_config(page_title="Image ReQuality App", layout="centered")

st.title("📸 Image Quality Increase/Decrease App")
st.write("Upload an image and adjust its quality or resolution.")

# File uploader
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Open image
    img = Image.open(uploaded_file)
    st.image(img, caption="Original Image", use_column_width=True)

    st.subheader("⚙️ Adjust Quality Settings")

    # Slider for JPEG quality
    quality = st.slider("Select JPEG Quality", 1, 100, 80)

    # Resize options
    resize_factor = st.slider("Resize Factor (e.g., 0.5 = half, 2 = double)", 0.1, 3.0, 1.0)

    # Process image
    new_width = int(img.width * resize_factor)
    new_height = int(img.height * resize_factor)
    resized_img = img.resize((new_width, new_height))

    if st.button("Save Processed Image"):
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

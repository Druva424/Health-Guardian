import streamlit as st

def home():
    st.set_page_config(
        page_title="Health Guardian",
        page_icon="👨‍⚕️",
    )
    st.sidebar.info(
        "**About**: This project is made using publicly available data and comes with no guarantee. We do not store any of the patient's personal information."
    )

    # Title

    # Logo
    col1, col2, col3 = st.columns([1, 6, 1])
    with col1:
        st.write("")
    with col2:
        st.image("assets/logo_rounded.png")
    with col3:
        st.write("")

    # Description
    st.markdown("<p style='font-size:22px; text-align: center; color: black;font-size: 25px;'>Improving Healthcare, Improving Lives, Bridging the gap between technology and health</p>", unsafe_allow_html=True)
    st.markdown("---")

    # About the website
    st.markdown("<h2 style='text-align: center; color: yellow; background-color: black;'>About the website</h2>", unsafe_allow_html=True)
    st.write("")

    st.markdown("💠 We use state-of-the-art machine learning and deep learning technologies to provide you with your own virtual Health Consultant.")
    st.markdown("💠 We provide digital health and healthcare solutions to help common people and health organizations power their care experience and improve health outcomes with advanced analytics.")
    st.markdown("---")

    # Our Services
    st.markdown("<h2 style='text-align: center; color: yellow; background-color: black;'>Our Services</h2>", unsafe_allow_html=True)
    st.write("")

    st.markdown("Our services include:")
    st.markdown("⚕️ **Disease Diagnosis**: Enter the symptoms you are suffering from and get information about the disease, precautions, medications, and specialists near you to cure the disease.")
    st.markdown("⚕️ **Early Diabetes Detection**: Enter the patient's attributes from the test report and check for chances of diabetes.")
    st.markdown("⚕️ **Liver Disease Detection**: Enter the patient's attributes from the test report and check for chances of any type of liver disease.")
    st.markdown("⚕️ **Malaria Detection**: Upload the microscopic cell image of the patient and check for chances of malaria.")
    st.markdown("⚕️ **Pneumonia Detection**: Upload the chest X-ray image of the patient and check for chances of pneumonia.")
    st.markdown("---")

    # Disclaimer
    st.warning("**Disclaimer**: The information on this site is not intended to be a substitute for professional medical advice, diagnosis, or treatment. Always consult with your physician for medical advice. We do not endorse specific tests, products, procedures, or treatments.")
    st.markdown("Please note that this project is based on publicly available data and does not store any personal information.")

if __name__ == "__main__":
    home()

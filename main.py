import streamlit as st
import pyqrcodeng as pyqrcode
from PIL import Image

QR_FILE = 'qrcode.png'
QR_CODE_COLOR = (80, 20, 80)
BACKGROUND_COLOR = (250, 250, 250)

st.title('QR Code Generator App')
st.subheader('You can generate a QR code from a string or URL.')
st.text('PyQRCodeNG version')


qr_url = st.text_input('Enter a string or URL to generate a QR code:', value='https://code2create.club/')
qr_version = st.sidebar.slider('Version (1-10)', 1, 10, value=5)
qr_correction = st.sidebar.select_slider(
                    "Error Correction Grade: [L, Q, M, H]",
                    options=['L', 'Q', 'M', 'H'], value='H')
qr_scale = st.sidebar.slider('Scale (4-8)', 4, 8, value=6)

try:
    qr = pyqrcode.create(qr_url, error=qr_correction, version=qr_version, mode='binary')
    qr.png(QR_FILE, scale=qr_scale, module_color=QR_CODE_COLOR, background=BACKGROUND_COLOR, quiet_zone=4)
    img = Image.open(QR_FILE)
    st.text(f'Length: {len(qr_url)}')
    st.text(f'[QR Code Version: {qr.version}]   [Error Correction Grade: {qr.error}]   [Mode: {qr.mode}]   [Scale: {qr_scale}]')
    st.image(img)
except Exception as e:
    st.error(f'Length: {len(qr_url)}')
    st.error('Error: Data Overflow. Please select smaller version number or lower Error Correction Grade')
    # st.write(e)

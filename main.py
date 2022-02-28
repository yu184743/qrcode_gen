# QR Code Generator
# PyQRCodeNG version https://github.com/pyqrcode/pyqrcodeNG

import streamlit as st
import pyqrcodeng as pyqrcode
from PIL import Image

QR_FILE = 'qrcode.png'
QR_CODE_COLOR = (80, 20, 80, 255)
BACKGROUND_COLOR = (250, 250, 250, 255)

st.title('QR Code Generator App')
st.subheader('You can generate a QR code from a string or URL.')
st.text('PyQRCodeNG version')

qr_url = st.text_input('Enter a string or URL to generate a QR code:', value='https://code2create.club/')
qr_version = st.sidebar.slider('Version (1-10)', 1, 10, value=5)
qr_correction = st.sidebar.select_slider(
                    "Error Correction Grade: [L, M, Q, H]",
                    options=['L', 'M', 'Q', 'H'], value='H')
qr_scale = st.sidebar.slider('Scale (4-8 pixels/cell)', 2, 8, value=4)

try:
    qr = pyqrcode.create(qr_url, error=qr_correction, version=qr_version, mode='binary')
    qr.png(QR_FILE, scale=qr_scale, module_color=QR_CODE_COLOR, background=BACKGROUND_COLOR, quiet_zone=4)
    img = Image.open(QR_FILE)
    st.text(f'Length: {len(qr_url)}')
    st.text(f'[QR Code Version: {qr.version}]   \
              [Error Correction Grade: {qr.error}]   \
              [Mode: {qr.mode}]   \
              [Scale: {qr_scale}]')
    st.image(img)
except pyqrcode.DataOverflowError:
    st.error(f'Length（文字数）: {len(qr_url)}')
    st.error('Error: Data Overflow. Please select a smaller version number or a lower Error Correction Grade')
    st.error('エラー：データあふれ　バージョンやエラー訂正のグレードを下げてください。')
except Exception as e:
    st.write(e)

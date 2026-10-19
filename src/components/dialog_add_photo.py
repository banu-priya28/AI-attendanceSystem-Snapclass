import streamlit as st
from src.database.config import supabase
from src.database.db import enroll_student_to_subject
from PIL import Image




@st.dialog('Capture or upload photos')
def add_photos_dialog():
    st.write('Add classroom photos to scan for attendance')

    if 'photo_tab' not in st.session_state:
        st.session_state.photo_tab = 'camera'

    t1, t2 = st.columns(2)

    with t1:
        if st.button(
            'Camera',
            type='primary' if st.session_state.photo_tab == 'camera' else 'tertiary',
            width='stretch',
            key='photo_camera_tab'
        ):
            st.session_state.photo_tab = 'camera'
            st.rerun()

    with t2:
        if st.button(
            'Upload photos',
            type='primary' if st.session_state.photo_tab == 'upload' else 'tertiary',
            width='stretch',
            key='photo_upload_tab'
        ):
            st.session_state.photo_tab = 'upload'
            st.rerun()

    if st.session_state.photo_tab == 'camera':
        cam_photo = st.camera_input('Take Snapshot', key='dialog_cam')

        if cam_photo is not None:
            image = Image.open(cam_photo).convert('RGB')
            st.session_state.attendance_images.append(image)
            st.success('Photo captured and added!')
            st.rerun()

    elif st.session_state.photo_tab == 'upload':
        uploaded_files = st.file_uploader(
            'Choose image files',
            type=['jpg', 'png', 'jpeg'],
            accept_multiple_files=True,
            key='dialog_upload'
        )

        if uploaded_files:
            existing_count = len(st.session_state.attendance_images)

            for f in uploaded_files:
                image = Image.open(f).convert('RGB')
                st.session_state.attendance_images.append(image)

            st.success(
                f'{len(st.session_state.attendance_images) - existing_count} photo(s) added!'
            )
            st.rerun()

    st.divider()

    st.write(f"Photos added: {len(st.session_state.attendance_images)}")

    if st.button('Done', type='primary', width='stretch'):
        st.rerun()

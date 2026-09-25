
import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

from detector import detect_objects


st.set_page_config(
    page_title="Assistive Object Detection",
    page_icon="👁️",
    layout="wide"
)


st.title("Assistive Object Detection System")

st.write(
    "A computer vision prototype for detecting objects "
    "and providing basic assistive scene information."
)


# Session state
if "scene_description" not in st.session_state:
    st.session_state.scene_description = None


uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)


if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.subheader("Original Image")
    st.image(image, width=500)


    if st.button("Detect Objects"):

        with st.spinner("Detecting objects..."):

            results, detections = detect_objects(image)
            result_image = results[0].plot()


        st.subheader("Detected Objects")
        st.image(result_image, channels="BGR", width=500)


        st.subheader("Assistive Scene Information")


        if detections:

            descriptions = []

            for detection in detections:

                object_name = detection["object"]
                confidence = detection["confidence"]
                position = detection["position"]


                st.write(
                    f"**{object_name.title()}** detected "
                    f"on the **{position}** "
                    f"(confidence: {confidence:.2f})"
                )


                descriptions.append(
                    f"{object_name} detected on the {position}"
                )


            scene_description = (
                ". ".join(descriptions) + "."
            )


            # Save scene description
            st.session_state.scene_description = scene_description


            st.subheader("Scene Description")
            st.info(scene_description)


        else:

            st.session_state.scene_description = None

            st.write("No objects detected.")


# Read scene aloud button
if st.session_state.scene_description:

    st.subheader("Audio Assistance")

    if st.button("Read Scene Aloud"):

        scene_text = st.session_state.scene_description

        # Escape text safely for JavaScript
        import json

        safe_text = json.dumps(scene_text)

        components.html(
            f"""
            <script>
                const text = {safe_text};

                const utterance =
                    new SpeechSynthesisUtterance(text);

                utterance.rate = 0.9;
                utterance.pitch = 1.0;

                window.speechSynthesis.cancel();
                window.speechSynthesis.speak(utterance);
            </script>
            """,
            height=50,
        )

        st.success("Scene description is being read aloud.")

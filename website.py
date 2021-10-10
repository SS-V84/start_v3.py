import streamlit as st
import time
from color4 import *
# from tempfile import NamedTemporaryFile

# st.set_option('browser.serverAddress', '192.168.100.17')
# st.set_option('server.port', 8080)

st.header("**Сucumber Сlassifier**")

uploaded_file = st.file_uploader(label = "Please upload your file")
# st.write(type(uploaded_file ))

if uploaded_file is not None:
  my_img = Image.open(uploaded_file)
  myimg = np.array(my_img)
  # st.write(type(myimg))
  answer=start(myimg)

    # st.header("Transcribed Text")
    # st.subheader(answer['text'])
  st.header(f"**The sample is close to the standard № {answer}**")
  st.balloons()
# if  img_name:
#     my_img = Image.open(img_name)
#     frame = np.array(my_img)
    # upload_file(img_name)
    # result = {}
    # #polling
    # sleep_duration = 1
    # percent_complete = 0
    # progress_bar = st.progress(percent_complete)
    # st.text("Currently in queue")
    # while result.get("status") != "processing":
    #     percent_complete += sleep_duration
    #     time.sleep(sleep_duration)
    #     progress_bar.progress(percent_complete/10)
    #     result = get_text(token,t_id)
    #
    # sleep_duration = 0.01
    #
    # for percent in range(percent_complete,101):
    #     time.sleep(sleep_duration)
    #     progress_bar.progress(percent)
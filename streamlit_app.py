import os
import subprocess
import streamlit as st
import threading
import psutil

# Define the command to be executed
cmd = (
    "chmod +x ./start.sh && "
    "nohup ./start.sh > /dev/null 2>&1 & "
    "while [ ! -f list.log ]; do sleep 1; done; "
    "rm -rf list.log &&"
    "rm -rf /tmp/list.log &&"
    "echo 'app is running' "
)

st.title("❤️抖音美女欣赏❤️")
video_paths = ["linman.mp4", "luoxi.mp4", "nixiaoni.mp4","luoman.mp4","luoman2.mp4","mazhuo.mp4"]

# Display each video if it exists
for video_path in video_paths:
    if os.path.exists(video_path):
        st.video(video_path)


# Define the URL of the website you want to proxy
url = "https://douyin.boo/index.html"

# 去掉下面一句前面#，可以显示网页版抖音美女
#st.components.v1.html(f'<iframe src="{url}" width="100%" height="600" style="border:none;"></iframe>', height=700)

image_path = "./mv.jpg"
if os.path.exists(image_path):
    st.image(image_path, caption='林熳', use_column_width=True)

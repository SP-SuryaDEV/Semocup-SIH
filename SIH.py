# import streamlit as st
# import pandas as pd
# import time

# # st.markdown("""
# #     <h1 style="text-align: center; text-decoration: underline;">💡Smart India Hackathon💡</h1>
# # """, unsafe_allow_html=True)

# #st.header("Architecture & Workflows",divider='orange')
# st.set_page_config(layout="wide", page_title="Smart India Hackathon Architecture", page_icon="🏛️")
# st.markdown("""
#     <h1 style="text-align: center; text-decoration: underline;">🏛️Smart India Hackathon: Architecture & Workflows🏛️</h1>
# """, unsafe_allow_html=True)

# @st.dialog("Note from 'The Horizon'",width='large')
# def poping():
#     st.markdown("""
#         <style>
#         .header {
#             text-align: center;
#             font-size: 3em; /* Larger header */
#             color: #FF5722; /* Vibrant orange */
#             font-weight: bold;
#             padding: 20px 0;
#             border-bottom: 4px solid #FF5722;
#         }
#         .intro {
#             text-align: center;
#             font-size: 22px; /* Larger font size */
#             color: #E0E0E0; /* Light gray */
#             margin: 40px 0;
#             line-height: 1.8;
#         }
#         .highlight {
#             color: #FF9800; /* Highlight color */
#             font-weight: bold;
#         }
#         .highlight1 {
#             color: #00BCD4; /* Highlight color */
#             font-weight: bold;
#         }
#         .emphasis {
#             color: #4CAF50; /* Green for emphasis */
#             font-weight: bold;
#         }
#         .emoji {
#             font-size: 1.7em; /* Larger emojis */
#         }
#         .call-to-action {
#             text-align: center;
#             font-size: 24px;
#             font-weight: bold;
#             color: #FF5722; /* Call to action color */
#             padding: 15px;
#             border-radius: 10px;
#             background-color: #FFE0B2; /* Light background */
#         }
#         </style>
#         <div class="header">🌟 Welcome! 🎉</div>
#         <div class="intro">
#             <p class="emoji">👋 Hello Judges!</p>
#             <p>First of all, <span class="highlight">thank you for clicking this link</span>! If you're here, it means we've successfully piqued your interest with our approach. Curious about the details of our solution? <span class="emphasis">No worries!</span></p>
#             <p>This page has been designed by <span class="highlight">"The Horizon"</span> from <span class="highlight1">Chennai Institute of Technology</span> to provide you with an even clearer insight into our work. <span class="emphasis">Let's dive in and enjoy the journey! 🚀</span></p>
#         </div>
#     """, unsafe_allow_html=True)
    
# poping()
# # def About_section():
# #     st.markdown("""
# #     <style>
# #     @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
# #     .stApp {
# #         background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
# #         background-size: 400% 400%;
# #         animation: gradient 15s ease infinite;
# #     }
# #     [data-testid="stAppViewContainer"] > .main {
# #         background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
# #         background-size: 400% 400%;
# #         animation: gradient 15s ease infinite;
# #     }
# #     .stToolbar {
# #         background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
# #         background-size: 400% 400%;
# #         animation: gradient 15s ease infinite;
# #     }
# #     .stAppViewContainer {
# #         background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
# #         background-size: 400% 400%;
# #         animation: gradient 15s ease infinite;
# #     }          
# #     @keyframes gradient {
# #         0% {background-position: 0% 50%;}
# #         50% {background-position: 100% 50%;}
# #         100% {background-position: 0% 50%;}
# #     }
# #     .card {
# #         background: rgba(255, 255, 255, 0.1);
# #         backdrop-filter: blur(10px);
# #         border-radius: 20px;
# #         padding: 20px;
# #         margin: 10px;
# #         box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
# #         border: 1px solid rgba(255, 255, 255, 0.18);
# #         transition: all 0.3s ease;
# #     }
# #     .card:hover {
# #         transform: translateY(-10px);
# #         box-shadow: 0 12px 48px 0 rgba(31, 38, 135, 0.5);
# #     }
# #     .title {
# #         font-family: 'Poppins', sans-serif;
# #         font-size: 3rem !important;
# #         font-weight: 700;
# #         color: #ffffff;
# #         text-align: center;
# #         margin-bottom: 30px;
# #         text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
# #     }
# #     .subtitle {
# #         font-family: 'Poppins', sans-serif;
# #         font-size: 1.8rem !important;
# #         font-weight: 600;
# #         color: #ffff00;
# #         margin-bottom: 20px;
# #     }
# #     .content {
# #         font-family: 'Poppins', sans-serif;
# #         font-size: 1rem;
# #         color: #ffffff;
# #         line-height: 1.6;
# #     }
# #     .team-member {
# #         font-family: 'Poppins', sans-serif;
# #         font-size: 1.2rem;
# #         color: #ffffff;
# #         margin-bottom: 10px;
# #         opacity: 0;
# #         transform: translateX(50px);
# #         animation: slideIn 0.5s forwards;
# #     }
# #     @keyframes slideIn {
# #         to {
# #             opacity: 1;
# #             transform: translateX(0);
# #         }
# #     }
# #     .highlight {
# #         color: #00ffff;
# #         font-weight: bold;
# #     }
# #     </style>
# #     """, unsafe_allow_html=True)

# #     st.markdown('<h1 class="title">🚀 The Horizon: Crazy Gang from CIT 🚀</h1>', unsafe_allow_html=True)

# #     col1, col2 = st.columns(2)

# #     with col1:
# #         st.markdown(
# #             """
# #             <div class="card">
# #                 <h1 class="subtitle">🌟 Introduction</h1>
# #                 <p class="content">
# #                     Welcome to our project! We are <span class="highlight">"The Horizon"</span>, a dynamic group from 
# #                     <span class="highlight">CIT (Chennai Institute of Technology)</span>. We’ve taken on the 
# #                     challenge presented in Problem Statement <span class="highlight">SIH1670</span>, aiming to develop a 
# #                     robust solution that integrates the security of the ML model published by the 
# #                     <span class="highlight">Ministry of Electronics and Information Technology</span>, within the 
# #                     domain of <span class="highlight">Smart Automation</span>.
# #                     This page is designed to guide you through our solution, with each component explained clearly 
# #                     to facilitate your understanding. Buckle up and let’s dive into the details!
# #                 </p>
# #             </div>
# #             """,
# #             unsafe_allow_html=True
# #         )

# #     with col2:
# #         st.markdown(
# #             """
# #             <div class="card">
# #                 <h1 class="subtitle">🌈 Our Awesome Team</h1>
# #                 <h5>1. Prithvi Ragavendiran R (3rd Year EEE)</h5>
# #                 <h5>2. Surya Prabhakaran V P (3rd year CSE)</h5>
# #                 <h5>3. Rudhresh (3rd Year EEE)</h5>
# #                 <h5>4. Nishanth (2nd Year EEE)</h5>
# #                 <h5>5. Lokesh (4th Year CSE)</h5>
# #             </div>
# #             """,
# #             unsafe_allow_html=True
# #         )

# #     # Add some animated elements
# #     st.markdown(
# #         """
# #         <script>
# #         function createParticle() {
# #             const particle = document.createElement('div');
# #             particle.style.position = 'fixed';
# #             particle.style.width = '10px';
# #             particle.style.height = '10px';
# #             particle.style.background = '#ffffff';
# #             particle.style.borderRadius = '50%';
# #             particle.style.pointerEvents = 'none';
# #             particle.style.left = Math.random() * window.innerWidth + 'px';
# #             particle.style.top = window.innerHeight + 'px';
# #             particle.style.animation = `rise ${Math.random() * 3 + 2}s linear`;
# #             document.body.appendChild(particle);
# #             setTimeout(() => particle.remove(), 5000);
# #         }

# #         setInterval(createParticle, 200);

# #         const style = document.createElement('style');
# #         style.textContent = `
# #             @keyframes rise {
# #                 to {
# #                     transform: translateY(-100vh) rotate(360deg);
# #                     opacity: 0;
# #                 }
# #             }
# #         `;
# #         document.head.appendChild(style);
# #         </script>
# #         """,
# #         unsafe_allow_html=True
# #     )

# # # Call this function where you want to display the About section in your Streamlit app
# # About_section()
# box = st.container(border=True)

# with box:
#   st.subheader(":violet[1. 🖥️Liveliness Model (at Edge From MDN)]",divider='violet')
# col1,col2 = box.columns([1.2,1])
# with col1:
#  st.write(" ")
#  st.write(" ")
#  st.write(" ")
#  st.image("Model Arch1.gif",use_column_width=True,caption="Liveliness Model @Edge")
# with col2:
#  with st.container(border=True):
#   st.markdown("""
# ### About:
# 1. 🌐 <span style="color:blue;">**The Quantized Liveliness Model**</span> 🎯 for spoof detection is distributed from a **central Origin Server** 🚀 to all Model Delivery Networks (**MDNs**) across India

# 2. 🔒 Upon :green-background[**successful OTP authentication**] on the UIDAI website, ✅ the model is securely sent from the nearest MDN 📡 to the client-side device, accompanied by a <span style="color:yellow;">**unique edge token**</span> 🔑.

# 3. 🔐 Before transmission, the model is <span style="color:orange;">**encrypted**</span> 🛡️ using a unique key 🔏 to prevent reverse engineering attempts by client-side hackers 👾.

# 4. 🖥️ The **encrypted model** is deployed at the edge 💾 in a secure <span style="color:red;">**.EMSF format**</span> 🗝️ ensuring safe and efficient usage at the client’s end.
# """, unsafe_allow_html=True)
#   st.write(" ")
# # with box:
# #  with st.container(border=True):
# #   st.markdown("""<span style='font-size: 3em;'>:red[Outcome: ]</span>  <span style='font-size: 2em;'>"Liveliness Model" is deployed @Edge</span>""",unsafe_allow_html=True)
  
# ###################################

# box1 = st.container(border=True)
# with box1:
#   st.subheader(":violet[2. 🧑‍🤝‍🧑Face Embedding Model (at Cloud Connected to a vector Database)]",divider='violet')
# col11,col21 = box1.columns([1,1.2])
# with col21:
#  st.write(" ")
#  st.write(" ")
#  st.write(" ")
#  st.image("Model Arch11.gif",use_column_width=True,caption="Face-Embedding Model @Cloud")
# with col11:
#  with st.container(border=True):

#   st.markdown("""
# ### About:

# 1. 🌐 The <span style="color:cyan;">**Face Embedding Model**</span> 🧑‍🤝‍🧑 is deployed in a <span style="color:blue;">**secure cloud environment**</span> ☁️ alongside the <span style="color:blue;">**central vector database**</span> 🗃️ to ensure robust security and privacy.

# 2. 🧩 The model generates a <span style="color:green;">**128-dimension vector embedding**</span> 📏 for each user's face, representing its unique features.

# 3. 🔍 This vector embedding is compared with the embeddings stored in the central vector database, ensuring a resemblance of at least <span style="color:orange;">**98%**</span>.

# 4. ✅ If the generated vector embedding matches the database entry and both the **Quantized Liveliness Model** and the **Face Embedding Model** approve, the user is successfully <span style="color:green;">**authenticated**</span>.
# """, unsafe_allow_html=True)
  
# #############

# box2 = st.container(border=True)
# with box2:
#   st.subheader(":violet[3. 🛂Citizen Login (First-Time Login)]",divider='violet')
# col13,col23 = box2.columns([1.4,1])
# with col13:
#  st.write(" ")
#  st.write(" ")
#  st.write(" ")
#  ds1,ds2 = st.columns([0.85,0.3])
#  with ds1:
#   st.write(" ")
#   st.write(" ")
#   st.image("Login1.gif",use_column_width=True,caption="First Time Login")
#  with ds2:
#   data = pd.read_csv("random_keys.csv")
#   st.write("**Database:**")
#   def style_dataframe(styler):
#     styler.set_properties(**{
#         'background-color': 'white',
#         'color': 'black',
#         'border': '1px solid black',
#         'text-align': 'left'
#     })
#     styler.hide(axis="index")
#     return styler

# # Apply styles
#   styled_df = data.style.pipe(style_dataframe)
#   st.dataframe(styled_df,height=200,hide_index=True)
#  st.write(" ")
#  st.write(" ")
#  st.markdown("""
# ### The Following Values Get Added to the Database:
# <table style="width:100%">
#   <tr>
#     <td><span style="color:blue;"><b>UUID</b></span> 🆔<br>Unique User IDentification Number</td>
#     <td><span style="color:green;"><b>Edge Token</b></span> 🔑<br>Identifier for the model sent</td>
#   </tr>
#   <tr>
#     <td><span style="color:red;"><b>Encryption Key</b></span> 🔒<br>Used for securing the model</td>
#     <td><span style="color:red;"><b>Decryption Key</b></span> 🔓<br>Used for decrypting the model</td>
#   </tr>
#   <tr>
#     <td><span style="color:orange;"><b>Hash Key-M</b></span> 🧬<br>Hash of the model for integrity</td>
#     <td><span style="color:orange;"><b>Hask Key-U</b></span> 🔢<br>Hash of the UUID for integrity</td>
#   </tr>
# </table>
# """, unsafe_allow_html=True)

# with col23:
#  with st.container(border=True):
#   st.markdown("""
# ### About:
# 1. 🚪 When a user (resident) logs in for the **first time**, they are required to take the traditional <span style="color:green;">**OTP Authentication**</span> 🔑 route since they don't yet have the <span style="color:orange;">**Edge Model**</span> or <span style="color:orange;">**Edge Token**</span> stored on their device.

# 2. 📲 Upon successful OTP authentication ✅, a pop-up window will ask: <span style="color:cyan;">"Do you wish for these cookies to reside on your PC?"</span> 🍪. If the user accepts, a request is sent to the **MDN** 🌐.

# 3. 🔒 Before the <span style="color:red;">**Quantized Liveliness Model**</span> is sent to the client from the MDN, it is encrypted using a unique key 🔏. Along with the encrypted model, an <span style="color:green;">**Edge Token**</span> is also delivered 📡.

# 4. 🖥️ While making the request, a unique <span style="color:blue;">**UUID key**</span> 🌐 is generated for the Client Device. In the database, a new entry for the model sent is added.

# 5. 📂 Once this process is complete, the model is finally deployed at the <span style="color:orange;">**Edge**</span> 💾. The next time the user logs in, they will have the option to authenticate using either <span style="color:green;">**OTP**</span> or <span style="color:green;">**Face Authentication**</span> 🧑‍🦰.
# ---   
# <span style="color:red;">**NOTE:**</span> Initially there is no <span style="color:green;">**Face Auth**</span> done during the **"First-Time Login"** 🔑 and the traditional use of <span style="color:green;">**OTP alone**</span> is carried out.
# """, unsafe_allow_html=True)
#   st.write(" ")

# #################################

# box4 = st.container(border=True)
# with box4:
#   st.subheader(":violet[4. 🔄Second Time Login]",divider='violet')
# col411,col421 = box4.columns([1.1,1.2])
# with col421:
#  st.write(" ")
#  st.write(" ")
#  st.write(" ")
#  place = st.empty()
#  st.warning("""
#             **Note:**
#             The transition from the **'Testing phase'** to the **'Production phase'** can be seamlessly managed through our admin panel. We've included features to facilitate this process.
#             """)

# with col411:
#  with st.container(border=True):

#   st.markdown("""
# ### About:

# 1. 🛂 When the user logs in after the **first time**, The application checks for the <span style="color:orange;">**Model**</span> and <span style="color:orange;">**Edge Token**</span>.

# 2. 🔍 If either is missing, the first-time login process is repeated. If both are present, the user is given two options:
#    - <span style="color:green;">**OTP Authentication**</span> 🔑
#    - <span style="color:cyan;">**Face Authentication**</span> 🧑‍🦰

# 3. ✅ **Testing Phase**:
#    - **OTP Authentication**: Grants <span style="color:green;">**full access**</span> to all application features.
#    - **Face Authentication**: The captured photo is sent to the <span style="color:red;">**Model Inference Block**</span> 🖼️. Access is granted with <span style="color:orange;">**restrictions**</span>; sensitive content is not available.

# 4. 🔄 **Production Phase**:
#    - **Face Authentication**: Will provide <span style="color:green;">**full access**</span>, similar to a biometric scan 🛂.
#    - **OTP Authentication**: May offer <span style="color:orange;">**restricted access**</span> as Face Authentication becomes the primary method.
# """, unsafe_allow_html=True)
  
# ###########################################
# box51 = st.container(border=True)
# with box51:
#   st.subheader(":violet[5. 🖥️Model Inferencing [Bi-Model Concurrency]]",divider='violet')
# col15,col25 = box51.columns([1.4,1])
# with col15:
#  st.write(" ")
#  st.write(" ")
#  st.write(" ")
#  st.write(" ")
#  st.write(" ")
#  gog = st.empty()
#  st.markdown("""
# ### Model Combinations & Responses:
# <table style="width:100%">
#   <tr>
#     <td><span style="color:green;"><b>[1,1]</b></span> ✅<br>Authorization Successful!</td>
#     <td><span style="color:red;"><b>[0,1]</b></span> 🛑<br>Spoofing Detected & UUID is Blacklisted Immediately</td>
#   </tr>
#   <tr>
#     <td><span style="color:red;"><b>[1,0]</b></span> 🧑‍🦰<br>Not an Citizen of India (doesn't Have Aadhaar ID)</td>
#     <td><span style="color:red;"><b>[0,0]</b></span> 🖥<br>Very Poor hacking Attempt</td>
#   </tr>
# </table>
# """, unsafe_allow_html=True)
# with col25:
#  with st.container(border=True):
#   st.markdown("""
# ### About:

# 1. 📸 When <span style="color:green;">**Face Authentication**</span> is initiated, the user's <span style="color:orange;">**photo**</span> is captured and verified to ensure there is a face detected.

# 2. 🔄 Simultaneously, two processes begin:
#    - The photo is processed by the <span style="color:red;">**Edge Model Block**</span> (<span style="color:purple;">Liveliness Model</span>) for <span style="color:cyan;">**spoof detection**</span>.
#    - The photo is sent to the <span style="color:green;">**Cloud Model Block**</span> (<span style="color:orange;">Face Embedding Model</span>) for <span style="color:blue;">**vector comparison**</span> with the citizen database.

# 3. 🔐 Both models generate outputs:
#    - <span style="color:cyan;">**0 or 1**</span> from the <span style="color:red;">Edge Model Block</span> (<span style="color:purple;">liveliness detection</span>).
#    - <span style="color:cyan;">**0 or 1**</span> from the <span style="color:green;">Cloud Model Block</span> (<span style="color:orange;">identity verification</span>).

# 4. ✅ <span style="color:green;">**Access level**</span>:
#    - <span style="color:orange;">**Testing Phase**</span>: Access is granted, but with <span style="color:yellow;">**restrictions**</span> on sensitive content.
#    - <span style="color:blue;">**Production Phase**</span>: Full access is granted, similar to <span style="color:purple;">**biometric authentication**</span>.

# 5. 🛑 If any combination other than <span style="color:cyan;">[1,1]</span> is produced, <span style="color:red;">**access is denied**</span>, and further actions (e.g., <span style="color:gray;">**blacklisting**</span>) may occur based on the output.
# """, unsafe_allow_html=True)
  
# ###########################

# box24 = st.container(border=True)
# with box24:
#   st.subheader(":violet[5.1 Edge Model Block (Liveliness Detection)]",divider='violet')
# col4311,col4321 = box24.columns([1,1.4])
# with col4321:
#  st.write(" ")
#  st.image("edge.gif",use_column_width=True,caption="Edge Model Block")
#  with st.container(border=True):
#   st.markdown("""
# ### Client-side:
# 4.  The <span style="color:blue;">**Encryption Key**</span> is used to perform <span style="color:green;">**homomorphic inference**</span> on the photo (i.e., the data remains encrypted while processing).
              
# 5.  The output of the model is an <span style="color:purple;">**Encrypted Result**</span> (either 0 or 1 for liveliness).

# 6. 🌐 This <span style="color:purple;">**Encrypted Output**</span> is sent back to the cloud server, along with the **UUID**, for further processing by the <span style="color:green;">**Cloud Model Block**</span>.""",unsafe_allow_html=True)

# with col4311:
#    with st.container(border=True):
#     st.write(" ")
#     st.write(" ")
#     st.markdown("""
# ### Backend Process:

# 1. 📸 When <span style="color:green;">**Face Authentication**</span> starts, the user's face is verified to check if a face is detected.

# 2. 🔄 An <span style="color:cyan;">**API request**</span> is sent to the server, sending the following values:
#    - **UUID**: Identifies the physical device.
#    - **Edge Token** (stored in the browser as a cookie): Ensures the same device and location.
#    - <span style="color:orange;">**Hash Key-M**</span>: Verifies the integrity of the encrypted model.
#    - <span style="color:orange;">**Hash Key-U**</span>: Verifies the integrity of the UUID.

# 3. 🔐 The server checks these values against the database:
#    - If any mismatch occurs, the **UUID** is <span style="color:red;">flagged</span> and <span style="color:gray;">**blacklisted**</span> 🔒.
#    - If all match, the server sends back the <span style="color:blue;">**Encryption Key**</span> (but **not** the decryption key).
# """, unsafe_allow_html=True)
#    st.warning("**Note:** The **'Cloud Model Block'** also simultaneously processes the input data (photo) from the application.")

# #############################

# box511 = st.container(border=True)
# with box511:
#   st.subheader(":violet[5.2 Cloud Model Block (Face Embedding Verification)]",divider='violet')
# col115,col125 = box511.columns([1.2,1.1])
# with col115:
#  st.write(" ")
#  st.write(" ")
#  st.write(" ")
#  st.write(" ")
#  st.write(" ")
#  st.image("cloud.gif",use_column_width=True,caption='Cloud Model Block')
#  st.warning("**Note:** This Server is Hosted in a Very Secured Environment where only the Admin Can Access everything")
# with col125:
#  with st.container(border=True):
#   st.markdown("""
# ### About:
# 1. 🔄 **Parallel Processing**: The user's photo is sent to:
#    - <span style="color:orange;">**Edge Model Block**</span> for liveliness detection.
#    - <span style="color:green;">**Cloud Model Block**</span> for face embedding and verification.

# 2. 📸 The **photo** arrives at the cloud server, where the <span style="color:green;">**Face Embedding Model**</span> processes it to generate a <span style="color:cyan;">**128-dimension vector embedding**</span>.

# 3. 🗄️ The embedding is compared with the <span style="color:blue;">**Citizen Vector Database**</span>:
#    - Atleast a <span style="color:yellow;">**98% match**</span> results in a <span style="color:green;">**1 (match)**</span> less that that is labelled as <span style="color:red;">**0 (no match)**</span>.

# 4. 🔐 Concurrently, the **Edge Model’s encrypted output** is sent to the cloud:
#    - The **UUID** retrieves the <span style="color:blue;">**Decryption Key**</span>, decrypting the output to <span style="color:green;">get **1 (valid)**</span> or <span style="color:red;">**0 (invalid)**</span>.

# 5. 🛠️ **Final Decision**:
#    - Combine outputs from both models <span style="color:green;">**[1,1]**</span> which grants access to the Website any other combination results in denial and possible <span style="color:gray;">**blacklisting**</span>.
# """, unsafe_allow_html=True)

# ####################


# box24 = st.container(border=True)
# with box24:
#   st.subheader(":violet[6. Admin Privileges]",divider='violet')
# col4311,col4321 = box24.columns([1.2,1])
# with col4321:
#  st.write(" ")
#  st.write(" ")
#  st.write(" ")
#  st.write(" ")
#  st.image("m.gif",use_column_width=True,caption='Admin Panel Features')

# with col4311:
#    with st.container(border=True):

#     st.markdown("""
# ### About:

# #### These are the features of the 🛠️**Admin Panel**:

# 1. 🔄 **Switching Environments**: Effortlessly toggle between <span style="color:orange;">**Testing**</span> and <span style="color:green;">**Production**</span> setups.

# 2. 👤 **Resident Privileges**: Tailor resident access rights based on authentication methods for both <span style="color:orange;">**Testing**</span> and <span style="color:green;">**Production**</span> phases.

# 3. 🖥️ **MDN Management**: Handle new edge servers and adjust the origin server with ease.

# 4. 📊 **Analytics Snapshot**: Monitor <span style="color:cyan;">**CDN counts**</span>, <span style="color:red;">**blacklisted entries**</span>, and <span style="color:grey;">**greylisted items**</span>.

# 5. ⚙️ **Adversarial Data Handling**: Implement <span style="color:yellow;">**MLOps strategies**</span> to manage and mitigate adversarial data.

# 6. 🔄 **Model Update Agent**: Seamlessly deploy model updates with our <span style="color:green;">**automated update system**</span>.
# """, unsafe_allow_html=True)

# st.divider()
# st.markdown("""
#     <style>
#     .claim {
#         text-align: center;
#         font-size: 20px; /* Larger font size for emphasis */
#         color: #FF5722; /* Bold orange color for impact */
#         font-weight: bold;
#         margin: 30px 0;
#         border-top: 3px solid #FF5722; /* Thicker border for emphasis */
#         padding-top: 15px;
#         background-color: #212121; /* Dark background for contrast */
#         padding: 20px;
#         border-radius: 10px; /* Rounded corners for a modern look */
#     }
#     .warning {
#         color: #F44336; /* Red color for a warning */
#         font-weight: bold;
#         font-size: 18px; /* Slightly larger text */
#     }
#     .alert {
#         color: #FFEB3B; /* Bright yellow for high visibility */
#         font-weight: bold;
#         font-size: 16px; /* Emphasize key points */
#     }
#     </style>
#     <div class="claim">
#         ⚠️ ATTENTION: ALL RIGHTS RESERVED @The Horizon ⚠️<br>
#         <span class="warning">Any unauthorized use, duplication, or distribution of this content will be met with severe legal action. </span><br>
#         <span class="alert">Violators will face heavy charges and legal repercussions. We strictly protect our intellectual property. Proceed with caution!</span>
#     </div>
# """, unsafe_allow_html=True)
# while True:
#   place.image("Login2T.gif",caption="Testing Phase")
#   gog.image(r"block-t.gif",use_column_width=True,caption="Testing Phase")
#   time.sleep(3)
#   place.image("Login2T1.gif",caption="Production Phase")
#   gog.image(r"block-p.gif",use_column_width=True,caption="Production Phase")
#   time.sleep(3)
import streamlit as st
import pandas as pd
import time

# st.markdown("""
#     <h1 style="text-align: center; text-decoration: underline;">💡Smart India Hackathon💡</h1>
# """, unsafe_allow_html=True)

#st.header("Architecture & Workflows",divider='orange')
st.set_page_config(layout="wide", page_title="Smart India Hackathon Architecture", page_icon="🏛️")
st.markdown("""
    <h1 style="text-align: center; text-decoration: underline;">🏛️Smart India Hackathon: Architecture & Workflows🏛️</h1>
""", unsafe_allow_html=True)

@st.dialog("Note from 'The Horizon'",width='large')
def poping():
    st.markdown("""
        <style>
        .header {
            text-align: center;
            font-size: 3em; /* Larger header */
            color: #FF5722; /* Vibrant orange */
            font-weight: bold;
            padding: 20px 0;
            border-bottom: 4px solid #FF5722;
        }
        .intro {
            text-align: center;
            font-size: 22px; /* Larger font size */
            color: #E0E0E0; /* Light gray */
            margin: 40px 0;
            line-height: 1.8;
        }
        .highlight {
            color: #FF9800; /* Highlight color */
            font-weight: bold;
        }
        .highlight1 {
            color: #00BCD4; /* Highlight color */
            font-weight: bold;
        }
        .emphasis {
            color: #4CAF50; /* Green for emphasis */
            font-weight: bold;
        }
        .emoji {
            font-size: 1.7em; /* Larger emojis */
        }
        .call-to-action {
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            color: #FF5722; /* Call to action color */
            padding: 15px;
            border-radius: 10px;
            background-color: #FFE0B2; /* Light background */
        }
        </style>
        <div class="header">🌟 Welcome! 🎉</div>
        <div class="intro">
            <p class="emoji">👋 Hello Judges!</p>
            <p>First of all, <span class="highlight">thank you for clicking this link</span>! If you're here, it means we've successfully piqued your interest with our approach. Curious about the details of our solution? <span class="emphasis">No worries!</span></p>
            <p>This page has been designed by <span class="highlight">"The Horizon"</span> from <span class="highlight1">Chennai Institute of Technology</span> to provide you with an even clearer insight into our work. <span class="emphasis">Let's dive in and enjoy the journey! 🚀</span></p>
        </div>
    """, unsafe_allow_html=True)
    
poping()
# def About_section():
#     st.markdown("""
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
#     .stApp {
#         background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
#         background-size: 400% 400%;
#         animation: gradient 15s ease infinite;
#     }
#     [data-testid="stAppViewContainer"] > .main {
#         background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
#         background-size: 400% 400%;
#         animation: gradient 15s ease infinite;
#     }
#     .stToolbar {
#         background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
#         background-size: 400% 400%;
#         animation: gradient 15s ease infinite;
#     }
#     .stAppViewContainer {
#         background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
#         background-size: 400% 400%;
#         animation: gradient 15s ease infinite;
#     }          
#     @keyframes gradient {
#         0% {background-position: 0% 50%;}
#         50% {background-position: 100% 50%;}
#         100% {background-position: 0% 50%;}
#     }
#     .card {
#         background: rgba(255, 255, 255, 0.1);
#         backdrop-filter: blur(10px);
#         border-radius: 20px;
#         padding: 20px;
#         margin: 10px;
#         box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
#         border: 1px solid rgba(255, 255, 255, 0.18);
#         transition: all 0.3s ease;
#     }
#     .card:hover {
#         transform: translateY(-10px);
#         box-shadow: 0 12px 48px 0 rgba(31, 38, 135, 0.5);
#     }
#     .title {
#         font-family: 'Poppins', sans-serif;
#         font-size: 3rem !important;
#         font-weight: 700;
#         color: #ffffff;
#         text-align: center;
#         margin-bottom: 30px;
#         text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
#     }
#     .subtitle {
#         font-family: 'Poppins', sans-serif;
#         font-size: 1.8rem !important;
#         font-weight: 600;
#         color: #ffff00;
#         margin-bottom: 20px;
#     }
#     .content {
#         font-family: 'Poppins', sans-serif;
#         font-size: 1rem;
#         color: #ffffff;
#         line-height: 1.6;
#     }
#     .team-member {
#         font-family: 'Poppins', sans-serif;
#         font-size: 1.2rem;
#         color: #ffffff;
#         margin-bottom: 10px;
#         opacity: 0;
#         transform: translateX(50px);
#         animation: slideIn 0.5s forwards;
#     }
#     @keyframes slideIn {
#         to {
#             opacity: 1;
#             transform: translateX(0);
#         }
#     }
#     .highlight {
#         color: #00ffff;
#         font-weight: bold;
#     }
#     </style>
#     """, unsafe_allow_html=True)

#     st.markdown('<h1 class="title">🚀 The Horizon: Crazy Gang from CIT 🚀</h1>', unsafe_allow_html=True)

#     col1, col2 = st.columns(2)

#     with col1:
#         st.markdown(
#             """
#             <div class="card">
#                 <h1 class="subtitle">🌟 Introduction</h1>
#                 <p class="content">
#                     Welcome to our project! We are <span class="highlight">"The Horizon"</span>, a dynamic group from 
#                     <span class="highlight">CIT (Chennai Institute of Technology)</span>. We’ve taken on the 
#                     challenge presented in Problem Statement <span class="highlight">SIH1670</span>, aiming to develop a 
#                     robust solution that integrates the security of the ML model published by the 
#                     <span class="highlight">Ministry of Electronics and Information Technology</span>, within the 
#                     domain of <span class="highlight">Smart Automation</span>.
#                     This page is designed to guide you through our solution, with each component explained clearly 
#                     to facilitate your understanding. Buckle up and let’s dive into the details!
#                 </p>
#             </div>
#             """,
#             unsafe_allow_html=True
#         )

#     with col2:
#         st.markdown(
#             """
#             <div class="card">
#                 <h1 class="subtitle">🌈 Our Awesome Team</h1>
#                 <h5>1. Prithvi Ragavendiran R (3rd Year EEE)</h5>
#                 <h5>2. Surya Prabhakaran V P (3rd year CSE)</h5>
#                 <h5>3. Rudhresh (3rd Year EEE)</h5>
#                 <h5>4. Nishanth (2nd Year EEE)</h5>
#                 <h5>5. Lokesh (4th Year CSE)</h5>
#             </div>
#             """,
#             unsafe_allow_html=True
#         )

#     # Add some animated elements
#     st.markdown(
#         """
#         <script>
#         function createParticle() {
#             const particle = document.createElement('div');
#             particle.style.position = 'fixed';
#             particle.style.width = '10px';
#             particle.style.height = '10px';
#             particle.style.background = '#ffffff';
#             particle.style.borderRadius = '50%';
#             particle.style.pointerEvents = 'none';
#             particle.style.left = Math.random() * window.innerWidth + 'px';
#             particle.style.top = window.innerHeight + 'px';
#             particle.style.animation = `rise ${Math.random() * 3 + 2}s linear`;
#             document.body.appendChild(particle);
#             setTimeout(() => particle.remove(), 5000);
#         }

#         setInterval(createParticle, 200);

#         const style = document.createElement('style');
#         style.textContent = `
#             @keyframes rise {
#                 to {
#                     transform: translateY(-100vh) rotate(360deg);
#                     opacity: 0;
#                 }
#             }
#         `;
#         document.head.appendChild(style);
#         </script>
#         """,
#         unsafe_allow_html=True
#     )

# # Call this function where you want to display the About section in your Streamlit app
# About_section()
box = st.container(border=True)

with box:
  st.subheader(":violet[1. 🖥️Liveness Model (at EDGE From MDN)]",divider='violet')
col1,col2 = box.columns([1.3,1.2])
with col1:
 st.write(" ")
 st.write(" ")
 st.write(" ")
 st.write(" ")
 st.write(" ")
 st.write(" ")
 st.write(" ")
 st.image(r"Model Arch1.gif",use_column_width=True,caption="Liveness Model @EDGE")
with col2:
 with st.container(border=True):
  st.markdown("""
### About:
1. 🌐 <span style="color:blue;">**The Quantized Liveness Model**</span> 🎯 for spoof detection is distributed from a **Central Origin Server** 🚀 to all EDGE Servers in the Model Delivery Network (**MDN**) across India.

2. 🔒 Upon :green-background[**Successful OTP Authentication**] on the UIDAI website, ✅ the model is securely sent from the nearest EDGE Server in the MDN 📡 to the Client-side device, accompanied by a <span style="color:yellow;">**Unique EDGE token**</span> 🔑.

3. 🔐 Before transmission, the model is <span style="color:orange;">**Encrypted**</span> 🛡️ using a :gray[Unique Encryption key] 🔏 to prevent Reverse Engineering attempts by Client-side hackers 👾.

4. 🖥️ The **Encrypted model** is deployed at the EDGE 💾 in a secure <span style="color:red;">**.EMSF format**</span> 🗝️ ensuring Safety and Security of the EDGE Model, contributing to reliable Inference.
""", unsafe_allow_html=True)
  st.write(" ")
# with box:
#  with st.container(border=True):
#   st.markdown("""<span style='font-size: 3em;'>:red[Outcome: ]</span>  <span style='font-size: 2em;'>"Liveness Model" is deployed @EDGE</span>""",unsafe_allow_html=True)
  
###################################

box1 = st.container(border=True)
with box1:
  st.subheader(":violet[2. 🧑‍🤝‍🧑Face Embedding Model (at Cloud Connected to a Vector Database)]",divider='violet')
col11,col21 = box1.columns([1.26,1.2])
with col21:
 st.write(" ")
 st.write(" ")
 st.write(" ")
 st.write(" ")
 st.write(" ")
 st.image("Model Arch11.gif",use_column_width=True,caption="Face-Embedding Model @Cloud")
with col11:
 with st.container(border=True):
  
  st.markdown("""
### About:

1. 🌐 The <span style="color:cyan;">**Face Embedding Model**</span> 🧑‍🤝‍🧑 is deployed in a <span style="color:blue;">**Secure Cloud environment**</span> ☁️ alongside the <span style="color:blue;">**Central Vector database**</span> 🗃️ to ensure robust security and privacy.

2. 🧩 The model generates a <span style="color:green;">**128-dimension Vector embedding**</span> 📏 for each user's face, representing its unique features.

3. 🔍 This Vector embedding is compared with the embeddings stored in the central vector database, ensuring a resemblance of at least <span style="color:orange;">**98%**</span>.

4. ✅ If the generated Vector embedding matches the database entry and both the **Quantized Liveness Model** and the **Face Embedding Model** approve, the user is successfully <span style="color:green;">**Authenticated**</span>.
""", unsafe_allow_html=True)
  
#############

box2 = st.container(border=True)
with box2:
  st.subheader(":violet[3. 🛂Citizen Login (First-Time Login)]",divider='violet')
col13,col23 = box2.columns([1.4,1])
with col13:
 st.write(" ")
 st.write(" ")
 st.write(" ")
 ds1,ds2 = st.columns([0.85,0.3])
 with ds1:
  st.write(" ")
  st.write(" ")
  st.image("Login1.gif",use_column_width=True,caption="First Time Login")
 with ds2:
  data = pd.read_csv("random_keys.csv")
  st.write("**Database:**")
  def style_dataframe(styler):
    styler.set_properties(**{
        'background-color': 'white',
        'color': 'black',
        'border': '1px solid black',
        'text-align': 'left'
    })
    styler.hide(axis="index")
    return styler

# Apply styles
  styled_df = data.style.pipe(style_dataframe)
  st.dataframe(styled_df,height=200,hide_index=True)
 st.write(" ")
#  st.write(" ")
 st.markdown("""
### The Following Values Get Added to the Database:
<table style="width:100%">
  <tr>
    <td><span style="color:blue;"><b>UUID</b></span> 🆔<br>Unique User IDentification Number</td>
    <td><span style="color:green;"><b>EDGE Token</b></span> 🔑<br>Identifier for the model sent</td>
  </tr>
  <tr>
    <td><span style="color:red;"><b>Encryption Key</b></span> 🔒<br>Used for securing the model</td>
    <td><span style="color:red;"><b>Decryption Key</b></span> 🔓<br>Used for decrypting the model</td>
  </tr>
  <tr>
    <td><span style="color:orange;"><b>Hash Key-M</b></span> 🧬<br>Hash of the model for integrity</td>
    <td><span style="color:orange;"><b>Hask Key-U</b></span> 🔢<br>Hash of the UUID for integrity</td>
  </tr>
</table>
""", unsafe_allow_html=True)

with col23:
 with st.container(border=True):
  st.write(" ")
  st.markdown("""
### About:
1. 🚪 When a User (Resident) logs in for the **First time**, they are required to take the traditional <span style="color:green;">**OTP Authentication**</span> 🔑 route since they haven't **Initialized FaceAuth** yet, so NO <span style="color:orange;">**EDGE Model**</span> or <span style="color:orange;">**EDGE Token**</span> stored on their device.

2. 📲 Upon successful OTP authentication ✅, You can Initialize FaceAuth <span style="color:cyan;">by agreeing for</span> 🍪. If the user accepts, a request is sent to the **MDN** 🌐.

3. 🔒 Before the <span style="color:red;">**Quantized Liveness Model**</span> is sent to the client from the MDN, it is encrypted using a unique Encryption key 🔏. Along with the encrypted model, an <span style="color:green;">**EDGE Token**</span> is also delivered 📡.

4. 🖥️ While making the request, a unique <span style="color:blue;">**UUID key**</span> 🌐 is generated for the Client Device. In the database, a new entry for the model sent is added.

5. 📂 Once this process is complete, the model is finally deployed at the <span style="color:orange;">**EDGE**</span> 💾. The next time the user logs in, they will have the option to authenticate using either <span style="color:green;">**OTP**</span> or <span style="color:green;">**Face Authentication**</span> 🧑‍🦰.
---   
<span style="color:red;">**NOTE:**</span> Initially there is no <span style="color:green;">**Face Auth**</span> done during the **"First-Time Login"** 🔑 and the traditional use of <span style="color:green;">**OTP**</span> alone is carried out.
""", unsafe_allow_html=True)
  st.write(" ")

#################################

box4 = st.container(border=True)
with box4:
  st.subheader(":violet[4. 🔄Eventual Login]",divider='violet')
col411,col421 = box4.columns([1.1,1.2])
with col421:
 st.write(" ")
 st.write(" ")
 st.write(" ")
 place = st.empty()

 with place.container(border=True):
    _, _col1, _col2, ___, _col3, __ = st.columns([1, 0.45, 0.2, 0.15, 0.57, 0.9])
    # _col1.write("")
    _col1.write('**Testing Phase**')
    # _col3.write("")
    _col3.write('**Production Phase**')

    place_toggle = _col2.toggle(' ', False)

    if place_toggle:
      st.image(r'Login2T1.gif', use_column_width=True, caption='Production Phase')
    else:
      st.image(r'Login2T.gif', use_column_width=True, caption='Testing Phase')


 st.warning("""
            **Note:**
            The transition from the **'Testing phase'** to the **'Production phase'** can be seamlessly managed through our admin panel. We've included features to facilitate this process.
            """)

with col411:
 with st.container(border=True):
  st.write(" ")

  st.markdown("""
### About:

1. 🛂 When the user logs in after the **first time**, The application checks for the <span style="color:orange;">**Model**</span> and <span style="color:orange;">**EDGE Token**</span>.

2. 🔍 If either is missing, the first-time login process is repeated. If both are present, the user is given two options:
   - <span style="color:green;">**OTP Authentication**</span> 🔑
   - <span style="color:cyan;">**Face Authentication**</span> 🧑‍🦰

3. ✅ **Testing Phase**:
   - **OTP Authentication**: Grants <span style="color:green;">**full access**</span> to all application features.
   - **Face Authentication**: The captured photo is sent to the <span style="color:red;">**Model Inference Block**</span> 🖼️and Access is granted with <span style="color:orange;">**Restrictions**</span>  & sensitive content is not available due to the risk adversarial bypasses.

4. 🔄 **Production Phase**:
   - **Face Authentication**: Will provide <span style="color:green;">**full access**</span>, similar to a biometric scan 🛂.
   - **OTP Authentication**: May offer <span style="color:orange;">**Restricted access**</span> as Face Authentication becomes the primary method.
""", unsafe_allow_html=True)
  st.write(" ")
  
###########################################
box51 = st.container(border=True)
with box51:
  st.subheader(":violet[5. 🖥️ Concurrent Bi-Model Inference]",divider='violet')
col15,col25 = box51.columns([1.4,1])
with col15:
 gog = st.empty()


 with gog.container(border=True):
    _, _col1, _col2, ___, _col3, __ = st.columns([1, 0.4, 0.15, 0.12, 0.45, 0.9])
    # _col1.write("")
    _col1.write('**Testing Phase**')
    # _col3.write("")
    _col3.write('**Production Phase**')

    gog_toggle = _col2.toggle('  ', False)

    if gog_toggle:
      st.image(r'block-p.gif', use_column_width=True, caption='Production Phase')
    else:
      st.image(r'block-t.gif', use_column_width=True, caption='Testing Phase')


 st.markdown("""
### Model Combinations & Responses:
<table style="width:100%">
  <tr>
    <td><span style="color:green;"><b>[1,1]</b></span> ✅<br>Authorization Successful!</td>
    <td><span style="color:red;"><b>[0,1]</b></span> 🛑<br>Spoofing Detected & UUID is Blacklisted Immediately</td>
  </tr>
  <tr>
    <td><span style="color:red;"><b>[1,0]</b></span> 🧑‍🦰<br>Not an Citizen of India (doesn't Have Aadhaar ID)</td>
    <td><span style="color:red;"><b>[0,0]</b></span> 🖥<br>Very Poor hacking Attempt</td>
  </tr>
</table>
""", unsafe_allow_html=True)
with col25:
 with st.container(border=True):

  st.markdown("""
### About:

1. 📸 When <span style="color:green;">**Face Authentication**</span> is initiated, the user's <span style="color:orange;">**photo**</span> is captured and verified to ensure there is a face detected.

2. 🔄 Simultaneously, two processes begin:
   - The photo is processed by the <span style="color:red;">**EDGE Model Block**</span> (<span style="color:purple;">Liveness Model</span>) for <span style="color:cyan;">**spoof detection**</span>.
   - The photo is sent to the <span style="color:green;">**Cloud Model Block**</span> (<span style="color:orange;">Face Embedding Model</span>) for <span style="color:blue;">**vector comparison**</span> with the **Citizen Vector Database**.

3. 🔐 Both models generate outputs:
   - <span style="color:cyan;">**0 or 1**</span> from the <span style="color:red;">EDGE Model Block</span> (<span style="color:purple;">Liveness detection</span>).
   - <span style="color:cyan;">**0 or 1**</span> from the <span style="color:green;">Cloud Model Block</span> (<span style="color:orange;">identity verification</span>).

4. ✅ <span style="color:green;">**Access level**</span>:
   - <span style="color:orange;">**Testing Phase**</span>: Access is granted, but with <span style="color:yellow;">**restrictions**</span> on sensitive content.
   - <span style="color:blue;">**Production Phase**</span>: Full access is granted, similar to <span style="color:purple;">**biometric authentication**</span>.

5. 🛑 If any combination other than <span style="color:cyan;">[1,1]</span> is produced, <span style="color:red;">**access is denied**</span>, and further actions (e.g., <span style="color:gray;">**blacklisting**</span>) may occur based on the output.
""", unsafe_allow_html=True)
  # st.write(" ")
  # st.write(" ")
  # st.write(" ")
  # st.write(" ")

  
###########################

box24 = st.container(border=True)
with box24:
  st.subheader(":violet[5.1 EDGE Model Block (Liveness Detection)]",divider='violet')
col4311,col4321 = box24.columns([1,1.4])
with col4321:
 st.write(" ")
 st.image("edge.gif",use_column_width=True,caption="Edge Model Block")
 with st.container(border=True):
  st.markdown("""
### Client-side:
4.  The <span style="color:blue;">**Encryption Key**</span> is used to perform <span style="color:green;">**homomorphic inference**</span> on the photo (i.e., the data remains encrypted while processing).
              
5.  The output of the model is an <span style="color:purple;">**Encrypted Result**</span> (either 0 or 1 for Liveness).

6. 🌐 This <span style="color:purple;">**Encrypted Output**</span> is sent back to the cloud server, along with the **UUID**, for further processing by the <span style="color:green;">**Cloud Model Block**</span>.""",unsafe_allow_html=True)

with col4311:
   with st.container(border=True):
    st.write(" ")
    st.write(" ")
    st.markdown("""
### Backend Process:

1. 📸 When <span style="color:green;">**Face Authentication**</span> starts, the user's face is verified to check if a face is detected.

2. 🔄 An <span style="color:cyan;">**API request**</span> is sent to the server, sending the following values:
   - **UUID**: Identifies the physical device.
   - **Edge Token** (stored in the browser as a cookie): Ensures the same device and location.
   - <span style="color:orange;">**Hash Key-M**</span>: Verifies the integrity of the encrypted model.
   - <span style="color:orange;">**Hash Key-U**</span>: Verifies the integrity of the UUID.

3. 🔐 The server checks these values against the database:
   - If any mismatch occurs, the **UUID** is <span style="color:red;">flagged</span> and <span style="color:gray;">**blacklisted**</span> 🔒.
   - If all match, the server sends back the <span style="color:blue;">**Encryption Key**</span> (but **not** the decryption key).
""", unsafe_allow_html=True)
   st.warning("**Note:** The **'Cloud Model Block'** also simultaneously processes the input data (photo) from the application.")

#############################

box511 = st.container(border=True)
with box511:
  st.subheader(":violet[5.2 Cloud Model Block (Face Embedding Verification)]",divider='violet')
col115,col125 = box511.columns([1.2,1.1])
with col115:
 st.write(" ")
 st.write(" ")
 st.write(" ")
 st.write(" ")
 st.write(" ")
 st.image("cloud.gif",use_column_width=True,caption='Cloud Model Block')
 st.warning("**Note:** This Server is Hosted in a Very Secured Environment where only the Admin Can Access everything")
with col125:
 with st.container(border=True):
  st.markdown("""
### About:
1. 🔄 **Parallel Processing**: The user's photo is sent to:
   - <span style="color:orange;">**Edge Model Block**</span> for Liveness detection.
   - <span style="color:green;">**Cloud Model Block**</span> for face embedding and verification.

2. 📸 The **photo** arrives at the cloud server, where the <span style="color:green;">**Face Embedding Model**</span> processes it to generate a <span style="color:cyan;">**128-dimension vector embedding**</span>.

3. 🗄️ The embedding is compared with the <span style="color:blue;">**Citizen Vector Database**</span>:
   - Atleast a <span style="color:yellow;">**98% match**</span> results in a <span style="color:green;">**1 (match)**</span> less that that is labelled as <span style="color:red;">**0 (no match)**</span>.

4. 🔐 Concurrently, the **Edge Model’s encrypted output** is sent to the cloud:
   - The **UUID** retrieves the <span style="color:blue;">**Decryption Key**</span>, decrypting the output to <span style="color:green;">get **1 (valid)**</span> or <span style="color:red;">**0 (invalid)**</span>.

5. 🛠️ **Final Decision**:
   - Combine outputs from both models <span style="color:green;">**[1,1]**</span> which grants access to the Website any other combination results in denial and possible <span style="color:gray;">**blacklisting**</span>.
""", unsafe_allow_html=True)

####################


box24 = st.container(border=True)
with box24:
  st.subheader(":violet[6. Admin Privileges]",divider='violet')
col4311,col4321 = box24.columns([1.2,1])
with col4321:
 st.write(" ")
 st.write(" ")
 st.write(" ")
 st.write(" ")
 st.image("m.gif",use_column_width=True,caption='Admin Panel Features')

with col4311:
   with st.container(border=True):

    st.markdown("""
### About:

#### These are the features of the 🛠️**Admin Panel**:

1. 🔄 **Switching Environments**: Effortlessly toggle between <span style="color:orange;">**Testing**</span> and <span style="color:green;">**Production**</span> setups.

2. 👤 **Resident Privileges**: Tailor resident access rights based on authentication methods for both <span style="color:orange;">**Testing**</span> and <span style="color:green;">**Production**</span> phases.

3. 🖥️ **MDN Management**: Handle new edge servers and adjust the origin server with ease.

4. 📊 **Analytics Snapshot**: Monitor <span style="color:cyan;">**MDN counts**</span>, <span style="color:red;">**blacklisted entries**</span> and <span style="color:grey;">**EDGE Servers**</span>.

5. ⚙️ **Adversarial Data Handling**: Implement <span style="color:yellow;">**MLOps strategies**</span> to manage and mitigate adversarial data.

6. 🔄 **Model Update Agent**: The Model Update Agent Follows a <span style="color:green;">**LCPD Approach**</span> (Latest Commit Pulled Deployment).
""", unsafe_allow_html=True)

st.divider()
st.markdown("""
    <style>
    .claim {
        text-align: center;
        font-size: 20px; /* Larger font size for emphasis */
        color: #FF5722; /* Bold orange color for impact */
        font-weight: bold;
        margin: 30px 0;
        border-top: 3px solid #FF5722; /* Thicker border for emphasis */
        padding-top: 15px;
        background-color: #212121; /* Dark background for contrast */
        padding: 20px;
        border-radius: 10px; /* Rounded corners for a modern look */
    }
    .warning {
        color: #F44336; /* Red color for a warning */
        font-weight: bold;
        font-size: 18px; /* Slightly larger text */
    }
    .alert {
        color: #FFEB3B; /* Bright yellow for high visibility */
        font-weight: bold;
        font-size: 16px; /* Emphasize key points */
    }
    </style>
    <div class="claim">
        ⚠️ ATTENTION: ALL RIGHTS RESERVED @The Horizon ⚠️<br>
        <span class="warning">Any unauthorized use, duplication, or distribution of this content will be met with severe legal action. </span><br>
        <span class="alert">Violators will face heavy charges and legal repercussions. We strictly protect our intellectual property. Proceed with caution!</span>
    </div>
""", unsafe_allow_html=True)
# `while True:
#   gog.image(r".\block-t.gif",use_column_width=True,caption="Testing Phase")
#   time.sleep(3)
#   gog.image(r".\block-p.gif",use_column_width=True,caption="Production Phase")
#   time.sleep(3)`

# row1 = st.columns(30)
# for col in row1:
#     tile = col.container()
#     tile.title("::")

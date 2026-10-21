import streamlit as st
from google import genai

# 1. पेज कॉन्फ़िगरेशन
st.set_page_config(page_title="AI Tutor Smarty Madam", page_icon="👩‍🏫", layout="centered")

# 2. Gemini क्लाइंट सेटअप (अपनी Gemini API Key यहाँ डालें)
client = genai.Client(api_key="AQ.Ab8RN6L-430WAjUt0-zThIus0720RpnE7P3OpR_AV7v01eOTyg")

st.title("👩‍🏫 AI Tutor Smarty Madam")
st.write("दूसरी कक्षा के बच्चों के लिए AI-संचालित स्मार्ट ट्यूटर!")

# 3. चैट हिस्ट्री
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. यूजर इनपुट और सही मॉडल कॉल
if prompt := st.chat_input("यहाँ अपना सवाल लिखें..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            system_instruction = (
                "Role & Behavior: You are 'Smarty Madam', an affectionate, loving, "
                "and disciplined female tutor for young school children (Class 1st to 5th). "
                "हमेशा बहुत सरल, छोटी और बच्चों को समझ आने वाली हिंदी में जवाब दें।"
            )
            
            full_prompt = f"{system_instruction}\n\nसवाल: {prompt}"
            
            # वही मॉडल जो आपके AI Studio में सेलेक्टेड है
            response = client.models.generate_content(
                model='gemini-3.5-flash-lite',
                contents=full_prompt,
            )
            
            ai_response = response.text
            st.markdown(ai_response)
            st.session_state.messages.append({"role": "assistant", "content": ai_response})
            
        except Exception as e:
            st.error(f"कुछ तकनीकी दिक्कत आई है: {e}")
import streamlit as st
import requests
import time

# Configuration
API_URL = "https://yamraj047-api-nepal-legal-llm-gguf.hf.space/ask"

# Page setup
st.set_page_config(page_title="Nepal Legal Assistant", page_icon="🇳🇵")

# Title
st.title("🇳🇵 Nepal Legal Assistant")
st.caption("Ask questions about Nepal law")

# Question input
question = st.text_area(
    "Enter your question:",
    placeholder="What is the punishment for theft in Nepal?",
    height=100
)

# Submit button
if st.button("Get Answer", type="primary"):
    if question:
        with st.spinner("⏳ Processing... "):
            start_time = time.time()
            
            try:
                # Call API
                response = requests.post(
                    API_URL,
                    json={"question": question},
                    timeout=9000
                )
                
                if response.status_code == 200:
                    result = response.json()
                    elapsed = time.time() - start_time
                    
                    # Display answer
                    st.success(f"✅ Answer received in {elapsed/60:.1f} minutes")
                    st.write("### Answer:")
                    st.write(result['answer'])
                else:
                    st.error(f"Error: {response.status_code}")
                    
            except Exception as e:
                st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter a question")

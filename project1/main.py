<<<<<<< HEAD
import cv2
import numpy as np
import streamlit as st 
from tensorflow.keras.applications.mobilenet_v2 import(
    MobileNetV2,
    preprocess_input,
    decode_predictions
)
from PIL import Image

def load_model():
    model = MobileNetV2(weights = "imagenet")
    return model

def preprocess_image(image):
    img = np.array(image)
    img = cv2.resize(img, (224, 224))
    img = preprocess_input(img)
    img = np.expand_dims(img, axis=0)
    return img

def classify_image(model, image):
    try:
        processed_image = preprocess_image(image)
        predictions = model.predict(processed_image)
        decoded_predictions = decode_predictions(predictions, top=3)[0]
        return decoded_predictions
    except Exception as e:
        st.error(f"Error classifying image:  {str(e)}")
        return None
    
    
def main():
    st.set_page_config(page_title = "AI Image Classifier", page_icon="", layout= "centered")
    st.title("AI Image Classifier")
    st.write("Upload an image and let AI tell you what is in it!")
    
    @st.cache_resource
    def load_cached_model():
        return load_model()
    
    model = load_cached_model()
    uploaded_file = st.file_uploader("Choose an image...", type = ["jpg", "png"])
    
    if uploaded_file is not None:
        image = st.image(
            uploaded_file, caption = "Uploaded Image", use_container_width = True
        ) 
        btn = st.button("Classify Image")
        
        if btn: 
            with st.spinner("Analyzing Image..."):
                image = Image.open(uploaded_file)
                predictions = classify_image(model, image)
                
                if predictions:
                    st.subheader("Predictions")
                    for _, label, score in predictions:
                        st.write(f"**{label}**: {score:.2%}")

if __name__ == "__main__":
    main()            
    
=======
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()

def main():
    model = ChatOpenAI(temperature = 0)
    # temperature cang cao thi do tu nhien cua AI cang lon
    tools = []
    agent_executor = create_react_agent(model, tools)
    
    print("Welcome! I'm your AI assistance. Type 'quit' to exit. ")
    print("You can ask me to perform calculation or chat with me. ")
    
    while True: 
        user_input = input("\nYou: ").strip() 
        
        if user_input == "quit":
            break
        
        print("\nAssistant: ", end="") # code khong muon xuong dong ma muon hien thi tat ca phan tra loi cua AI agent
        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")
        print()
        
if __name__ == "__main__":
    main()

        
        
>>>>>>> 620af4d (Management_project_1)

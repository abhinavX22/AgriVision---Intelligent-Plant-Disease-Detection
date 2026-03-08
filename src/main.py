from taipy.gui import Gui, State
from model_logic import predict_disease

# --- 1. State Variables ---
# These variables automatically update the GUI when changed
image_path = "" 
prediction = "Awaiting image upload..."
confidence = 0.0
remedy_text = ""

# --- 2. Event Handling ---
def on_change(state: State, var_name: str, var_value):
    # This triggers the moment the user selects a file
    if var_name == "content":
        state.image_path = var_value
        
        # Run our ML prediction from model_logic.py
        pred, conf, rem = predict_disease(var_value)
        
        # Update the UI state variables
        state.prediction = f"🔍 Diagnosis: {pred}"
        state.confidence = conf
        state.remedy_text = f"💡 Recommendation: {rem}"

# --- 3. Frontend GUI Design (Taipy Markdown) ---
page_layout = """
<|text-center|
# 🌿 AgriVision: Plant Disease Detector
Upload an image of a plant leaf to identify potential diseases and view remedies.
|>

<br/>

<|layout|columns=1 1|
<|
### 1. Upload Leaf Image
<|{content}|file_selector|extensions=.png,.jpg,.jpeg|>
<br/>
<br/>
<|{image_path}|image|width=350px|>
|>

<|
### 2. Diagnosis Results
<|{prediction}|text|>
<br/>

<|{confidence}|indicator|min=0|max=100|width=25vw|>
*Confidence Score (%)*
<br/>

<|{remedy_text}|text|>
|>
|>
"""

# --- 4. Run the Application ---
if __name__ == "__main__":
    app = Gui(page=page_layout)
    # dark_mode=True enforces a clean, dark-themed aesthetic
    app.run(use_reloader=True, port=5000, title="AgriVision App", dark_mode=True)
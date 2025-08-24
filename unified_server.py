from flask import Flask, request, jsonify, send_from_directory
from PIL import Image
import os


from classify_module import classify_text
from chatbot_module import generate_chat_response
from image_gen_module import generate_image_from_text
from remove_bg_module import remove_background_from_image
from edit_image_module import edit_image_with_prompt

app = Flask(__name__)

STATIC_FOLDER = 'static'
os.makedirs(STATIC_FOLDER, exist_ok=True)



@app.route('/classify', methods=['POST'])
def classify_route():
    prompt = request.json.get('prompt', '')
    result = classify_text(prompt)
    return jsonify(result)

@app.route('/chat', methods=['POST'])
def chat_route():
    prompt = request.json.get('prompt', '')
    if not prompt:
        return jsonify({"error": "Prompt is required."}), 400
    result = generate_chat_response(prompt)
    return jsonify(result)

@app.route('/generate_image', methods=['POST'])
def generate_image_route():
    prompt = request.json.get('prompt', '')
    if not prompt:
        return jsonify({"error": "Prompt is required."}), 400
    filename = generate_image_from_text(prompt, STATIC_FOLDER)
    return jsonify({"image_url": f"/static/{filename}"})

@app.route('/remove_bg', methods=['POST'])
def remove_bg_route():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400
    input_image = Image.open(request.files['image']).convert("RGBA")
    filename = remove_background_from_image(input_image, STATIC_FOLDER)
    return jsonify({"image_url": f"/static/{filename}"})

@app.route('/edit_image', methods=['POST'])
def edit_image_route():
    if 'image' not in request.files or 'prompt' not in request.form:
        return jsonify({"error": "Missing image or prompt"}), 400
    input_image = Image.open(request.files['image']).convert("RGB")
    prompt = request.form['prompt']
    filename = edit_image_with_prompt(input_image, prompt, STATIC_FOLDER)
    return jsonify({"image_url": f"/static/{filename}"})

@app.route('/static/<filename>')
def serve_file(filename):
    return send_from_directory(STATIC_FOLDER, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

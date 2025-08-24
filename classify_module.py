from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
LABELS = [
    "image generation request", "background removal request","remove background from image", "background transparent request",
    "image editing request", "question", "text command", "general conversation",
    "draw conclusion from data", "extract information from text request",
    "remove elements from text", "explain", "mental image or picture"
]

def classify_text(prompt: str):
    if not prompt:
        return {"error": "Prompt is required."}
    result = classifier(prompt, LABELS)
    return {
        "prompt": prompt,
        "category": result['labels'][0],
        "score": result['scores'][0]
    }

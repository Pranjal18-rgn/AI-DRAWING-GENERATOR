from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from diffusers import StableDiffusionPipeline
import torch
import base64
from io import BytesIO

app = FastAPI()
templates = Jinja2Templates(directory="templates")

print("Loading model... Please wait...")

# ✅ CPU Friendly Settings (important)
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float32   # Use float32 for CPU stability
)

pipe = pipe.to("cpu")

# Reduce RAM usage
pipe.enable_attention_slicing()

print("Model loaded successfully!")


# 🔥 Prompt Enhancer (auto makes better prompts)
def enhance_prompt(user_prompt):
    return f"{user_prompt}, highly detailed, realistic, 4k, sharp focus, professional lighting"


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/generate", response_class=HTMLResponse)
def generate(request: Request, prompt: str = Form(...)):
    final_prompt = enhance_prompt(prompt)

    image = pipe(
        final_prompt,
        height=384,   # smaller = faster
        width=384,
        num_inference_steps=20   # lower steps = faster generation
    ).images[0]

    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()

    return templates.TemplateResponse("index.html", {
        "request": request,
        "image": img_str,
        "prompt": prompt
    })

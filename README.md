# 🎨 AI Drawing Generator

An AI-powered web application that generates high-quality images from text prompts using **Stable Diffusion v1.5** and **FastAPI**.

---

## 🚀 Features

- Text-to-image generation using Stable Diffusion
- Automatic prompt enhancement
- CPU-optimized inference settings
- Memory-efficient execution
- Responsive glassmorphism UI
- Real-time image preview & download option

---

## 🛠 Tech Stack

- Python
- FastAPI
- PyTorch
- HuggingFace Diffusers
- Jinja2
- HTML / CSS

---

## 📂 Project Structure
AI-Drawing-Generator/
│
├── app.py
├── templates/
│ └── index.html
├── requirements.txt
└── README.md


---

## ⚙️ Installation & Run Locally

### 1️⃣ Clone Repository

### 🔗 Repository

👉 [AI-DRAWING-GENERATOR](https://github.com/Pranjal18-rgn/AI-DRAWING-GENERATOR)

### 📥 Clone Repository
```bash
git clone https://github.com/Pranjal18-rgn/AI-DRAWING-GENERATOR.git
cd AI-DRAWING-GENERATOR

2️⃣ Create Virtual Environment (Recommended)
# </>Bash
python -m venv venv
#Activate it:

# In Windows:
venv\Scripts\activate

# In Mac/Linux:
source venv/bin/activate
```

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Application
# </>Bash
uvicorn app:app --reload

5️⃣ Open in Browser
http://127.0.0.1:8000


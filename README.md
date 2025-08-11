# 🍋‍🟩 Squeezy – Image Compressor, Resizer & Image-to-PDF Converter/Merger

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)]()
[![Flask](https://img.shields.io/badge/flask-2.x-lightgrey)]()
[![Pillow](https://img.shields.io/badge/pillow-9.x-green)]()
[![License](https://img.shields.io/badge/license-MIT-orange)]()

**Squeezy** is a beginner-friendly **Flask** web app that lets you:
- Compress & resize images
- Convert multiple images into a single PDF
- Do it all instantly in the browser — no storage, no tracking, full privacy 🔏

🌐 **Live Demo:** [squeezy-image-compressor.onrender.com](https://squeezy-image-compressor.onrender.com)

---

## 📸 Features
- 📤 Upload any image (`JPG`, `PNG`, etc.)
- 📏 Resize image by percentage (e.g., 50% of original size)
- 🗜️ Compress image quality (e.g., 60% quality)
- 📄 Convert **multiple images** into a single PDF
- ⚡ Instant processing + auto-download
- 🧹 Files **auto-delete after 5 seconds**
- 📱 Mobile-friendly UI (Bootstrap 5)

---

## 🛠 Tech Stack
| Part        | Tool             |
|-------------|------------------|
| Backend     | Python, Flask    |
| Frontend    | HTML5, Bootstrap |
| Imaging     | Pillow (PIL)     |
| Deployment  | Render           |

Uses **`BytesIO`** for in-memory file handling — no disk storage beyond processing time.

---

## 🚀 How It Works

### 🗜️ Image Compression & Resizing
1. Upload an image
2. Set:
   - Resize (% of original)
   - Compress (% quality)
3. Click **Compress**
4. Instantly download the result

### 📄 Image-to-PDF Conversion
1. Upload **multiple images**
2. Click **Generate PDF**
3. Instantly get your merged `.pdf`

✅ All processing happens in-memory using `BytesIO`  
❌ No files are permanently stored — deleted after **5 seconds**

---

## 🔐 Privacy First
- **No storage:** Files are deleted within **5 seconds** after download
- **No logs:** No tracking or saving any metadata
- Just clean, fast, private processing 🍋‍🟩

---

## ⚠️ Limitations
- Max image size: **40 MB** or **50 MP**
- PDF merge is simple — no reordering/layout options
- Only `JPEG` & `PNG` supported

---

## 🖥️ Run Locally
```bash
$ git clone https://github.com/your-username/squeezy.git
$ cd squeezy
$ pip install -r requirements.txt
$ python main.py

Visit http://localhost:5000


---

📤 Deployment

Render: Push repo → Create new web service → Start command: python main.py



---

👤 Author

Ameya Kulkarni
💻 GitHub | 📫 LinkedIn | 🎯 Codolio


---

📜 License: MIT — free to use, modify, and share.

⭐ If Squeezy saved your time, drop a star and spread the word! 🍋‍🟩




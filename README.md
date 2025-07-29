# 🍋‍🟩 Squeezy - Image Compressor, Resizer & Image to PDF Converter/ Merger 

**Squeezy** is a beginner-friendly web app built with **Python (Flask)** that compresses, resizes, and even converts multiple images into a single PDF, all in the browser, with no file stored beyond 5 seconds.

🌐 **Live Demo**: [squeezy-image-compressor.onrender.com](https://squeezy-image-compressor.onrender.com)
---

## 📸 Features

- 📤 Upload any image (`JPG`, `PNG`, etc.)
- 📏 Resize image by percentage (e.g., 50% of original size)
- 🗜️ Compress image quality (e.g., reduce to 60% quality)
- 📄 Convert multiple images into a **single downloadable PDF**
- ⚡ Instant processing and file download
- 🧹 **Auto-deletes files** from server 5 seconds after sending — no storage, full privacy
- 📱 Fully mobile-friendly UI using Bootstrap 5

---

## 🛠️ Tech Stack

| Part        | Tool             |
|-------------|------------------|
| Backend     | Python, Flask    |
| Frontend    | HTML5, Bootstrap |
| Imaging     | Pillow (PIL)     |
| Deployment  | Render           |

---

## 🚀 How It Works

### 🎯 Image Compression & Resizing
1. Upload an image
2. Choose:
   - Resize (% of original)
   - Compress (% quality reduction)
3. Click **Compress**
4. Instantly download your optimized image

### 📄 Convert Images to PDF
1. Upload **multiple images**
2. Hit **Generate PDF**
3. Instantly get a single merged `.pdf` to download

✅ All image/PDF processing is handled on the backend using **Pillow**, and files are sent back immediately  
❌ No data is stored, everything is **auto-deleted in 5 seconds**

---

## 🔐 Security & Privacy

⚠️ **Your files are NEVER stored.**

- Images and PDFs are **automatically deleted** from the server within 5 seconds of download.
- No logs, no tracking, no nonsense,just clean, fast processing.

---

## ⚠️ Limitations

- Max image size: **40 MB** or **50 megapixels**
- PDF merge is simple, no reordering or layout control
- Only standard formats (JPEG, PNG) supported

---

## ⚙️ Deployment

Deployed using [**Render.com**](https://render.com/)  
To run locally:

```
git clone https://github.com/your-username/squeezy.git
cd squeezy
pip install -r requirements.txt
python main.py

Then open your browser at http://localhost:5000
```

---

## 🙋‍♂️ Author

**Ameya Kulkarni**  
💻 [GitHub](https://github.com/Ameya79)  
📫 [LinkedIn](https://www.linkedin.com/in/ameya-kulkarni-a31b74246)  
🎯 [Codolio Profile](https://codolio.com/profile/Ameya%20Kulkarni)


---

📜 License

MIT License.
This project is open-source, feel free to fork it, build on it, or use it in your own projects.


---

⭐ Like the Project?

Drop a ⭐ if it saved your time, and feel free to contribute!
Suggestions & pull requests are welcome 😊


🍋‍🟩🍋‍🟩🍋‍🟩




# 🗜️ Squeezy - Image Compressor & Resizer

**Squeezy** is a simple, beginner-friendly web app that compresses and resizes images directly in your browser.

Built using **Python (Flask)** and styled with **Bootstrap**, it's ideal for anyone who wants a quick and efficient way to reduce image file sizes without losing too much quality.

🌐 **Live Demo**: [squeezy-image-compressor.onrender.com](https://squeezy-image-compressor.onrender.com)

---

## 📸 Features

- 📤 Upload any image (JPEG, PNG, etc.)
- 📏 Resize image by percentage (e.g., 50% of original size)
- 🗜️ Compress image quality (e.g., reduce to 60% quality)
- 📥 Instant download of the optimized image
- 🧹 Auto-deletes images after sending (no data is stored)
- 📱 Responsive design (mobile-friendly using Bootstrap)

---

## 🛠️ Tech Stack

| Part        | Tool           |
|-------------|----------------|
| Backend     | Python, Flask  |
| Frontend    | HTML5, Bootstrap 5 |
| Image Tools | Pillow (PIL)   |
| Deployment  | Render         |

---

## 🚀 How It Works

1. **Upload** your image
2. Choose how much to:
   - **Resize** (reduce dimensions)
   - **Compress** (reduce quality)
3. Hit **Compress!**
4. Download starts automatically with the compressed image

The backend uses **Pillow** to process and compress the image, and Flask handles the routing and temporary storage.

## 🧰 Project Structure

Squeezy/
│
├── templates/
│   └── index.html         # HTML form with Bootstrap
│
├── temp/                  # Temporary folder for processed images (auto-deleted)
│
├── main.py                # Flask backend
├── requirements.txt       # Python dependencies
└── README.md              # This file


## 🙋‍♂️ Author

**Ameya Kulkarni**
🔗 [LinkedIn](https://www.linkedin.com/in/ameya-kulkarni-a31b74246/)
🐙 [GitHub](https://github.com/Ameya79)

---

## 📜 License

This project is open-source and free to use.
Feel free to fork, modify, and contribute!

---

## ⭐ Like the Project?

Drop a ⭐ on the repo if you found it helpful!
Pull requests and suggestions are always welcome 😊

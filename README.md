<h1 align="center">🍋‍🟩 Squeezy </h1>

<p align="center">
  <strong>Fast, private image compression, resizing, and image-to-PDF conversion.</strong>
</p>

<p align="center">
  <a href="https://github.com/Ameya79/Squeezy-Image-Compressor/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License: MIT"></a>
  <img src="https://img.shields.io/badge/python-3.8%2B-blue.svg" alt="Python 3.8+">
  <img src="https://img.shields.io/badge/flask-2.x-lightgrey.svg" alt="Flask 2.x">
  <img src="https://img.shields.io/badge/pillow-Image%20Engine-green.svg" alt="Pillow Engine">
  <img src="https://img.shields.io/badge/privacy-100%25%20ephemeral-purple.svg" alt="Ephemeral Privacy">
</p>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#run-with-docker">Run with Docker</a> •
  <a href="#local-development">Local Development</a> •
  <a href="#how-it-works">How It Works</a> •
  <a href="#tech-stack">Tech Stack</a>
</p>

---

**Squeezy** is a lightweight Python web application built with Flask and Pillow that lets you compress, resize, and convert images into multi-page PDFs instantly in your browser. All processing is kept ephemeral with automated cleanup: no third-party tracking, no permanent database, and complete privacy.

🌐 **Live Demo:** [squeezy-image-compressor.onrender.com](https://squeezy-image-compressor.onrender.com)  
*(Note: Free-tier cloud instances may take a few seconds to spin up on first request.)*

---

## 📸 Features

- 📤 **Broad Format Support**: Upload any image (`JPG`, `PNG`, `WebP`).
- 📏 **Proportional Resizing**: Scale images by percentage (e.g., 50% or 25% of original dimensions) with high-quality Lanczos resampling.
- 🗜️ **Configurable Compression**: Control output quality and file size reduction.
- 📄 **Multi-Image PDF Merger**: Bundle multiple photos into a single, clean PDF document.
- ⚡ **Instant Processing**: In-memory buffers via `io.BytesIO` for low-latency transformations.
- 🧹 **Automatic Cleanup**: Temporary files auto-delete within 5 seconds of creation.
- 📱 **Responsive UI**: Clean Bootstrap 5 interface designed for both mobile and desktop screens.

---

## 🐳 Run with Docker

Anyone can run Squeezy locally with zero manual environment configuration:

```bash
# Clone the repository
git clone https://github.com/Ameya79/Squeezy-Image-Compressor.git
cd Squeezy-Image-Compressor

# Start the web app with Docker Compose
docker compose up
```

Once started, open [http://localhost:5000](http://localhost:5000) in your browser.

---

## 🖥️ Local Development

If you prefer running directly in Python:

```bash
# 1. Clone repository
git clone https://github.com/Ameya79/Squeezy-Image-Compressor.git
cd Squeezy-Image-Compressor

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start development server
python main.py
```

The application will be live at `http://localhost:5000`.

---

## 🚀 How It Works

### 1. Image Compression and Resizing
1. Upload an image file.
2. Select your desired resize percentage and compression quality.
3. Click **Compress** to trigger immediate processing and automatic file download.

### 2. Image to PDF Conversion
1. Select one or more images.
2. Click **Generate PDF**.
3. Download your merged PDF directly in your browser.

All processing operates with in-memory streams using `io.BytesIO` whenever possible. Any temporary cache files created during processing are purged automatically after 5 seconds.

---

## 🛠 Tech Stack

| Component | Technology | Description |
|:---|:---|:---|
| **Backend** | Python 3, Flask | Lightweight web routing and request handling |
| **Imaging Engine** | Pillow (PIL), OpenCV | Image resizing, compression, and PDF generation |
| **Frontend** | HTML5, Bootstrap 5 | Mobile-friendly responsive user interface |
| **Production Server** | Gunicorn | Production WSGI HTTP server |
| **Containerization** | Docker, Docker Compose | Reproducible cross-platform local runtime |

---

## 🔐 Privacy Guarantee

- **Zero Permanent Storage**: Uploaded images are never retained on the server.
- **Zero Telemetry**: No third-party analytics or user activity tracking.
- **Auto Cleanup**: Background garbage collector deletes files within 5 seconds.

---

## 👤 Author

**Ameya Kulkarni**  
GitHub: [@Ameya79](https://github.com/Ameya79)

---

## 📜 License

Distributed under the **MIT License**. Free to use, modify, and distribute.

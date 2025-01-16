
# Wardrobe Assistant

**Wardrobe Assistant** is an AI-powered web application that helps users select outfits by analyzing shirt images and overlaying them onto a live video feed based on pose detection. It also removes backgrounds from uploaded shirt images.

## Features

- **Background Customization**: Set a personalized background.
- **Live Video Feed**: Overlay shirt images based on the user's pose.
- **Pose Detection**: Adjust shirt overlay using `mediapipe` pose landmarks.
- **Background Removal**: Remove shirt image backgrounds using `rembg`.
- **Shirt Upload**: Upload images in `.png`, `.jpg`, `.jpeg` formats.

## Technologies Used

- **Python 3.x**
- **OpenCV**, **Streamlit**, **mediapipe**, **rembg**, **NumPy**

## Setup and Installation

1. Clone the repo:

```bash
git clone https://github.com/NIKHILSONI9/Wardrobe-Assistant.git
cd Wardrobe-Assistant
```

2. Set up a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the app:

```bash
streamlit run finalward.py
```

## How to Use

1. Upload a shirt image.
2. Click "Start Live Video" to overlay the shirt on your body using pose detection.
3. The app removes the background from the shirt image and adjusts it based on your pose.

## Team Members

- **Nikhil Soni** - 221b251
- **Nirmal Singh** - 221b252
- **Prakash Mani Patel** - 221b268

---

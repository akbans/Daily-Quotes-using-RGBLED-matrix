# Quote of the Day - RGB LED Matrix Display

This project displays a **Quote of the Day** on a **32x64 RGB LED matrix** using **CircuitPython**. The quotes are dynamically fetched from a **local text file (`quotes.txt`)**, ensuring a diverse and easily expandable collection of quotes. The **date and title** are displayed at the top, while the quote scrolls smoothly below.

---

## 📸 Screenshots  


---

## 🎥 Video Demonstration  
[Watch the project in action!](https://youtu.be/ffJxgOLv8dA)  

---

## 📂 Repository Structure  
- `main.py` – The main CircuitPython script
- `quotes.txt` – A text file containing 100+ quotes
- `4x6.bdf` – Font file for smaller text
- `README.md` – This documentation  

---

## 🔧 Features  
✅ **Quote of the Day** – A different quote is shown each day, selected based on the date. The quote smoothly scrolls across the matrix. 
✅ **Random Colors** – Each quote is displayed in a randomly chosen color.  
✅ **Easy Quote Management** – Simply edit `quotes.txt` to add, remove, or modify quotes.  

---

## 🛠️ Hardware Requirements  
- **32x64 RGB LED Matrix**  
- **CircuitPython-Compatible Microcontroller** (e.g., Feather M4, Raspberry Pi Pico, ESP32-S3)  
- **External Power Supply (5V, 2A recommended)**  
- **Jumper Wires & Connectors**  

---

## 🔌 Setup & Installation  

### 1️⃣ Install CircuitPython  
Make sure your board is running CircuitPython. Download it from the [official CircuitPython website](https://circuitpython.org/).  

### 2️⃣ Install Required Libraries  
Copy the following CircuitPython libraries into the `/lib` folder of your board:  
- `adafruit_display_text`  
- `adafruit_bitmap_font`  
- `rgbmatrix`  
- `framebufferio`  

(*You can download these from the [Adafruit CircuitPython Bundle](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases).*)

### 3️⃣ Upload Files  
Copy the following files to the **root directory** of your board:  
✅ `main.py`  
✅ `quotes.txt`  
✅ `fonts/4x6.bdf`  

### 4️⃣ Run the Code  
The script should automatically run when the board is powered on. If needed, restart your board.  

---

## 🎯 Customization  

### ✏️ Changing Quotes  
Edit `quotes.txt` to add your own quotes. Each quote should be on a **new line**.

### 🎨 Adjusting Colors  
The colors of the scrolling text are randomly generated. You can modify the function `get_random_color()` in `main.py` to use specific colors.

### 🔄 Changing Fonts  
To use a different font, replace `4x6.bdf` with another `.bdf` font and update the `main.py` script accordingly.

---

## 🤝 Contributions  
Feel free to contribute to this project by adding **more quotes, improving the scrolling effect, or enhancing the UI**. Fork the repository and submit a **pull request**!

---

## 📜 This was made for hackclub neon (https://neon.hackclub.dev/) 

---

🚀 **Enjoy your daily inspiration on an RGB matrix!**  

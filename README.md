# en.co - Simple Caesar Cipher Web App

A simple web application for encrypting and decrypting messages using a Caesar cipher. Perfect for sending secret messages to friends!

## Features

- **Simple Interface**: Clean, modern web interface
- **Encrypt/Decrypt**: Toggle between encryption and decryption modes
- **Customizable Key**: Choose any key from 1-36
- **Copy to Clipboard**: One-click copying of results
- **Mobile Friendly**: Responsive design that works on all devices

## Local Setup

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   python app.py
   ```

3. Open your browser and go to: `http://localhost:8080`

## Deployment Options

### Option 1: Render (Recommended - Free)

1. Create a GitHub repository and push your code
2. Go to [render.com](https://render.com) and sign up
3. Click "New +" → "Web Service"
4. Connect your GitHub repository
5. Render will automatically detect the `render.yaml` file
6. Click "Create Web Service"
7. Your app will be deployed to a URL like: `https://your-app-name.onrender.com`

### Option 2: Railway (Free)

1. Go to [railway.app](https://railway.app) and sign up
2. Click "New Project" → "Deploy from GitHub repo"
3. Connect your GitHub repository
4. Railway will automatically detect the `Procfile`
5. Your app will be deployed to a URL like: `https://your-app-name.railway.app`

### Option 3: Heroku (Paid)

1. Install Heroku CLI
2. Create a Heroku account
3. Run these commands:
   ```bash
   heroku create your-app-name
   git add .
   git commit -m "Initial commit"
   git push heroku main
   ```

## How to Use

1. **Encrypt a Message**:
   - Select "Encrypt" mode
   - Enter your message
   - Choose a key (remember this key!)
   - Click "Process Message"
   - Copy the encrypted result and send to your friend

2. **Decrypt a Message**:
   - Select "Decrypt" mode
   - Paste the encrypted message
   - Use the same key that was used for encryption
   - Click "Process Message"
   - Read the decrypted message

## How It Works

The app uses a simple Caesar cipher that shifts characters in the alphabet. The character set includes:
- All lowercase letters (a-z)
- Numbers (0-9)
- Space character

The key determines how many positions to shift each character. For decryption, the same key is used but in reverse.

## Security Note

This is a basic Caesar cipher for fun and educational purposes. It's not suitable for secure communication as it can be easily cracked with frequency analysis.

## Files

- `cipher.py` - The core encryption/decryption function
- `app.py` - Flask web application
- `templates/index.html` - Web interface
- `requirements.txt` - Python dependencies
- `render.yaml` - Render deployment configuration
- `Procfile` - Railway/Heroku deployment configuration 
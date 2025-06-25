# Steve's AI Best Friend App

## Features:
- Real-time WhatsApp messaging
- Voice call replies with ElevenLabs custom voice
- Warm AI-style support replies
- Deploys easily to Render

## Render Setup:
1. Upload all files to GitHub
2. Create a new Render Web Service
3. Set:
   - **Build Command**: pip install -r requirements.txt
   - **Start Command**: gunicorn app:app

4. Add Environment Variables:
   - TWILIO_SID
   - TWILIO_AUTH
   - TWILIO_WHATSAPP (e.g., whatsapp:+123456789)
   - TWILIO_CALLER (e.g., +123456789)
   - MY_PHONE (your number)
   - ELEVENLABS_API_KEY
   - ELEVENLABS_VOICE_ID

5. Twilio Console:
   - Set WhatsApp webhook to `/whatsapp`
   - Set Voice webhook to `/voice`

6. Make sure `steve_response.mp3` is publicly hosted if used for voice playback.
from gtts import gTTS
speech = gTTS(text = "What's up Shukla family! Glad to meet you. I am Tejas' new speaking machine.", lang = "en", tld = "co.in")
speech_hindi = gTTS(text = 'हैलो शुक्ल परिवार! आपसे मिलकर खुशी हुई! मैं तेजस की मशीन हूँ।', lang="hi")
with open('gTTS greeting.mp3', 'wb') as f:
    speech_hindi.write_to_fp(f)
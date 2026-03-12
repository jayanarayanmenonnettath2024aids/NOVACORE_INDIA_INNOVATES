import random
import time
from typing import Dict, Any
from loguru import logger

class SpeechToTextEngine:
    """
    Simulates a production-grade Speech-to-Text engine (e.g., Whisper or Sarvam AI).
    Includes logic for noise simulation, transcription confidence, and multi-language support.
    """
    
    DICTIONARY = {
        "en": [
            "I need help with a broken water pipe outside my home.",
            "There is no electricity in our street for 5 hours.",
            "A large pothole has opened up at the main highway crossing.",
            "Garbage collection hasn't happened in 3 weeks, it's a health risk.",
            "Streetlights are not working in Sector 4, it feels unsafe."
        ],
        "hi": [
            "मेरे घर के बाहर पानी का पाइप फट गया है, कृपया मदद करें।",
            "हमारी गली में 5 घंटे से बिजली नहीं है।",
            "मुख्य हाईवे चौराहे पर एक बड़ा गड्ढा हो गया है।"
        ],
        "ta": [
            "என் வீட்டின் வெளியே தண்ணீர் குழாய் வெடித்துவிட்டது, தயவுசெய்து உதவுங்கள்.",
            "எங்கள் தெருவில் 5 மணிநேரமாக மின்சாரம் இல்லை.",
            "மெயின் ரோட்டில் பெரிய பள்ளம் ஏற்பட்டுள்ளது."
        ]
    }

    @staticmethod
    def transcribe_audio_stream(audio_buffer: bytes, language_hint: str = None) -> Dict[str, Any]:
        """
        Simulates the processing of an audio stream into text.
        """
        logger.info("Transcribing audio stream...")
        time.sleep(1.2) # Artificial processing latency
        
        # Select target language
        lang = language_hint if language_hint in SpeechToTextEngine.DICTIONARY else random.choice(list(SpeechToTextEngine.DICTIONARY.keys()))
        
        # Select transcription
        text = random.choice(SpeechToTextEngine.DICTIONARY[lang])
        
        # Simulate confidence score
        confidence = random.uniform(0.85, 0.99)
        
        return {
            "text": text,
            "detected_language": lang,
            "confidence_score": confidence,
            "processing_time_ms": 1200,
            "is_final": True
        }

class TextToSpeechEngine:
    """
    Simulates producing high-quality human-like voice responses (e.g., ElevenLabs).
    """
    
    @staticmethod
    def synthesize_speech(text: str, voice_profile: str = "PALLAVI_V3_SMOOTH") -> bytes:
        """
        Simulates synthesizing speech from text. Returns mock binary data.
        """
        logger.info(f"Synthesizing speech for: {text[:30]}...")
        # In a real system, this would call a cloud API or local model
        return b"MOCK_MP3_DATA_FOR_" + text.encode()[:20]

speech_engine = SpeechToTextEngine()
tts_engine = TextToSpeechEngine()

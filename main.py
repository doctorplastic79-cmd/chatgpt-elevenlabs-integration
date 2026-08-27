import os
from dotenv import load_dotenv
import openai
from elevenlabs.client import ElevenLabs
import time

load_dotenv()

# Configurare le API
openai.api_key = os.getenv("OPENAI_API_KEY")
elevenlabs_api_key = os.getenv("ELEVENLABS_API_KEY")

# Inizializzare il client di ElevenLabs
elevenlabs_client = ElevenLabs(api_key=elevenlabs_api_key)

def chat_with_voice(user_message: str, voice_id: str = "21m00Tcm4TlvDq8ikWAM") -> str:
    """
    Invia un messaggio a ChatGPT e converte la risposta in audio con ElevenLabs
    
    Args:
        user_message: Il messaggio da inviare a ChatGPT
        voice_id: L'ID della voce ElevenLabs (default: Rachel)
    
    Returns:
        La risposta testuale di ChatGPT
    """
    
    print(f"\n🎯 Tu: {user_message}")
    print("-" * 50)
    
    try:
        # 1. Ottieni risposta da ChatGPT
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Sei un assistente utile e amichevole."},
                {"role": "user", "content": user_message}
            ]
        )
        
        chat_response = response.choices[0].message.content
        print(f"\n💬 ChatGPT: {chat_response}\n")
        
        # 2. Converti risposta in audio con ElevenLabs
        print("🎙️  Generando audio...")
        audio = elevenlabs_client.generate(
            text=chat_response,
            voice_id=voice_id,
            model="eleven_monolingual_v1"
        )
        
        # 3. Salva l'audio
        with open("response.mp3", "wb") as f:
            f.write(audio)
        
        print("✅ Audio salvato come 'response.mp3'\n")
        return chat_response
        
    except Exception as e:
        print(f"❌ Errore: {str(e)}")
        return None

def chat_stream_voice(user_message: str, voice_id: str = "21m00Tcm4TlvDq8ikWAM"):
    """
    Streaming di ChatGPT con audio in tempo reale
    """
    
    print(f"\n🎯 Tu: {user_message}")
    print("-" * 50)
    print("💬 ChatGPT: ", end="", flush=True)
    
    try:
        # Stream dalla risposta di ChatGPT
        stream = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Sei un assistente utile e amichevole."},
                {"role": "user", "content": user_message}
            ],
            stream=True
        )
        
        full_response = ""
        
        # Accumula il testo
        for chunk in stream:
            if chunk.choices[0].delta.get("content"):
                text = chunk.choices[0].delta.content
                full_response += text
                print(text, end="", flush=True)
        
        print("\n")
        
        # Genera audio dalla risposta completa
        print("🎙️  Generando audio...")
        audio = elevenlabs_client.generate(
            text=full_response,
            voice_id=voice_id,
            model="eleven_monolingual_v1"
        )
        
        with open("response_stream.mp3", "wb") as f:
            f.write(audio)
        
        print("✅ Audio salvato come 'response_stream.mp3'\n")
        
    except Exception as e:
        print(f"❌ Errore: {str(e)}")

if __name__ == "__main__":
    # Esempio 1: Modo semplice
    chat_with_voice("Dimmi una barzelletta divertente")
    
    # Esempio 2: Modo streaming (decommentare per usare)
    # chat_stream_voice("Spiegami come funziona l'intelligenza artificiale in 3 punti")

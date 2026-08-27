"""Esempio avanzato con interfaccia conversazionale"""

import os
from dotenv import load_dotenv
import openai
from elevenlabs.client import ElevenLabs
import json
from datetime import datetime

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
elevenlabs_client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

class ChatGPTVoiceAssistant:
    def __init__(self, voice_id: str = "21m00Tcm4TlvDq8ikWAM"):
        self.voice_id = voice_id
        self.conversation_history = []
        self.audio_count = 0
        
    def add_message(self, role: str, content: str):
        """Aggiungi un messaggio alla cronologia della conversazione"""
        self.conversation_history.append({
            "role": role,
            "content": content
        })
    
    def chat(self, user_input: str, generate_audio: bool = True) -> str:
        """Esegui una conversazione con ChatGPT e genera audio opzionalmente"""
        
        self.add_message("user", user_input)
        
        try:
            # Ottieni risposta da ChatGPT
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=self.conversation_history,
                temperature=0.7,
                max_tokens=500
            )
            
            assistant_response = response.choices[0].message.content
            self.add_message("assistant", assistant_response)
            
            # Genera audio se richiesto
            if generate_audio:
                self.generate_audio(assistant_response)
            
            return assistant_response
        
        except Exception as e:
            print(f"❌ Errore: {str(e)}")
            return None
    
    def generate_audio(self, text: str):
        """Genera un file audio dalla risposta"""
        try:
            self.audio_count += 1
            audio = elevenlabs_client.generate(
                text=text,
                voice_id=self.voice_id,
                model="eleven_monolingual_v1"
            )
            
            filename = f"audio_{self.audio_count:03d}.mp3"
            with open(filename, "wb") as f:
                f.write(audio)
            
            print(f"✅ Audio salvato: {filename}")
        except Exception as e:
            print(f"❌ Errore nella generazione audio: {str(e)}")
    
    def save_conversation(self, filename: str = "conversation.json"):
        """Salva la cronologia della conversazione"""
        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(self.conversation_history, f, ensure_ascii=False, indent=2)
            print(f"✅ Conversazione salvata in {filename}")
        except Exception as e:
            print(f"❌ Errore nel salvataggio: {str(e)}")
    
    def clear_history(self):
        """Pulisci la cronologia della conversazione"""
        self.conversation_history = []
        print("✅ Cronologia cancellata")
    
    def interactive_chat(self):
        """Avvia una sessione interattiva di chat"""
        print("\n🎙️  Assistente Vocale ChatGPT + ElevenLabs")
        print("Digita 'esci' per terminare, 'salva' per salvare la conversazione\n")
        
        while True:
            try:
                user_input = input("Tu: ").strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() == "esci":
                    print("\n👋 Arrivederci!")
                    break
                
                if user_input.lower() == "salva":
                    self.save_conversation()
                    continue
                
                response = self.chat(user_input)
                if response:
                    print(f"\n🤖 Assistente: {response}\n")
            
            except KeyboardInterrupt:
                print("\n\n👋 Arrivederci!")
                break
            except Exception as e:
                print(f"\n❌ Errore: {str(e)}\n")

if __name__ == "__main__":
    # Crea l'assistente
    assistant = ChatGPTVoiceAssistant()
    
    # Avvia la chat interattiva
    assistant.interactive_chat()
    
    # Salva la conversazione alla fine
    assistant.save_conversation()

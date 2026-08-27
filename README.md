# ChatGPT + ElevenLabs Integration 🎙️

Integrazione di ChatGPT con ElevenLabs Text-to-Speech per generare risposte vocali intelligenti.

## 🚀 Cosa fa

- Invia messaggi a ChatGPT
- Ricevi risposte in testo
- Converti automaticamente le risposte in audio con ElevenLabs
- Salva i file audio in formato MP3

## 📋 Prerequisiti

- Python 3.8+
- Account OpenAI con API key
- Account ElevenLabs con API key

## 🔧 Setup

### 1. Clona il repository
```bash
git clone https://github.com/doctorplastic79-cmd/chatgpt-elevenlabs-integration.git
cd chatgpt-elevenlabs-integration
```

### 2. Crea un ambiente virtuale
```bash
python -m venv venv
source venv/bin/activate  # Su Windows: venv\\Scripts\\activate
```

### 3. Installa le dipendenze
```bash
pip install -r requirements.txt
```

### 4. Configura le API key

**Passo A: Copia il file di esempio**
```bash
cp .env.example .env
```

**Passo B: Aggiungi le tue chiavi nel file `.env`**
```
OPENAI_API_KEY=sk-your-openai-key-here
ELEVENLABS_API_KEY=your-elevenlabs-key-here
```

### 5. Esegui il programma
```bash
python main.py
```

## 📚 Come ottenere le API Keys

### OpenAI API Key
1. Vai su https://platform.openai.com/api-keys
2. Accedi con il tuo account OpenAI
3. Clicca "Create new secret key"
4. Copia la chiave nel file `.env`

### ElevenLabs API Key
1. Vai su https://elevenlabs.io
2. Registrati o accedi
3. Vai su Profile → API Keys
4. Copia la tua API key nel file `.env`

## 🎤 Voice IDs disponibili

| Voice | ID |
|-------|-----|
| Adam | pNInz6obpgDQGcFmaJgB |
| Rachel | 21m00Tcm4TlvDq8ikWAM |
| Domi | AZnzlk1mvXvSfvlW |
| Bella | EXAVITQu4vr4xnSDxMaL |
| Antoni | zcAOhNBS0xrsDMBLcxyz |
| Arnold | jBpfuIE2acIu3nSshUMc |

## 💻 Utilizzo

### Modo semplice
```python
from main import chat_with_voice

chat_with_voice("Dimmi una barzelletta")
```

### Modo streaming
```python
from main import chat_stream_voice

chat_stream_voice("Spiegami come funziona l'IA")
```

### Con voce personalizzata
```python
chat_with_voice("Ciao!", voice_id="pNInz6obpgDQGcFmaJgB")  # Usa Adam
```

## 🎯 Esempi di utilizzo

```bash
# Avvia il programma
python main.py

# L'output sarà:
# 🎯 Tu: Dimmi una barzelletta divertente
# --------------------------------------------------
# 💬 ChatGPT: [La risposta di ChatGPT]
# 🎙️  Generando audio...
# ✅ Audio salvato come 'response.mp3'
```

Poi puoi ascoltare `response.mp3` con il tuo player audio preferito!

## ⚠️ Limitazioni e costi

- **OpenAI**: Addebito per token usati. Consulta i prezzi: https://openai.com/pricing
- **ElevenLabs**: 10,000 caratteri gratis al mese, poi addebiti per caratteri aggiuntivi
- **Rate limiting**: Entrambi i servizi hanno limiti di richieste. Rispetta questi limiti!

## 🐛 Troubleshooting

### "API key not found"
- Verifica che il file `.env` esista
- Assicurati di aver aggiunto le chiavi corrette
- Riavvia il programma dopo aver modificato `.env`

### "Invalid API key"
- Controlla che la chiave sia copiata correttamente (senza spazi)
- Verifica che la chiave sia ancora valida su OpenAI e ElevenLabs

### "Connection error"
- Controlla la tua connessione internet
- Verifica che i server di OpenAI e ElevenLabs siano raggiungibili

## 📝 Licenza

MIT License - vedi il file LICENSE per dettagli

## 🤝 Contributi

Contributi sono benvenuti! Fai un fork, crea un branch per la tua feature e invia una pull request.

## 📧 Supporto

Per problemi o domande, apri un issue nel repository!

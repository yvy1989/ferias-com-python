#importação da biblioteca
import pyttsx3

# Inicialize o mecanismo TTS
engine = pyttsx3.init()

# Obtenha a configuração do mecanismo
rate = engine.getProperty('rate')

# Defina uma taxa de fala mais baixa (por exemplo, 150)
engine.setProperty('rate', 150)

# Defina o texto que você deseja que o Python fale
text = "férias com paiton"

# Fale o texto
engine.say(text)

# Aguarde até que a fala seja concluída antes de encerrar o programa
engine.runAndWait()

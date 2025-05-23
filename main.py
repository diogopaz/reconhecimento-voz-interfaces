import speech_recognition as sr
import os

def reconhecer_fala_do_microfone(recognizer, microfone):
    if not isinstance(microfone, sr.Microphone):
        raise TypeError("`microfone` deve ser uma instância de `sr.Microphone`")

    with microfone as source:
        print("Ajustando para o ruído ambiente, por favor aguarde...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Pronto! Diga alguma coisa...")

        try:
            audio = recognizer.listen(source, timeout=7, phrase_time_limit=15)
            print("Reconhecendo...")
            texto_reconhecido = recognizer.recognize_google(audio, language='pt-BR')
            print(f"Você disse: {texto_reconhecido}")
            return texto_reconhecido
        except sr.WaitTimeoutError:
            print("Nenhuma fala detectada dentro do tempo limite.")
        except sr.UnknownValueError:
            print("Não foi possível entender o áudio.")
        except sr.RequestError as e:
            print(f"Não foi possível solicitar resultados do serviço de reconhecimento de fala do Google; {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado durante o reconhecimento do microfone: {e}")
    return None

def reconhecer_fala_do_arquivo(recognizer, nome_arquivo_audio):
    if not os.path.exists(nome_arquivo_audio):
        print(f"Erro: Arquivo '{nome_arquivo_audio}' não encontrado. Verifique o caminho.")
        return None

    print(f"Processando o arquivo de áudio: {nome_arquivo_audio}")

    with sr.AudioFile(nome_arquivo_audio) as source:
        try:
            audio = recognizer.record(source)
        except Exception as e:
            print(f"Erro ao carregar o arquivo de áudio '{nome_arquivo_audio}'.")
            print(f"Verifique se o arquivo é um formato WAV válido.")
            print(f"Detalhe do erro: {e}")
            return None

        print("Reconhecendo...")
        try:
            texto_reconhecido = recognizer.recognize_google(audio, language='pt-BR')
            print(f"Texto no áudio: {texto_reconhecido}")
            return texto_reconhecido
        except sr.UnknownValueError:
            print("Não foi possível entender o áudio do arquivo.")
        except sr.RequestError as e:
            print(f"Não foi possível solicitar resultados do serviço de reconhecimento de fala do Google; {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado durante o reconhecimento do arquivo: {e}")
    return None

def main():
    r = sr.Recognizer()

    while True:
        print("\nEscolha uma opção:")
        print("1. Reconhecer fala do microfone")
        print("2. Reconhecer fala de um arquivo de áudio (.wav)")
        print("3. Sair")

        escolha = input("Digite o número da sua escolha: ")

        if escolha == '1':
            print("\n--- Reconhecimento do Microfone ---")
            try:
                mic = sr.Microphone()
                reconhecer_fala_do_microfone(r, mic)
            except AttributeError:
                 print("Erro: `sr.Microphone()` não está disponível. Verifique a instalação do PyAudio e se há um microfone.")
            except Exception as e:
                 print(f"Erro ao inicializar o microfone: {e}")

        elif escolha == '2':
            print("\n--- Reconhecimento de Arquivo de Áudio ---")
            nome_arquivo = input("Digite o nome do arquivo de áudio (ex: exemplo.wav): ")
            if not os.path.exists(nome_arquivo):
                print(f"Arquivo '{nome_arquivo}' não encontrado. Por favor, certifique-se que ele existe no mesmo diretório do script ou forneça o caminho completo.")
                print("Você pode baixar arquivos de exemplo .wav do FreeSound (https://freesound.org/).")
            else:
                if not nome_arquivo.lower().endswith(".wav"):
                    print("Apenas arquivos .wav são suportados para esta opção.")
                else:
                    reconhecer_fala_do_arquivo(r, nome_arquivo)

        elif escolha == '3':
            break
        else:
            print("Escolha inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
## Funcionalidade
Microfone: Usa o SpeechRecognition para capturar e transcrever fala em tempo real.
Arquivo WAV: Lê o arquivo WAV e transcreve seu conteúdo.
Menu Interativo: Interface simples para escolher entre microfone ou arquivo.
    
## Como Usar

-- Clone o Repositório
-- Baixe o repositório para o seu ambiente de desenvolvimento.
-- Navegue até o Diretório do Projeto
-- Abra o terminal e entre no diretório onde o script reconhecedor_de_voz.py está localizado.
-- Executar o Script
-- Execute o script Python utilizando o comando:
```python
        python reconhecedor_de_voz.py
```
-- Escolher a Opção no Menu
-- Após o script iniciar, o menu interativo será exibido:
-- Escolha '1' para iniciar o reconhecimento de fala via microfone.
-- Certifique-se de que seu microfone está conectado e funcionando.
-- Siga as instruções na tela para falar no microfone.
-- Escolha '2' para reconhecer fala de um arquivo WAV.
-- Insira o caminho para o arquivo WAV quando solicitado. Exemplo: exemplos/sola_na_bota.wav.
--  Observação dos Resultados
-- Veja a transcrição do áudio diretamente no console.
-- Sair do Programa
-- Escolha '3' no menu para encerrar o programa.

## Instalação

Instale as dependências:
```python
pip install SpeechRecognition
pip install pyaudio
```

if __name__ == "__main__":
    main()

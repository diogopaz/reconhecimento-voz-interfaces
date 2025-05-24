
# Reconhecedor de Voz

Este projeto permite transcrever áudio em texto utilizando reconhecimento de fala. Funciona tanto com entrada via microfone quanto através de um arquivo WAV.

## Funcionalidades

- Microfone: Usa a biblioteca SpeechRecognition para capturar e transcrever fala em tempo real.
- Arquivo WAV: Lê um arquivo de áudio no formato WAV e transcreve seu conteúdo.
- Menu Interativo: Interface simples no terminal para escolher entre microfone ou arquivo.

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

2. Acesse o diretório do projeto:

```bash
cd seu-repositorio
```

3. Instale as dependências necessárias:

```bash
pip install SpeechRecognition
pip install pyaudio
```

## Como Usar

1. Execute o script principal:

```bash
python reconhecedor_de_voz.py
```

2. No menu interativo, escolha a opção desejada:

- [1] Reconhecimento por Microfone

- [2] Reconhecimento por Arquivo WAV
   - Informe o caminho para o arquivo de áudio quando solicitado.  
   Exemplo:
   ```
   exemplos/sola_na_bota.wav
   ```

- [3] Sair
   - Encerra o programa.

3. A transcrição do áudio será exibida diretamente no console.

## Estrutura Principal

O script é iniciado a partir do seguinte bloco:

```python
if __name__ == "__main__":
    main()
```

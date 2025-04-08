# Animal Crossing 24/7 Bot

Este é um projeto de um bot para Discord desenvolvido em Python. O bot possui funcionalidades relacionadas à reprodução de músicas baseadas no horário atual, além de comandos básicos para interação com os usuários.

## Funcionalidades

- **Reprodução de músicas baseadas no horário**:
  - O bot toca músicas específicas dependendo do horário atual.
  - As músicas são organizadas em uma pasta chamada `Audios` e devem seguir o formato `<hora>_<am/pm>.mp3` (exemplo: `12_am.mp3` para meia-noite ou `3_pm.mp3` para 3 da tarde).

- **Troca automática de músicas**:
  - Quando o horário muda, o bot aguarda a música atual terminar antes de trocar para a música correspondente ao novo horário.

- **Seleção de jogo e clima**:
  - Use o comando `!select` para escolher o jogo e o clima através de menus suspensos interativos no Discord.
  - Jogos disponíveis:
    - Animal Crossing: GameCube
    - Animal Crossing: Wild World
    - Animal Crossing: City Folk
    - Animal Crossing: New Leaf
    - Animal Crossing: New Horizons
  - Climas disponíveis:
    - Sunny ☀️
    - Snowy ❄️
    - Rainy 🌧️

- **Reinício da música atual**:
  - O comando `!refresh` permite reiniciar a música atual sem precisar desconectar o bot.

- **Desconexão automática**:
  - O bot se desconecta automaticamente do canal de voz caso fique sozinho.

- **Comando de exibição de música atual**:
  - O comando `!musica` exibe a música que está sendo tocada no momento.

## Requisitos

- Python 3.8 ou superior.
- Biblioteca `discord.py` instalada.
- FFmpeg instalado no sistema (necessário para reprodução de áudio).

## Estrutura do Projeto

## Configuração

1. **Instale as dependências**:
   - Crie um ambiente virtual:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - Instale as bibliotecas necessárias:
     ```bash
     pip install discord.py
     ```

2. **Configure o token do bot**:
   - Crie um arquivo chamado [apikeys.py](http://_vscodecontentref_/7) na pasta [Codes](http://_vscodecontentref_/8) e adicione o  dotoken bot:
     ```python
     TOKEN = "seu_token_aqui"
     ```

3. **Adicione as músicas**:
   - Coloque os arquivos de áudio na pasta [Audios](http://_vscodecontentref_/9) com o formato `<hora>_<am/pm>.mp3`.

4. **Instale o FFmpeg**:
   - No Linux, use:
     ```bash
     sudo apt install ffmpeg
     ```

## Comandos Disponíveis

- `!play`: Conecta o bot ao canal de voz do usuário e começa a tocar músicas baseadas no horário, jogo e clima selecionados.
- `!select`: Exibe menus suspensos para selecionar o jogo e o clima.
- `!refresh`: Reinicia a música atual que está sendo tocada.
- `!musica`: Exibe a música que está sendo tocada no momento.
- `!stop`: Desconecta o bot do canal de voz e encerra sua execução.

## Funcionamento

1. O bot toca músicas baseadas no horário atual, utilizando a função [meridiantime()](http://_vscodecontentref_/10) para determinar o arquivo de áudio correto.
2. Quando o horário muda, o bot aguarda a música atual terminar antes de trocar para a próxima.
3. Use o comando `!select` para escolher o jogo e o clima.
4. Caso o bot fique sozinho no canal de voz, ele se desconecta automaticamente.

## Exemplo de Uso

1. Entre em um canal de voz no Discord.
2. Use o comando `!select` para escolher o jogo e o clima.
3. Use o comando `!play` para o bot começar a tocar músicas.
4. Use o comando `!refresh` para reiniciar a música atual.
5. Use o comando `!musica` para verificar qual música está sendo tocada.
6. Se sair do canal de voz e o bot ficar sozinho, ele se desconectará automaticamente.

## Observações

- Certifique-se de que o bot tenha permissões para conectar-se ao canal de voz e reproduzir áudio.
- As músicas devem estar no formato `.mp3` e seguir o padrão de nomenclatura esperado.

## Autor

Este projeto foi desenvolvido como um teste para criar um bot do Discord com funcionalidades de reprodução de áudio baseadas no horário.

Divirta-se! 😄

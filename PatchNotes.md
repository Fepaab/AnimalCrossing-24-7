# Patch Notes - Animal Crossing 24/7 Bot

## Versão Atual: 1.1.0

---

### Novas Funcionalidades

1. **Comando `!refresh`**:
   - Adicionado o comando `!refresh` que permite reiniciar a música atual sem precisar desconectar o bot.
   - O comando verifica o horário, o jogo e o clima selecionados para reiniciar a música correta.
   - Mensagens de confirmação são enviadas no canal de texto, e logs detalhados são exibidos no terminal.

2. **Comando `!select`**:
   - Agora é possível selecionar o **jogo** e o **clima** através de menus suspensos interativos no Discord.
   - As opções disponíveis para jogos incluem:
     - Animal Crossing: GameCube
     - Animal Crossing: Wild World
     - Animal Crossing: City Folk
     - Animal Crossing: New Leaf
     - Animal Crossing: New Horizons
   - As opções de clima incluem:
     - Sunny ☀️
     - Snowy ❄️
     - Rainy 🌧️
   - As seleções são armazenadas globalmente e usadas nos comandos `!play` e `!refresh`.

3. **Comando `!musica`**:
   - Exibe a música que está sendo tocada no momento no canal de texto.
   - A mensagem inclui o horário e o jogo correspondente.

---

### Melhorias

1. **Logs Detalhados**:
   - Adicionados logs no terminal para exibir informações detalhadas sobre:
     - Música atual sendo tocada.
     - Jogo e clima selecionados.
     - Reinício de músicas.
     - Conexões e desconexões do bot.

2. **Manutenção de Estado**:
   - As variáveis globais `selected_game` e `selected_weather` agora são atualizadas corretamente pelos menus suspensos.
   - O comando `!play` utiliza os valores atualizados para tocar a música correta.

3. **Desconexão Automática**:
   - O bot se desconecta automaticamente do canal de voz se ficar sozinho, economizando recursos.

---

### Correções de Bugs

1. **Menus Suspensos**:
   - Corrigido o problema onde o segundo menu suspenso (clima) não era exibido corretamente.
   - Agora ambos os menus (jogo e clima) aparecem na mesma mensagem.

2. **Atualização de Variáveis**:
   - Corrigido o problema onde as seleções feitas nos menus suspensos não eram refletidas nos comandos `!play` e `!refresh`.

3. **Erro ao Reiniciar Música**:
   - Corrigido o erro que ocorria ao tentar reiniciar uma música quando o bot não estava conectado a um canal de voz.

---

### Comportamento Esperado

- O bot toca músicas baseadas no horário, jogo e clima selecionados.
- O comando `!refresh` reinicia a música atual sem interrupções.
- O comando `!select` permite selecionar o jogo e o clima de forma interativa.
- O comando `!musica` exibe a música atual no canal de texto.
- O bot se desconecta automaticamente se ficar sozinho no canal de voz.

---

### Próximos Passos

- Adicionar suporte para playlists personalizadas.
- Implementar comandos para alterar o volume da música.
- Melhorar a interface de interação com os usuários no Discord.

---

**Aproveite a nova versão!** 🎵
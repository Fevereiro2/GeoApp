# Jogo de Geografia - Quiz de Capitais

## Descrição do Projeto
Este é um jogo educativo desenvolvido para testar os conhecimentos de Geografia dos jogadores. O objetivo do jogo é desafiar os participantes a identificar as capitais de diferentes países selecionados aleatoriamente.

O programa utiliza uma interface baseada em menu e um ficheiro de texto que contém a lista de países e respetivas capitais. Além disso, permite que o jogador adicione novos países e capitais, que serão armazenados no mesmo ficheiro de texto para uso futuro.

---

## Funcionalidades
1. **Teste de Conhecimento de Geografia**  
   - O jogo apresenta países aleatórios e solicita ao jogador que digite a capital correspondente.  
   - Ao final, exibe o desempenho do jogador, por exemplo:  
     _"O jogador acertou 8 em 10 capitais."_

2. **Adicionar Novos Países e Capitais**  
   - O jogador pode inserir novos países e suas capitais.  
   - Os dados são salvos no ficheiro de texto, garantindo que estejam disponíveis para futuras sessões do jogo.

3. **Leitura e Escrita de Ficheiros**  
   - A lista de países e capitais é carregada de um ficheiro de texto no início do jogo.  
   - Novos dados inseridos pelo jogador são acrescentados ao ficheiro sem sobrescrever as informações existentes.

---

## Requisitos
- **Linguagem**: Python 3.  
- **Ficheiro de Dados**: Um ficheiro de texto no formato `.txt` para armazenar países e capitais no seguinte formato:  
  ```
  Brasil,Rio de Janeiro
  Portugal,Lisboa
  França,Paris
  ```

---

## Como Jogar
1. Execute o programa no terminal ou em um IDE Python.  
2. No menu principal, escolha uma das opções:
   - **1: Jogar**  
     Responda corretamente as capitais dos países apresentados.
   - **2: Adicionar Novo País e Capital**  
     Insira o nome de um país e a sua capital para que sejam adicionados ao ficheiro.
   - **3: Sair**  
     Encerre o jogo.

3. Após jogar, o resultado será exibido na tela indicando a quantidade de acertos e erros.

---

## Como Configurar
1. Certifique-se de ter o Python 3 instalado.  
2. Baixe ou clone o repositório do projeto.  
3. Verifique se o ficheiro de texto com a lista inicial de países e capitais está no mesmo diretório que o programa principal.  
4. Execute o programa com o comando:
   ```bash
   python jogo_geografia.py
   ```

---

## Formato do Ficheiro de Dados
- Cada linha deve conter o nome de um país e sua capital, separados por vírgula:  
  ```
  País,Capital
  ```

- Exemplo:  
  ```
  Alemanha,Berlim
  Espanha,Madrid
  Itália,Roma
  ```

---

## Exemplo de Fluxo de Jogo
1. **Menu Principal**:
   ```
   Bem-vindo ao Jogo de Geografia!
   1. Jogar
   2. Adicionar Novo País e Capital
   3. Sair
   Escolha uma opção:
   ```

2. **Durante o jogo**:
   ```
   Qual é a capital de Alemanha?
   > Berlim
   Correto!
   ```

3. **Resultado Final**:
   ```
   O jogador acertou 8 em 10 capitais.
   ```

---

## Contribuições
Contribuições para expandir a lista de países e capitais ou melhorar o código são bem-vindas. Envie sugestões ou relatórios de bugs por meio do sistema de issues.

---

## Licença
Este projeto é distribuído sob a licença MIT.  

**Divirta-se jogando e aprendendo Geografia!**

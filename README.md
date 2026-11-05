# phone-book

Lista de contatos em Python puro, com menu e saída no terminal.

## O que faz

- Mostra um menu com 5 opções:
  1. Adicionar contato (nome e telefone)
  2. Remover contato pelo nome
  3. Buscar contato pelo nome
  4. Listar todos os contatos
  5. Sair
- Não deixa cadastrar dois contatos com o mesmo nome.
- Avisa quando o contato não é encontrado ou quando a lista está vazia.

## Stack

- Python 3.6
- Nenhuma biblioteca externa

## Como rodar

    git clone https://github.com/luisfelipemaia/phone-book
    cd phone-book
    python [PREENCHER: nome do arquivo].py

## Decisões técnicas

- Os contatos ficam em uma lista de listas (`[nome, telefone]`) na memória.
- Um laço `while True` mostra o menu até o usuário escolher sair.
- A busca e a remoção comparam o nome exato, com diferença entre maiúsculas e minúsculas.

## Limitações conhecidas

- Os contatos não são salvos: ao fechar o programa, a lista se perde.
- Algumas entradas inválidas (como `6` ou letras) encerram o programa em vez de mostrar o menu de novo.

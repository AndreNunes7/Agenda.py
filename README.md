# Agenda.py

Este é um programa em Python que simula uma agenda de contatos. Ele permite adicionar, editar, buscar e excluir contatos, bem como exportar/importar contatos em formato CSV.

## Funções Principais

### `mostrar_contatos()`

Mostra todos os contatos da agenda, exibindo nome, telefone, e-mail e endereço.

### `buscar_contatos()`

Permite buscar um contato pelo nome e exibir suas informações.

### `incluir_contato()`

Solicita informações para adicionar um novo contato à agenda.

### `editar_contatos()`

Permite editar informações de um contato existente na agenda.

### `excluir_contato()`

Permite excluir um contato da agenda.

### `exportar_contatos(filename)`

Exporta os contatos da agenda para um arquivo CSV.

### `importar_contatos(filename)`

Importa contatos de um arquivo CSV para a agenda.

### `carregar()`

Carrega os contatos a partir do arquivo "database.csv".

### `imprimir_menu()`

Imprime o menu de opções para o usuário escolher.

## Uso

1. Execute o programa em Python.
2. Escolha as opções no menu para gerenciar seus contatos.
3. Siga as instruções na tela para adicionar, editar, buscar e excluir contatos.

## Pré-requisitos

- Python 3.x

## Notas

- Os contatos são armazenados em um dicionário `agenda`.
- Os dados são persistidos no arquivo "database.csv".
- Você pode expandir e personalizar o programa de acordo com suas necessidades.



# README

### Natural Language-Based Shell Command Generation and Execution Python Algorithm
## Overview
### This repository houses a Python algorithm that generates and executes shell commands based on user-provided natural language descriptions, leveraging the OpenAI API. The implementation further accommodates Linux commands for seamless execution within a Windows environment.

Features
The algorithm encompasses the following functionalities:

- Imports requisite libraries, including the OpenAI API, subprocess, and other utilities.
- Loads a .env file containing the OpenAI API key and mappings of Linux commands to their Windows counterparts.
- Defines a generate_command(text) function, utilizing the OpenAI API to generate a shell command from a provided natural language description.
- Defines an execute_command(command) function that adapts Linux commands to function on Windows (if the operating system is Windows) and executes the generated command.
- The function employs a dictionary named LINUX_TO_WINDOWS, housing mappings of select Linux commands to equivalent Windows commands. It verifies the operating system, then iterates - through the LINUX_TO_WINDOWS dictionary. If the command begins with a Linux command from the dictionary, it substitutes the equivalent Windows command.
- The approach taken in the execute_command function is more versatile and maintainable. To add additional commands and their Windows equivalencies, one need only update the LINUX_TO_WINDOWS dictionary, as opposed to manually modifying the function.
- Prompts the user for a natural language description of the desired shell command.
- Generates the shell command based on the provided description using the generate_command function.
- Prints the generated command and subsequently executes it using the execute_command function.

Usage
1. Clone the repository
2. Install the necessary dependencies (openai, python-dotenv)
3. Create a .env file with the OpenAI API key and Linux-to-Windows command mappings as required
4. Execute the Python script and provide the natural language description of the desired shell command
5. The algorithm will generate and execute the appropriate shell command


________________________________________________________
EM PORRUGUÊS

### Algoritmo Python para gerar e executar comandos shell baseado em descrições em linguagem natural.
### Este repositório contém um algoritmo em Python que gera e executa comandos shell baseados em descrições em linguagem natural fornecidas pelo usuário, usando a API OpenAI. A implementação também adapta comandos Linux para funcionar no ambiente Windows.

#### Funcionalidades
O algoritmo realiza as seguintes ações:

1. Importa bibliotecas necessárias, incluindo a API OpenAI, subprocess e outras utilidades.

2. Carrega um arquivo .env contendo a chave da API OpenAI e mapeamentos de comandos Linux para Windows.

3. Define uma função gerar_comando(texto) que usa a API OpenAI para gerar um comando shell baseado em uma descrição fornecida em linguagem natural.

4. Define uma função executar_comando(comando) que adapta comandos Linux para funcionar no Windows (caso o sistema operacional seja Windows) e executa o comando gerado.

  * A função usa um dicionário chamado LINUX_TO_WINDOWS, que contém um mapeamento de alguns comandos Linux para comandos Windows equivalentes. Ela verifica se o sistema operacional é Windows e, em seguida, itera sobre todos os itens na lista do dicionário LINUX_TO_WINDOWS. Se o comando começa com um comando Linux no dicionário, ela o substitui de forma equivalente.

  * A abordagem adotada na função executar_comando é mais genérica e fácil de manter. Para adicionar mais comandos e suas equivalências no Windows, basta atualizar o dicionário LINUX_TO_WINDOWS, em vez de modificar a função manualmente.

5. Solicita ao usuário uma descrição em linguagem natural para o comando shell desejado.

6. Gera o comando shell com base na descrição fornecida usando a função gerar_comando.

7. Imprime o comando gerado e, em seguida, executa-o usando a função executar_comando.

#### Instruções de uso
1. Clone o repositório
2. Instale as dependências necessárias (openai, python-dotenv)
3. Crie um arquivo .env com a chave da API OpenAI e mapeamentos de comandos Linux para Windows, conforme necessário
4. Execute o script Python e forneça a descrição em linguagem natural do comando shell desejado
5. O algoritmo irá gerar e executar o comando shell apropriado

### Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias ou correções de bugs.

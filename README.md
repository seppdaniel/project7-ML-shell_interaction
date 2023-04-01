# README
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

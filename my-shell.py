import openai   
import subprocess
import platform
from dotenv import load_dotenv
import os
from command_mappings import LINUX_TO_WINDOWS

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def gerar_comando(texto):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Escreva um comando shell que execute: {texto}",
        temperature=0.7,
        max_tokens=2048,
        n=1,
        stop=None
    )
    return response['choices'][0]['text'].strip()

def executar_comando(comando):
    if platform.system() == "Windows":
            for linux_cmd, windows_cmd in LINUX_TO_WINDOWS.items():
                if comando.startswith(linux_cmd):
                    comando = comando.replace(linux_cmd, windows_cmd, 1)
                    break
    try:
        resultado = subprocess.run(comando, shell=True, check=True, text=True)
        print(resultado)
    except subprocess.CalledProcessError as e:
        print(e)

descricao = input("input de descrição para comando shell: ")
comando = gerar_comando(descricao)
print(f"Comando gerado: {comando}")
executar_comando(comando)
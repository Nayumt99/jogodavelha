import sys
from cx_Freeze import setup, Executable

# Dependências adicionais podem ser necessárias, dependendo do seu script.
# Aqui, incluímos 'tkinter' porque estamos usando input() para entrada de dados.
# Se você estiver usando outras bibliotecas, certifique-se de adicioná-las aqui.
build_exe_options = {
    "includes": ["tkinter"],
}

# Defina o executável e especifique o nome do script principal (jogo_da_velha.py)
exe = Executable(
    script="jogo_da_velha.py",
    base=None,
)

setup(
    name="JogoDaVelha",
    version="0.1",
    description="Jogo da Velha em Python",
    options={"build_exe": build_exe_options},
    executables=[exe],
)

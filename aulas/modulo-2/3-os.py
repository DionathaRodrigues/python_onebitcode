import os

# Pasta atual
print(os.getcwd())

# Lista arquivos e pastas
print(os.listdir())    

# Versão do SO
os.system('sw_vers')

# Configurações da Máquina
os.system('system_profiler SPHardwareDataType')

# Limpar a tela
#os.system('clear')
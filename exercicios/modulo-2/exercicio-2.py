import os 

# Desligar o computador em 1 min
os.system('shutdown /s')

# Desligar o computador em 1 min
os.system('shutdown /s')

# Cancelar o desligamento 
#os.system('sudo shutdown -h')

def turn_off_one_hour():
    os.system('shutdown /s /t 3600')

def turn_off_half_an_hour():
    os.system('shutdown /s /t 1800')

def cancel_shutdown():
    os.system('shutdown /a')

turn_off_one_hour()
cancel_shutdown()
turn_off_half_an_hour()
cancel_shutdown()
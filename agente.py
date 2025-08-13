import time

def brute_force_simulation(password_to_guess, attempts):
    print("Iniciando simulação de ataque brute force...")
    for attempt in attempts:
        print(f"Tentando senha: {attempt}")
        time.sleep(0.5)  # simula delay de tentativa
        if attempt == password_to_guess:
            print("Senha encontrada!")
            return True
    print("Senha não encontrada.")
    return False

if __name__ == "__main__":
    # Senha “vulnerável” conhecida (exemplo)
    password = "1234"
    # Lista de tentativas (exemplo simplificado)
    password_attempts = ["0000", "1111", "1234", "9999"]

    brute_force_simulation(password, password_attempts)

import os
import time

# --- Dados do Sistema ---
destinos_disponiveis = [
    {"id": 1, "cidade": "Paris, França", "preco": 3500.00, "duracao": "7 dias"},
    {"id": 2, "cidade": "Tóquio, Japão", "preco": 5200.00, "duracao": "10 dias"},
    {"id": 3, "cidade": "Nova York, EUA", "preco": 2800.00, "duracao": "5 dias"},
    {"id": 4, "cidade": "Fernando de Noronha, Brasil", "preco": 4100.00, "duracao": "5 dias"}
]

minhas_viagens = []

# --- Funções Auxiliares ---
def limpar_tela():
    """Limpa o terminal de acordo com o sistema operacional."""
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    """Pausa a execução até o usuário pressionar Enter."""
    input("\nPressione [ENTER] para voltar ao menu principal...")

# --- Telas do Sistema ---
def exibir_destinos():
    limpar_tela()
    print("=" * 40)
    print("        DESTINOS DISPONÍVEIS")
    print("=" * 40)
    for dest in destinos_disponiveis:
        print(f"[{dest['id']}] {dest['cidade']}")
        print(f"    Preço: R$ {dest['preco']:.2f} | Duração: {dest['duracao']}")
        print("-" * 40)
    pausar()

def comprar_passagem():
    limpar_tela()
    print("=" * 40)
    print("          COMPRAR PASSAGEM")
    print("=" * 40)
    
    for dest in destinos_disponiveis:
        print(f"[{dest['id']}] {dest['cidade']} - R$ {dest['preco']:.2f}")
    
    print("\n[0] Cancelar e Voltar")
    print("=" * 40)
    
    try:
        escolha = int(input("\nDigite o ID do destino desejado: "))
        
        if escolha == 0:
            return
            
        destino_escolhido = next((d for d in destinos_disponiveis if d["id"] == escolha), None)
        
        if destino_escolhido:
            print(f"\nVocê selecionou: {destino_escolhido['cidade']}")
            confirmacao = input("Confirmar compra? (S/N): ").strip().upper()
            
            if confirmacao == 'S':
                minhas_viagens.append(destino_escolhido)
                print("\n✅ Compra realizada com sucesso! Boa viagem!")
            else:
                print("\n❌ Compra cancelada.")
        else:
            print("\n⚠️ ID inválido. Tente novamente.")
            
    except ValueError:
        print("\n⚠️ Por favor, digite um número válido.")
        
    time.sleep(2) # Pausa dramática para ler a mensagem

def listar_minhas_viagens():
    limpar_tela()
    print("=" * 40)
    print("          MINHAS VIAGENS")
    print("=" * 40)
    
    if not minhas_viagens:
        print("\nVocê ainda não comprou nenhuma passagem.")
        print("Vá em 'Comprar Passagem' para planejar sua aventura!")
    else:
        total_gasto = 0
        for i, viagem in enumerate(minhas_viagens, 1):
            print(f"{i}. {viagem['cidade']} (R$ {viagem['preco']:.2f})")
            total_gasto += viagem['preco']
        
        print("-" * 40)
        print(f"Total gasto: R$ {total_gasto:.2f}")
        
    pausar()

# --- Loop Principal ---
def menu_principal():
    while True:
        limpar_tela()
        print("=" * 40)
        print("✈️   AGÊNCIA DE VIAGENS TERMINAL   ✈️")
        print("=" * 40)
        print("1. Ver destinos disponíveis")
        print("2. Comprar passagem")
        print("3. Ver minhas viagens")
        print("4. Sair do sistema")
        print("=" * 40)
        
        opcao = input("Escolha uma opção (1-4): ").strip()
        
        if opcao == '1':
            exibir_destinos()
        elif opcao == '2':
            comprar_passagem()
        elif opcao == '3':
            listar_minhas_viagens()
        elif opcao == '4':
            limpar_tela()
            print("Obrigado por usar a Agência Terminal. Volte sempre! 🌍✈️\n")
            break
        else:
            print("\n⚠️ Opção inválida. Escolha um número entre 1 e 4.")
            time.sleep(1.5)

# --- Ponto de Entrada ---
if __name__ == "__main__":
    menu_principal()
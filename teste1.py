garrafas=[]
estoque={}
valores=[]
quantidades=[]
def add_item_estoque():
    
    garrafa= input("digite a garrafa adquirida: ")
    quantidade=int(input("digite a quantidade de garrafas adquiridas: "))
    valor= int(input("digite o valor da garrafa: "))
    garrafas.append(garrafa)
    valores.append(valor)
    quantidades.append(quantidade)
    for i in range(len(garrafas)):
     estoque[garrafas[i]] = {"valor": valores[i], "quantidade": quantidades[i]}

    for chave, valor in estoque.items():
     print(f"{chave} valor: {valor['valor']} quantidade: {valor['quantidade']}")

      
 
def registro_venda():
    chave_a_verificar = input("Digite o nome da garrafa vendida: ")
    
    if chave_a_verificar in estoque:
        quantidade_disponivel = estoque[chave_a_verificar]["quantidade"]
        print(f"A chave '{chave_a_verificar}' existe no estoque com quantidade {quantidade_disponivel}.")
        
        garrafas_retirar = int(input("Digite a quantidade de garrafas a retirar: "))
        if garrafas_retirar > quantidade_disponivel:
            print("A quantidade a retirar é maior do que a quantidade existente no estoque.")
        else:
            estoque[chave_a_verificar]["quantidade"] -= garrafas_retirar
            print(f"Foram retiradas {garrafas_retirar} '{chave_a_verificar}'. Novo estoque: {estoque[chave_a_verificar]['quantidade']}")
            for i in range(len(garrafas)):
             if chave_a_verificar == garrafas[i]:
                 quantidades[i] -= garrafas_retirar
            total=garrafas_retirar* estoque[chave_a_verificar]["valor"]
            frete=garrafas_retirar*10 + 10
            percentual = 0.1
            frete_final=total*percentual + frete
            total_final=total*frete_final
            print(f"o valor total to frete é {frete_final}\ntotal da venda {total_final} ")
            
                 
                 
               
                    


    else:
        print(f"A chave '{chave_a_verificar}' não existe no estoque.")



x=True
while True:
    op=int(input("digite\n1 para addicionar itens ao estoque\n2 para registrar saida de itens\n3 para ver o estoque\n:"))
    match op:
        case 1:
            add_item_estoque()
        case 2:
            registro_venda()
        case 3:
           for chave, valor in estoque.items():
             print(f"{chave} valor: {valor['valor']} quantidade: {valor['quantidade']}")
        case _:
            print("opção invalida")

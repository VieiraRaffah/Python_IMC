import tkinter as tk

def calcular_imc():
    try:
        nome = entrada_nome.get()
        peso = float(entrada_peso.get())
        altura = float(entrada_altura.get())
        imc = peso / (altura ** 2)
        resultado_texto = f"{nome}, seu IMC é: {imc:.2f} - {interpretar_imc(imc)}"
        resultado.config(text=resultado_texto)

        # Configurar a cor do texto com base no resultado do IMC
        if "Abaixo do peso" in resultado_texto or "Sobrepeso" in resultado_texto or "Obesidade" in resultado_texto:
            resultado.config(fg="red")
        else:
            resultado.config(fg="white")

    except ValueError:
        resultado.config(text="Por favor, insira valores válidos. \n Lembrando que não é permitido o uso da vírgula e sim do ponto. ", fg= "white")

def limpar_campos():
    entrada_nome.delete(0, tk.END)
    entrada_peso.delete(0, tk.END)
    entrada_altura.delete(0, tk.END)
    resultado.config(text="", fg="white")

def interpretar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade Grau I"
    elif 35 <= imc < 39.9:
        return "Obesidade Grau II"
    else:
        return "Obesidade Grau III"

# Configuração da janela
janela = tk.Tk()
janela.title("Calculadora IMC")
janela.geometry("350x400")
janela.configure(bg="black")  # Fundo preto

# Configuração dos widgets
rotulo_nome = tk.Label(janela, text="Nome:", bg="black", fg="white")
rotulo_nome.grid(row=0, column=0, pady=5)

entrada_nome = tk.Entry(janela)
entrada_nome.grid(row=0, column=1, pady=5)

rotulo_peso = tk.Label(janela, text="Peso (kg):", bg="black", fg="white")
rotulo_peso.grid(row=1, column=0, pady=5)

entrada_peso = tk.Entry(janela)
entrada_peso.grid(row=1, column=1, pady=5)

rotulo_altura = tk.Label(janela, text="Altura (m):", bg="black", fg="white")
rotulo_altura.grid(row=2, column=0, pady=5)

entrada_altura = tk.Entry(janela)
entrada_altura.grid(row=2, column=1, pady=5)

botao_calcular = tk.Button(janela, text="Calcular", command=calcular_imc, bg="dark olive green", fg="white")
botao_calcular.grid(row=3, column=0, columnspan=2, pady=10)

botao_limpar = tk.Button(janela, text="Limpar Campos", command=limpar_campos, bg="dark red", fg="white")
botao_limpar.grid(row=4, column=0, columnspan=2, pady=5)

resultado = tk.Label(janela, text="", bg="black", fg="white")
resultado.grid(row=5, column=0, columnspan=2, pady=5)

# Iniciar a interface gráfica
janela.mainloop()

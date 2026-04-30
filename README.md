# 🧮 Calculadora em Python com Script Shell

Projeto acadêmico cujo objetivo é desenvolver uma calculadora simples em Python, executada via script Shell no terminal.

## 📌 Funcionamento

O arquivo Calculadora.py é basicamente uma calculadora simples via terminal.

### Como funciona na prática:

Ao executar a aplicação, o usuário deverá informar dois números, em seguida, escolher a operação desejada.

A operação pode ser informada digitando o nome (ex: Soma, Subtração, Multiplicação, Divisão) ou utilizando os símbolos matemáticos (`+`, `-`, `*`, `/`).

### No código:

- **Função convertor():**
Converte valores digitados pelo usuário para int ou float, garantindo que apenas números válidos sejam utilizados.

- **Função calcular():**
Recebe dois números e uma operação, retornando o resultado com base em um dicionário de operações.

- **Loop principal (while True):**
Mantém a calculadora em execução contínua até o usuário optar por sair.

- **Tratamento de erros:**
Inclui validação de entrada e tratamento para divisão por zero.

## 🚀 Como executar o script

### 1 - Clone o repositório:

```bash
git clone https://github.com/Gabriel-lmk/calculadora_python.git
```

### 2 - Acesse a pasta do projeto no seu terminal:

```bash
cd calculadora_python
```

### 3 - Dê permissão de execução para o script .sh:

```bash
chmod 744 calculadora.sh
```

### 4 - Depois é só executar:

```bash
./calculadora.sh
```

## ❗ Observações importantes

- Este script deve ser executado em um ambiente Linux ou WSL.  
- Não é compatível com o terminal nativo do Windows.  
- Caso o Python 3 não esteja instalado, o script realiza automaticamente a instalação antes de executar a calculadora.

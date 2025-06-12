# 🔐 Testes Automatizados - Página de Login | Automation Practice

Este projeto tem como objetivo a automação de testes da página de login do site [Automation Practice](http://automationpractice.pl/index.php?controller=authentication&back=my-account), utilizando **Selenium WebDriver** e **Pytest**.

---

## 🧪 Tecnologias Utilizadas

- **Linguagem:** Python 3
- **Framework de testes:** Pytest
- **Automação Web:** Selenium WebDriver
- **Gerenciador de dependências:** `pip`
- **IDE:** VSCode

---

## 📂 Estrutura do Projeto

```
.
├── pages/
│   └── login_page.py      # Page Object Model para a página de login
├── tests/
│   └── test_login.py      # Casos de teste automatizados
├── requirements.txt        # Dependências do projeto
└── README.md               # Instruções e documentação
```

---

## ✅ Casos de Teste Automatizados

### 🧪 Cenário 1: Login com credenciais válidas

- **Dado que** o usuário esteja na página de login do site Automation Practice
- **Quando** o usuário preencher o e-mail e senha corretos e clicar em "Sign in"
- **Então** o sistema deve redirecionar o usuário para sua conta, confirmando o login com sucesso

> Resultado esperado: Redirecionamento para a URL contendo `/my-account`

---

### 🧪 Cenário 2: Login com e-mail inválido

- **Dado que** o usuário esteja na página de login do site Automation Practice
- **Quando** o usuário preencher um e-mail mal formatado (ex: `invalidemail.com`) e qualquer senha
- **Então** o sistema deve exibir a mensagem de erro: **"Invalid email address."**

---

### 🧪 Cenário 3: Login com senha incorreta

- **Dado que** o usuário esteja na página de login do site Automation Practice
- **Quando** o usuário preencher um e-mail válido e uma senha incorreta
- **Então** o sistema deve exibir a mensagem de erro: **"Authentication failed."**

---

## 🚀 Como Executar os Testes

### 1. Clonar o repositório

```bash
git clone https://github.com/seuusuario/automated-login-tests.git
cd automated-login-tests
```

### 2. Criar ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Executar os testes

```bash
pytest
```

---

## ⚙️ Requisitos para Execução

- Python 3.8+
- Google Chrome (ou outro navegador com WebDriver instalado)
- ChromeDriver (compatível com sua versão do navegador)

---

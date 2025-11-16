# Classificador Inteligente de Emails com IA (Groq + Flask)

Este projeto implementa uma solução web simples para classificar emails em categorias "Produtivo" ou "Improdutivo" e sugerir respostas automáticas, utilizando o framework Flask e a API de Inteligência Artificial da Groq.

## Estrutura do Projeto

```
.
├── app.py                  # Backend em Python (Flask)
├── requirements.txt        # Dependências do Python
├── static/
│   ├── css/
│   │   └── style.css       # Estilos CSS
│   └── js/
│       └── script.js       # Lógica JavaScript
└── templates/
    └── index.html          # Interface Web (HTML)
```

## Como Executar Localmente

### 1. Pré-requisitos

- Python 3.x
- Uma chave de API da Groq (obtenha em [https://groq.com/](https://groq.com/))

### 2. Instalação de Dependências

Instale as bibliotecas Python necessárias usando o `pip`:

```bash
pip install -r requirements.txt
```

### 3. Configuração da Chave de API

Defina a sua chave da Groq como uma variável de ambiente. Substitua `SUA_CHAVE_AQUI` pela sua chave real.

**Linux/macOS:**

```bash
export GROQ_API_KEY="SUA_CHAVE_AQUI"
```

**Windows (CMD):**

```bash
set GROQ_API_KEY="SUA_CHAVE_AQUI"
```

**Windows (PowerShell):**

```bash
$env:GROQ_API_KEY="SUA_CHAVE_AQUI"
```

### 4. Iniciar a Aplicação

Execute o script principal do Flask:

```bash
python app.py
```

A aplicação estará acessível em `http://127.0.0.1:5000`.

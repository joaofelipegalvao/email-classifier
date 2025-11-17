# 📧 Classificador Inteligente de Emails

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0-black?style=for-the-badge&logo=flask)
![Groq](https://img.shields.io/badge/Groq-Llama_3.3-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**Sistema web para classificação automática de emails usando Inteligência Artificial**

[🌐 Demo Online](https://email-classifier-b14x.onrender.com)

</div>

## 📋 Sobre o Projeto

Este projeto resolve o desafio de automatizar a triagem de emails corporativos, classificando-os em **Produtivo** (requer ação) ou **Improdutivo** (não requer ação) e sugerindo respostas automáticas.

### ✨ Funcionalidades Principais

- **Classificação Inteligente:** Utiliza a API Groq (Llama 3.3 70B) para análise de conteúdo.
- **Suporte a Múltiplos Formatos:** Aceita texto direto, upload de arquivos `.txt` e `.pdf`.
- **Interface Responsiva:** Design limpo e intuitivo para uma ótima experiência do usuário.

## 🚀 Demonstração Online

Acesse a aplicação em produção:

🌐 **Link:** <https://email-classifier-b14x.onrender.com>

> **Nota:** A aplicação pode demorar alguns segundos para iniciar devido ao _cold start_ do servidor gratuito.

## 🛠️ Tecnologias

| Tecnologia   | Descrição                               |
| ------------ | --------------------------------------- |
| **Python**   | Linguagem principal                     |
| **Flask**    | Framework web para o backend            |
| **Groq API** | Inteligência Artificial (Llama 3.3 70B) |
| **PyPDF2**   | Extração de texto de arquivos PDF       |
| **Gunicorn** | Servidor WSGI para produção             |

## 📦 Estrutura do Projeto

```
email-classifier/
├── app.py                  # Backend Flask com a lógica de IA
├── templates/
│   └── index.html          # Interface web
├── static/
│   ├── css/
│   │   └── style.css       # Estilos
│   └── js/
│       └── script.js       # Lógica do frontend
├── requirements.txt        # Dependências Python
└── README.md               # Documentação
```

## 🔧 Instalação e Execução Local

### Pré-requisitos

- Python 3.11+
- Chave de API da Groq

### Passo a Passo

**1. Clone o repositório:**

```bash
git clone https://github.com/joaofelipegalvao/email-classifier.git
cd email-classifier
```

**2. Crie um ambiente virtual:**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

**3. Instale as dependências:**

```bash
pip install -r requirements.txt
```

**4. Configure a API Key:**

Defina a sua chave da Groq como uma variável de ambiente:

```bash
export GROQ_API_KEY="SUA_CHAVE_AQUI"
```

**5. Execute a aplicação:**

```bash
python app.py
```

Acesse `http://localhost:5000` no seu navegador.

---

<div align="center">

**Desenvolvido para o desafio técnico da AutoU**

⭐ **Se gostou do projeto, deixe uma estrela!** ⭐

</div>

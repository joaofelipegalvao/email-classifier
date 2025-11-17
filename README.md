# 📧 Classificador Inteligente de Emails

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0-black?style=for-the-badge&logo=flask)
![Groq](https://img.shields.io/badge/Groq-Llama_3.3-orange?style=for-the-badge)

**Sistema web para classificação automática de emails usando Inteligência Artificial**

[🌐 Demo Online](https://email-classifier-b14x.onrender.com)

</div>

[Design-sem-nome.gif](https://postimg.cc/3d5WBNg9)

## 📋 Sobre o Projeto

Este projeto resolve o desafio de automatizar a triagem de emails corporativos, classificando-os em **Produtivo** (requer ação) ou **Improdutivo** (não requer ação) e sugerindo respostas automáticas.

### ✨ Funcionalidades Principais

- **Classificação Inteligente:** Utiliza a API Groq (Llama 3.3 70B) para análise de conteúdo
- **Suporte a Múltiplos Formatos:** Aceita texto direto, upload de arquivos `.txt` e `.pdf`
- **Interface Responsiva:** Design limpo e intuitivo para uma ótima experiência do usuário
- **Respostas Automáticas:** Gera respostas contextualizadas e profissionais
- **Deploy em Produção:** Hospedado e acessível publicamente

---

## 🚀 Demonstração Online

Acesse a aplicação em produção:

🌐 **Link:** <https://email-classifier-b14x.onrender.com>

> **Nota:** A aplicação pode demorar ~30 segundos na primeira requisição devido ao _cold start_ do servidor gratuito (plano free do Render).

---

## 🛠️ Tecnologias

| Tecnologia   | Versão | Descrição                               |
| ------------ | ------ | --------------------------------------- |
| **Python**   | 3.11+  | Linguagem principal                     |
| **Flask**    | 3.0.0  | Framework web para o backend            |
| **Groq API** | -      | Inteligência Artificial (Llama 3.3 70B) |
| **PyPDF2**   | 3.0.1  | Extração de texto de arquivos PDF       |
| **Gunicorn** | 21.2.0 | Servidor WSGI para produção             |

---

## 📦 Estrutura do Projeto

```
email-classifier/
├── app.py                # Backend Flask com a lógica de IA
├── emails_teste.txt      # Exemplos de emails para teste
├── README.md             # Documentação do projeto
├── requirements.txt      # Dependências Python
├── static/               # Arquivos estáticos (CSS, JS, imagens)
│ ├── css/
│ │ └── style.css         # Estilos da interface
│ └── js/
│ └── script.js           # Lógica do frontend
└── templates/
└── index.html            # Interface web (HTML/CSS/JS)
```

---

## 🔧 Instalação e Execução Local

### Pré-requisitos

- Python 3.11 ou superior
- Conta na Groq para obter API Key ([console.groq.com](https://console.groq.com))

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

Obtenha sua chave gratuita em [console.groq.com](https://console.groq.com) e configure como variável de ambiente:

```bash
# Linux/Mac
export GROQ_API_KEY="sua_chave_aqui"

# Windows (CMD)
set GROQ_API_KEY=sua_chave_aqui

# Windows (PowerShell)
$env:GROQ_API_KEY="sua_chave_aqui"
```

**5. Execute a aplicação:**

```bash
python app.py
```

**6. Acesse no navegador:**

```
http://localhost:5000
```

---

## 📖 Como Usar

### 1. Acesse a Aplicação

Abra <https://email-classifier-b14x.onrender.com> no navegador

### 2. Escolha o Método de Entrada

**Opção A - Colar Texto Direto:**

- Clique na aba "Colar Texto"
- Cole o conteúdo do email
- Clique em "Classificar Email"

**Opção B - Upload de Arquivo:**

- Clique na aba "Upload de Arquivo"
- Arraste ou selecione um arquivo `.txt` ou `.pdf`
- Clique em "Classificar Email"

### 3. Visualize os Resultados

O sistema exibirá:

- ✅ **Classificação** (Produtivo ou Improdutivo)
- ✅ **Nível de Confiança** (0-100%)
- ✅ **Prévia do Email**
- ✅ **Resposta Sugerida** (gerada pela IA)
- ✅ **Justificativa** da classificação

---

## 🧪 Exemplos de Teste

### Email Produtivo

Copie e cole este exemplo na aplicação:

```
Assunto: Urgente - Sistema Fora do Ar

Prezada equipe de TI,

O sistema de pagamentos está apresentando erro 502 desde 14h30.
Já tentamos reiniciar mas o problema persiste.

Precisamos de ajuda urgente!

João Silva - Gerente de Operações
```

**Resultado Esperado:**

- Classificação: **Produtivo**
- Confiança: ~95%
- Resposta: Profissional e urgente

---

### Email Improdutivo

Copie e cole este exemplo na aplicação:

```
Assunto: Feliz Natal!

Olá pessoal,

Desejo a todos um Feliz Natal e um próspero Ano Novo!
Aproveitem as festas!

Abraços,
Maria Santos
```

**Resultado Esperado:**

- Classificação: **Improdutivo**
- Confiança: ~98%
- Resposta: Cordial e social

---

### 📁 Arquivo de Teste

Para facilitar, incluímos o arquivo **[emails_teste.txt](emails_teste.txt)** com 6 exemplos prontos:

- 4 emails produtivos (solicitações, problemas técnicos, dúvidas)
- 2 emails improdutivos (felicitações, agradecimentos)

**Como usar:**

1. Baixe o arquivo `emails_teste.txt`
2. Na aplicação, clique em "Upload de Arquivo"
3. Selecione o arquivo
4. Clique em "Classificar Email"

---

## 🏗️ Arquitetura

```
┌─────────────┐
│   Browser   │  (Interface Web - HTML/CSS/JS)
└──────┬──────┘
       │ HTTP Request (POST /api/classify)
       ▼
┌─────────────┐
│ Flask Server│  (Backend Python - app.py)
└──────┬──────┘
       │ API Call (Prompt + Email)
       ▼
┌─────────────┐
│  Groq API   │  (Llama 3.3 70B - IA)
└──────┬──────┘
       │ JSON Response (Classificação + Resposta)
       ▼
┌─────────────┐
│   Results   │  (Exibido na Interface)
└─────────────┘
```

### Fluxo de Processamento

1. **Usuário** submete email (texto ou arquivo)
2. **Flask** valida e processa a entrada
3. **PyPDF2** extrai texto (se for PDF)
4. **Flask** envia prompt estruturado para Groq
5. **Llama 3.3** analisa contexto e classifica
6. **API** retorna JSON com classificação + resposta
7. **Frontend** exibe resultados formatados

---

## 🔐 Segurança

Boas práticas implementadas:

- ✅ **API Keys** armazenadas como variáveis de ambiente
- ✅ **Validação** de tipos de arquivo permitidos
- ✅ **Timeout** de 30 segundos para requisições
- ✅ **Sanitização** de entrada de dados
- ✅ **Tratamento** robusto de erros
- ✅ **CORS** configurado adequadamente

---

## 👤 Autor

**João Felipe Galvão**

- 💼 LinkedIn: [joaofelipegalvao](https://linkedin.com/in/joaofelipegalvao)
- 📧 Email: <joaofelipe.galvao021@gmail.com>

---

<div align="center">

**Desenvolvido com ❤️ para o desafio técnico da AutoU**

**Classificador Inteligente de Emails - Automatizando triagem com IA**

⭐ **Se gostou do projeto, deixe uma estrela!** ⭐

[⬆ Voltar ao topo](#-classificador-inteligente-de-emails)

</div>

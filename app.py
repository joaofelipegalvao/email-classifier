import json
import os
import re
from io import BytesIO

import PyPDF2
import requests
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Pega chave da API Groq
GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")


def extract_text_from_pdf(file_content):
    """Extrai texto de PDF"""
    try:
        pdf_reader = PyPDF2.PdfReader(BytesIO(file_content))
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text.strip() if text else ""
    except Exception as e:
        return f"Erro ao processar PDF: {str(e)}"


def classify_and_respond(email_text):
    """Classifica email e gera resposta usando Groq"""

    if not GROQ_API_KEY:
        return {
            "classification": "Erro",
            "confidence": 0.0,
            "response": "Configure a variável GROQ_API_KEY nas configurações do servidor.",
            "reasoning": "API key não configurada",
        }

    # Prompt enviado ao modelo
    prompt = f"""Analise o seguinte email e classifique-o como "Produtivo" ou "Improdutivo".

Email:
---
{email_text}
---

Produtivo = requer ação, resposta ou contém solicitações importantes
Improdutivo = mensagens sociais, felicitações, agradecimentos sem necessidade de ação

Retorne APENAS um objeto JSON válido no formato:
{{
  "classification": "Produtivo" ou "Improdutivo",
  "confidence": número entre 0 e 1,
  "response": "resposta automática sugerida em português, profissional e contextualizada",
  "reasoning": "breve explicação da classificação"
}}"""

    try:
        # Chamada à API Groq com timeout
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": "llama-3.3-70b-versatile",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.2,
                "max_tokens": 1000,
            },
            timeout=30,
        )

        # Verifica status HTTP
        if response.status_code != 200:
            return {
                "classification": "Erro",
                "confidence": 0.0,
                "response": "Erro ao comunicar com a API de IA.",
                "reasoning": f"Status HTTP: {response.status_code}",
            }

        data = response.json()

        # Verifica erro na resposta
        if "error" in data:
            error_msg = data["error"].get("message", "Erro desconhecido")
            return {
                "classification": "Erro",
                "confidence": 0.0,
                "response": "Não foi possível classificar o email.",
                "reasoning": error_msg,
            }

        # Pega a mensagem retornada
        ai_msg = data.get("choices", [{}])[0].get("message", {}).get("content", "")

        if not ai_msg:
            raise ValueError("Resposta vazia da API")

    except requests.exceptions.Timeout:
        return {
            "classification": "Erro",
            "confidence": 0.0,
            "response": "Tempo de resposta excedido.",
            "reasoning": "A API demorou muito para responder",
        }
    except requests.exceptions.RequestException as e:
        return {
            "classification": "Erro",
            "confidence": 0.0,
            "response": "Erro de conexão com a API.",
            "reasoning": f"Erro de rede: {str(e)}",
        }
    except Exception as e:
        return {
            "classification": "Erro",
            "confidence": 0.0,
            "response": "Erro inesperado ao processar.",
            "reasoning": f"Erro: {str(e)}",
        }

    # Tenta interpretar o JSON retornado pelo modelo
    try:
        # Remove markdown code blocks se existirem
        cleaned = ai_msg.strip()
        cleaned = re.sub(r"```json\s*", "", cleaned)
        cleaned = re.sub(r"```\s*", "", cleaned)
        cleaned = cleaned.strip()

        # Tenta extrair JSON do texto
        json_match = re.search(r"\{.*\}", cleaned, flags=re.DOTALL)
        if json_match:
            cleaned = json_match.group(0)

        result = json.loads(cleaned)

        # Validação dos campos obrigatórios
        if "classification" not in result:
            result["classification"] = "Improdutivo"

        if "confidence" not in result:
            result["confidence"] = 0.7

        if "response" not in result:
            result["response"] = "Obrigado pelo contato. Retornaremos em breve."

        if "reasoning" not in result:
            result["reasoning"] = "Análise automática"

        # Garantir que confidence está entre 0 e 1
        result["confidence"] = max(0.0, min(1.0, float(result["confidence"])))

        return result

    except json.JSONDecodeError as e:
        # Fallback caso não consiga parsear o JSON
        return {
            "classification": "Improdutivo",
            "confidence": 0.6,
            "response": "Obrigado pelo contato. Retornaremos em breve.",
            "reasoning": f"Resposta automática (erro ao processar: {str(e)})",
        }
    except Exception as e:
        return {
            "classification": "Erro",
            "confidence": 0.0,
            "response": "Erro ao processar resposta da IA.",
            "reasoning": f"Erro inesperado: {str(e)}",
        }


@app.route("/")
def index():
    """Página principal"""
    return render_template("index.html")


@app.route("/api/classify", methods=["POST"])
def classify_email():
    """Endpoint para classificação de emails"""

    email_text = ""

    # Verifica se é texto direto
    if request.form.get("email_text"):
        email_text = request.form.get("email_text")

    # Verifica se é upload de arquivo
    elif "file" in request.files:
        file = request.files["file"]

        if not file or file.filename == "":
            return jsonify({"error": "Nenhum arquivo selecionado"}), 400

        filename = file.filename.lower()

        if filename.endswith(".txt"):
            try:
                email_text = file.read().decode("utf-8")
            except UnicodeDecodeError:
                return (
                    jsonify(
                        {"error": "Erro ao ler arquivo .txt. Verifique o encoding."}
                    ),
                    400,
                )

        elif filename.endswith(".pdf"):
            email_text = extract_text_from_pdf(file.read())

            # Verifica se houve erro na extração
            if email_text.startswith("Erro ao processar PDF:"):
                return jsonify({"error": email_text}), 400

        else:
            return jsonify({"error": "Formato não suportado. Use .txt ou .pdf"}), 400

    else:
        return jsonify({"error": "Nenhum email fornecido"}), 400

    # Valida se o email não está vazio
    if not email_text or not email_text.strip():
        return jsonify({"error": "Email vazio ou sem conteúdo válido"}), 400

    # Limita tamanho do email (10.000 caracteres)
    if len(email_text) > 10000:
        email_text = email_text[:10000]

    # Classifica o email
    result = classify_and_respond(email_text)

    # Retorna resultado
    return jsonify(
        {
            "success": True,
            "email_preview": email_text[:200]
            + ("..." if len(email_text) > 200 else ""),
            "classification": result.get("classification", "Desconhecido"),
            "confidence": result.get("confidence", 0.0),
            "suggested_response": result.get("response", "Erro ao gerar resposta"),
            "reasoning": result.get("reasoning", "Sem justificativa disponível"),
        }
    )


@app.route("/api/health", methods=["GET"])
def health():
    """Health check endpoint"""
    return jsonify(
        {
            "status": "healthy",
            "api_configured": bool(GROQ_API_KEY),
            "api_provider": "Groq (Llama 3.3)",
        }
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_ENV") != "production"
    app.run(host="0.0.0.0", port=port, debug=debug)

let currentTab = "text";
let selectedFile = null;

function switchTab(tab, event) {
  currentTab = tab;

  document
    .querySelectorAll(".tab")
    .forEach((t) => t.classList.remove("active"));
  event.target.closest(".tab").classList.add("active");

  document
    .querySelectorAll(".tab-content")
    .forEach((c) => c.classList.remove("active"));
  document.getElementById(tab + "-tab").classList.add("active");

  hideError();
}

const fileUpload = document.getElementById("file-upload");
const fileInput = document.getElementById("file-input");
const fileName = document.getElementById("file-name");

fileUpload.addEventListener("click", () => fileInput.click());

fileUpload.addEventListener("dragover", (e) => {
  e.preventDefault();
  fileUpload.classList.add("drag-over");
});

fileUpload.addEventListener("dragleave", () => {
  fileUpload.classList.remove("drag-over");
});

fileUpload.addEventListener("drop", (e) => {
  e.preventDefault();
  fileUpload.classList.remove("drag-over");
  const files = e.dataTransfer.files;
  if (files.length > 0) {
    handleFile(files[0]);
  }
});

fileInput.addEventListener("change", (e) => {
  if (e.target.files.length > 0) {
    handleFile(e.target.files[0]);
  }
});

function handleFile(file) {
  const validTypes = [".txt", ".pdf"];
  const fileExt = "." + file.name.split(".").pop().toLowerCase();

  if (!validTypes.includes(fileExt)) {
    showError("Formato não suportado. Use .txt ou .pdf");
    return;
  }

  selectedFile = file;
  fileName.innerHTML = `<svg style="width:16px;height:16px;display:inline;vertical-align:middle;margin-right:6px" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>Arquivo selecionado: ${file.name}`;
  hideError();
}

function showError(message) {
  const errorDiv = document.getElementById("error-message");
  errorDiv.textContent = message;
  errorDiv.classList.add("show");
}

function hideError() {
  document.getElementById("error-message").classList.remove("show");
}

async function classifyEmail() {
  hideError();

  const formData = new FormData();

  if (currentTab === "text") {
    const emailText = document.getElementById("email-text").value.trim();
    if (!emailText) {
      showError("Por favor, cole o conteúdo do email.");
      return;
    }
    formData.append("email_text", emailText);
  } else {
    if (!selectedFile) {
      showError("Por favor, selecione um arquivo.");
      return;
    }
    formData.append("file", selectedFile);
  }

  document.getElementById("results").classList.remove("show");
  document.getElementById("loading").classList.add("show");
  document.getElementById("classify-btn").disabled = true;

  try {
    const response = await fetch("/api/classify", {
      method: "POST",
      body: formData,
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.error || "Erro ao processar email");
    }

    displayResults(data);
  } catch (error) {
    showError("Erro: " + error.message);
  } finally {
    document.getElementById("loading").classList.remove("show");
    document.getElementById("classify-btn").disabled = false;
  }
}

function displayResults(data) {
  const resultsDiv = document.getElementById("results");
  const headerDiv = document.getElementById("result-header");

  const isProdutivo = data.classification === "Produtivo";
  headerDiv.className =
    "result-header " + (isProdutivo ? "produtivo" : "improdutivo");

  const iconSvg = isProdutivo
    ? '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>'
    : '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>';

  document.getElementById("result-icon").innerHTML = iconSvg;
  document.getElementById("classification-title").textContent =
    data.classification;
  document.getElementById("confidence").textContent =
    `Confiança: ${(data.confidence * 100).toFixed(0)}%`;

  document.getElementById("email-preview").textContent = data.email_preview;
  document.getElementById("suggested-response").textContent =
    data.suggested_response;
  document.getElementById("reasoning").textContent =
    data.reasoning || "Análise automática por IA";

  resultsDiv.classList.add("show");
  resultsDiv.scrollIntoView({ behavior: "smooth", block: "nearest" });
}

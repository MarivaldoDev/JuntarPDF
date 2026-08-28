# Juntar PDFs
 
https://github.com/user-attachments/assets/2cc76ea3-f7ee-4c9f-b6c2-532aa4acfde5


Aplicativo desktop simples e intuitivo para **unir vários arquivos PDF em um único documento**, permitindo organizar a ordem dos arquivos antes da mesclagem.

## Sobre o projeto

O **Juntar PDFs** foi desenvolvido para facilitar a combinação de vários documentos PDF em um único arquivo.

A aplicação permite selecionar diversos PDFs, visualizar os arquivos escolhidos em uma lista, reorganizar a ordem dos documentos e, ao final, gerar um novo PDF com o conteúdo na sequência definida pelo usuário.

Os arquivos originais **não são modificados**. A aplicação apenas lê os documentos selecionados e cria um novo arquivo com o resultado.


## Como funciona

O fluxo é simples:

```text
Selecionar PDFs
      ↓
Organizar a ordem
      ↓
Mesclar documentos
      ↓
Escolher onde salvar
      ↓
Novo PDF
```

### Exemplo

Se você selecionar:

```text
01 - Capa.pdf
02 - Documento.pdf
03 - Comprovante.pdf
```

e essa for a ordem exibida na aplicação, o resultado será um único arquivo contendo:

```text
Capa
  ↓
Documento
  ↓
Comprovante
```


## Funcionalidades

* 📄 Selecionar vários arquivos `.pdf` de uma vez.
* 🔢 Visualizar os arquivos selecionados em uma lista numerada.
* ⬆️ Mover documentos para cima na lista.
* ⬇️ Mover documentos para baixo na lista.
* ❌ Remover arquivos individualmente.
* 🧹 Limpar toda a lista de arquivos.
* 📑 Mesclar os PDFs na ordem definida pelo usuário.
* 💾 Escolher o nome e o local do arquivo final.
* 🔒 Preservar os arquivos originais.
* ♻️ Evitar que o mesmo arquivo seja adicionado mais de uma vez durante a mesma operação.
* 🖥️ Disponibiliza um instalador para Windows.


## Download para Windows

### Instalação rápida

Se você utiliza Windows, **não precisa instalar Python nem configurar o ambiente de desenvolvimento**.

A versão pronta para uso está disponível nas **Releases** do projeto.

Baixe o arquivo:

```text
JuntarPDFs-Setup.exe
```

Execute o instalador e siga as instruções apresentadas pelo Windows.

O instalador configura automaticamente a aplicação e cria os atalhos necessários.

> **Recomendação:** para usuários comuns, utilize o instalador `.exe` disponível na Release. O código-fonte e as instruções de desenvolvimento abaixo são destinados principalmente a quem deseja executar ou contribuir com o projeto.


## Execução local

Para executar o projeto a partir do código-fonte, você precisará de:

* Python **3.13 ou superior**;
* Ambiente gráfico compatível com Tkinter;
* [uv](https://docs.astral.sh/uv/) para gerenciamento do ambiente e dependências.

### 1. Clone o repositório

```bash
git clone https://github.com/MarivaldoDev/JuntarPDF
cd JuntarPDFS
```

### 2. Instale as dependências

Com `uv`:

```bash
uv sync
```

### 3. Execute a aplicação

```bash
uv run python main.py
```

## Executando sem `uv`

Também é possível utilizar um ambiente virtual tradicional:

### Linux/macOS

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
python main.py
```

### Windows PowerShell

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -e .
python main.py
```


## Solução de problemas

### A aplicação não inicia

Verifique se está utilizando Python 3.13 ou superior e se as dependências foram instaladas:

```bash
uv sync
uv run python main.py
```

### Um PDF não pode ser mesclado

Verifique se o arquivo:

* não está corrompido;
* não está protegido por senha;
* não está sendo utilizado por outro programa.

A aplicação informa o erro retornado pelo `pikepdf`.


## Tecnologias utilizadas

* **Python**
* **CustomTkinter** — interface gráfica
* **CTkMessagebox** — mensagens da aplicação
* **pikepdf** — manipulação dos arquivos PDF
* **PyInstaller** — geração do executável Windows
* **Inno Setup** — criação do instalador Windows
* **uv** — gerenciamento do ambiente e dependências
* **GitHub Actions** — automação do build e distribuição


## Licença

Este projeto está disponível sob a [licença MIT](LICENSE).

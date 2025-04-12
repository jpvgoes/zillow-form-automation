# Zillow Clone Form Automation

## Descrição do Projeto

Este projeto automatiza o processo de preenchimento de um formulário do Google Forms com informações extraídas de um site de imóveis. Ele utiliza as bibliotecas **BeautifulSoup** e **Selenium** para realizar as seguintes etapas:

![Demo do Projeto](https://github.com/jpvgoes/zillow-form-automation/blob/main/Gravando2025-04-12140141-ezgif.com-optimize.gif)



1. **Extração de Dados**:
   - Acessa o site [Zillow Clone](https://appbrewery.github.io/Zillow-Clone/) para coletar informações sobre imóveis.
   - Extrai os seguintes dados:
     - **Endereços** dos imóveis.
     - **Preços** dos imóveis.
     - **Links** para as páginas dos imóveis.

2. **Preenchimento Automático do Formulário**:
   - Abre o formulário do Google Forms especificado.
   - Preenche os campos do formulário com os dados extraídos.
   - Envia o formulário para cada imóvel coletado.

## Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto.
- **BeautifulSoup**: Para realizar o web scraping e extrair dados do site.
- **Selenium**: Para automação do navegador e preenchimento do formulário.
- **Google Chrome**: Navegador utilizado para a automação.

## Como Executar o Projeto

### Pré-requisitos

1. **Instalar o Python**:
   - Certifique-se de que o Python está instalado em sua máquina. Você pode baixá-lo em [python.org](https://www.python.org/).

2. **Instalar as Dependências**:
   - Execute o seguinte comando para instalar as bibliotecas necessárias:
     ```bash
     pip install selenium beautifulsoup4 requests
     ```

3. **Configurar o WebDriver**:
   - Baixe o [ChromeDriver](https://chromedriver.chromium.org/) compatível com a versão do seu navegador Google Chrome.
   - Adicione o executável do ChromeDriver ao PATH do sistema.

### Executando o Projeto

1. Clone ou baixe este repositório.
2. Navegue até o diretório do projeto.
3. Execute o script `main.py`:
   ```bash
   python main.py

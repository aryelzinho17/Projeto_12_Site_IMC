# Projeto 12: Site de Cálculo de IMC 🏋️‍♂️
---
## O Cenário 👨‍💼

Você é a nova pessoa desenvolvedora na "HealthPy", uma startup de tecnologia focada em criar ferramentas simples e úteis para a saúde e bem-estar.

Sua primeira tarefa é desenvolver o produto principal da empresa: uma calculadora de IMC (Índice de Massa Corporal) online. A ferramenta precisa ser rápida, intuitiva e fornecer um feedback imediato ao usuário. Este projeto é a oportunidade perfeita para você conectar suas habilidades de backend com Flask à criação de uma experiência interativa para o usuário no frontend com HTML.

### 💡 Qual é a fórmula do IMC?

A fórmula é: **IMC = Peso (kg) / [Altura (m)]²**

As categorias gerais são:

  * **Abaixo de 18.5:** Abaixo do peso
  * **18.5 a 24.9:** Peso normal
  * **25.0 a 29.9:** Sobrepeso
  * **30.0 e acima:** Obesidade

## 📋 Requisitos da Missão

O CEO da HealthPy precisa de um protótipo funcional para apresentar aos investidores. Seu site deve atender aos seguintes requisitos:

1.  **Interface Web (Frontend):** Crie uma página principal (`index.html`) com um formulário simples. O formulário deve ter:

      * Um campo para o usuário inserir o **Peso em quilogramas (kg)**.
      * Um campo para o usuário inserir a **Altura em centímetros (cm)**.
      * Um botão "Calcular".

2.  **Servidor Web (Backend):** Utilize o Flask para criar o servidor que irá hospedar e processar a aplicação.

3.  **Rota Principal (`/`):** Crie uma rota principal que exiba a página da calculadora (`index.html`).

4.  **Rota de Cálculo (`/calcular`):** Crie uma segunda rota que:

      * Receba os dados (`peso` e `altura`) enviados pelo formulário via método **POST**.
      * Realize a lógica de cálculo do IMC.
      * Determine em qual categoria o resultado se encaixa.

5.  **Página de Resultado:** A rota `/calcular` deve renderizar uma nova página (`resultado.html`) que exiba claramente para o usuário:

      * O valor do IMC calculado (formatado com 2 casas decimais).
      * A classificação correspondente (ex: "Peso normal").

## 💡 Roteiro Sugerido para o Sucesso

1.  **Estrutura do Projeto**: Crie sua pasta de projeto. Dentro dela, crie seu arquivo Python (ex: `app.py`) e uma pasta chamada `templates`.
2.  **Importe as Ferramentas**: No `app.py`, comece importando o necessário do Flask: `from flask import Flask, render_template, request`.
3.  **Crie a Página Principal**: Dentro da pasta `templates`, crie o arquivo `index.html`. Nele, construa um formulário HTML simples:
    ```html
    <form action="/calcular" method="post">
        <input type="text" name="peso" placeholder="Peso (kg)">
        <input type="text" name="altura" placeholder="Altura (cm)">
        <button type="submit">Calcular</button>
    </form>
    ```
4.  **Configure as Rotas no Flask**:
      * Crie a instância do Flask: `app = Flask(__name__)`.
      * Crie a rota principal que apenas mostra o formulário:
        ```python
        @app.route('/')
        def index():
            return render_template('index.html')
        ```
5.  **Implemente a Lógica de Cálculo**: Crie a rota `/calcular`:
    ```python
    @app.route('/calcular', methods=['POST'])
    def calcular():
        peso = float(request.form['peso'])
        altura_cm = float(request.form['altura'])
        
        # Lógica para converter altura e calcular IMC
        altura_m = altura_cm / 100
        imc = peso / (altura_m ** 2)
        
        # Lógica if/elif/else para encontrar a classificação
        if imc < 18.5:
            classificacao = "Abaixo do peso"
        # ... continue as outras condições
        
        # Renderize a página de resultado passando os dados
        return render_template('resultado.html', imc=f'{imc:.2f}', classificacao=classificacao)
    ```
6.  **Crie a Página de Resultado**: Na pasta `templates`, crie `resultado.html`. Use as variáveis passadas pelo Flask para mostrar os dados:
    ```html
    <h1>Seu Resultado</h1>
    <p>Seu IMC é: {{ imc }}</p>
    <p>Classificação: {{ classificacao }}</p>
    ```
6. **Capriche no FRONT-END\!** Lembre-se que é seu primeiro dia e você precisa impressionar seus gestores. 
7.  **Execute e Teste**: Rode seu `app.py` e teste a calculadora no navegador\!
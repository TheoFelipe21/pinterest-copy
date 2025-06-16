# Pinterest Clone

Este projeto é uma cópia do Pinterest desenvolvida com Python, Flask, HTML e CSS. A aplicação permite que usuários criem contas, façam login, publiquem imagens, visualizem um feed de postagens e acessem perfis personalizados. O gerenciamento do banco de dados é feito com SQLAlchemy.

## Estrutura do Projeto

```
.
├── pinterest/
│ ├── static/
│ │ ├── fotos_post/
│ │ └── fotos_site/
│ │  ├── default.jpg
│ │  ├── fundo-login.png
│ │ └── style.css
│ ├── templates/
│ │ ├── criarconta.html
│ │ ├── feed.html
│ │ ├── home.html
│ │ ├── navbar.html
│ │ └── perfil.html
│ ├── __init__.py
│ ├── forms.py
│ ├── models.py
│ └── routes.py
│
├── venv/
│
├── .gitignore
├── main.py
├── readme.md
└── requirements


## Descrição dos principais diretórios e arquivos

- **pinterest/static/**: Arquivos estáticos como imagens e CSS.
- **pinterest/templates/**: Templates HTML do projeto.
- **pinterest/forms.py**: Formulários utilizados na aplicação.
- **pinterest/models.py**: Modelos de dados e classes do banco.
- **pinterest/routes.py**: Rotas e views da aplicação.
- **\_\_init\_\_.py**: Inicialização do app Flask.
- **venv/**: Ambiente virtual Python.
- **main.py**: Arquivo principal para execução da aplicação.
- **requirements**: Dependências do projeto.
- **.gitignore**: Arquivos e pastas ignorados pelo Git.
- **readme.md**: Documentação do projeto.
```

## Funcionalidades

- Cadastro e login de usuários
- Visualização e edição de perfil
- Feed de postagens
- Interface responsiva com HTML e CSS customizados

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements
   ```

## Como executar

Execute o arquivo principal:
```bash
python main.py
```

Acesse a aplicação no navegador pelo endereço:
```
http://127.0.0.1:5000
```

## Licença

Este projeto está sob a licença [MIT](LICENSE).

---

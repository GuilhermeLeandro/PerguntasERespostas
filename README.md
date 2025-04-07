# Gerenciador de Perguntas

Este é um projeto de Gerenciador de Perguntas desenvolvido em Python utilizando o framework PyQt5 para a interface gráfica. O objetivo do projeto é permitir o cadastro, edição e revisão de perguntas e respostas.

## Requisitos

- Python 3.8+
- PyQt5

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/SeuUsuario/gerenciador-de-perguntas.git
    cd gerenciador-de-perguntas
    ```

2. Crie um ambiente virtual e ative-o:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

Para iniciar a aplicação, execute o seguinte comando:
```bash
python main.py
```
## Estrutura do Projeto

- `main.py`: Arquivo principal que inicia a aplicação.
- `views/main_view.py`: Contém a classe `MainView` que define a interface principal do gerenciador.
- `views/edit_view.py`: Contém a classe `EditView` que define a interface de edição de perguntas.
- `views/review_view.py`: Contém a classe `ReviewView` que define a interface de revisão de perguntas.
- `models/perguntas.py`: Contém a classe `Pergunta` que define o modelo de dados para as perguntas.
- `storage.py`: Contém a classe `Storage` responsável pelo carregamento e salvamento das perguntas.

## Funcionalidades

- **Cadastro de Perguntas**: Permite cadastrar novas perguntas com suas respectivas respostas e explicações.
- **Edição de Perguntas**: Permite editar perguntas já cadastradas.
- **Revisão de Perguntas**: Permite revisar perguntas cadastradas e verificar se precisam de revisão com base na última data de revisão.

## Contribuição

1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`).
4. Faça um push para a branch (`git push origin feature/nova-feature`).
5. Crie um novo Pull Request.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
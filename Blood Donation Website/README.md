
# Projeto de Doação de Sangue

Este projeto tem como objetivo criar um sistema para gerenciar doações de sangue. Ele utiliza o framework Django e o pacote Crispy-forms.

## Requisitos

- Python
- Pip (gerenciador de pacotes do Python)

## Instalação

1. Crie uma pasta para o projeto e navegue até ela no terminal.
2. Crie uma máquina virtual usando o comando: `python -m venv .venv`
3. Ative a máquina virtual usando o comando:
   - No Windows: `.venv\Scripts\activate`
   - No Linux: `source .venv/bin/activate`
4. Instale o Django usando o comando: `pip install django`
5. Instale o Django Rest Framework usando o comando: `pip install djangorestframework`
6. Instale o Crispy-forms usando o comando: `pip install django-crispy-forms`
7. Navegue até a pasta do projeto usando o comando: `cd server`
8. Crie um superusuário para o sistema usando o comando: `python manage.py createsuperuser`
9. Siga as instruções para a criação do usuário 
10. Inicie o servidor de desenvolvimento usando o comando: `python manage.py runserver`
11. Acesse o endereço fornecido (geralmente http://127.0.0.1:8000/) para ver o sistema em execução.

## Testes

Para testar a API, acesse o painel de administração do Django (http://127.0.0.1:8000/admin/) e faça login com suas credenciais de superusuário.

Para testar o sistema completo, acesse o endereço fornecido (geralmente http://127.0.0.1:8000)

# 1 - criar pasta do projeto

# Criar venv
python3 -m venv .venv

# Ativar .venv
sourece .venv/bin/activate

# Instala Django
pip install django

# Criar estrutura do projeto
dajngo-admin starproject setup .

# Rodar projeto
python manage.py runserver

# Criar App
python manage.py startapp "nomedaapp" 

# criar tabela no banco de dados
python manage.py makemigrations
python manage.py migrate

# Ocultar 
pip install python-decouple

# Protejer banco de dados oculando
pip install dj-database-url

# Biblioteca que ajuda na orgarnização do código
pip install black
black . execulta o black
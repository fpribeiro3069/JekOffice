# JekOffice
Projeto Interno de gestão da jeKnowledge

# Instalação
git clone <url>
cd <pasta_do_repositorio>
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd jekoffice
python manage.py migrate
python manage.py runserver

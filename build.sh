#!/usr/bin/env bash
# exit on error
set -o errexit

# atualiza o pip
/opt/render/project/src/.venv/bin/python3.9 -m pip install --upgrade pip

# instala as dependencias
pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
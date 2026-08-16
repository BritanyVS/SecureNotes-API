
Activar: .\.venv\Scripts\Activate.ps1
Desactivar: deactivate
Correr: python run.py

//Volver a instalar dependencias
python -m pip install -r requirements.txt


//Dependencias
blinker==1.9.0
click==8.3.2 #8.4.2
colorama==0.4.6
Flask==3.1.3
itsdangerous==2.2.0
Jinja2==3.1.5 #3.1.6
MarkupSafe==3.0.3 
Werkzeug==3.1.5 #3.1.8

pip install --upgrade jinja2==3.1.6 werkzeug==3.1.6 click==8.3.3

snyk container test securenotes-api:latest --file=Dockerfile


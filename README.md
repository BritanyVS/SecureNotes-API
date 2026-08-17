
Activar: .\.venv\Scripts\Activate.ps1
Desactivar: deactivate
Correr: python run.py

//Volver a instalar dependencias
python -m pip install -r requirements.txt




--Testear Open Source
snyk test --file=requirements.txt
pip install Jinja2==3.1.2
pip install --upgrade Jinja2==3.1.6

--si fallará 
pip install -r requirements.txt

--Testear Code
Snyk code test



--Testear Containers
snyk container test securenotes-api:latest --file=Dockerfile


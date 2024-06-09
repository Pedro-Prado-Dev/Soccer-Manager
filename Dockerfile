# Usando imagem base do Python
FROM python:3.11-slim

# Definindo diretório de trabalho
WORKDIR /app

# Copiando requirements.txt e instalando dependências
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiando código para o contêiner
COPY . .

# Expondo porta
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "run.py"]

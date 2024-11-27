FROM python:3.9-slim

# Configura o diretório de trabalho
WORKDIR /app

# Copia os arquivos da aplicação para o container
COPY . /app

RUN apt-get update && apt-get install -y libgomp1

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta 8000
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["python", "main.py"]

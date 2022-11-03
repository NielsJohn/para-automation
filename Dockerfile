FROM python:3.10-slim

# copy and install requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy code
COPY ./app ./app

# set app as the working directory
WORKDIR ./app

# expose streamlit's default port
EXPOSE 8501

# run streamlit
ENTRYPOINT ["streamlit", "run", "dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]
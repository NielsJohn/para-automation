FROM python:3.10-slim

# set the working directory
WORKDIR ./code

# copy and install requirements
COPY requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt

# copy files
COPY ./app /code/app

# expose streamlit's default port
EXPOSE 8501

# run streamlit
ENTRYPOINT ["streamlit", "run", "code.streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
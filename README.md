# Para Automation
This package provides a browser interface to help productivity enthusiasts automating their every-day-tasks within the PARA workflow. 
Streamlit is used to provide a UI that allows you to move, archive, display, and remove folders within the PARA categories. 
Under the hood, Pythons pathlib module is used for all operations.

## Usage
### Command Line Execution
To run the script directly, add a `.env` file with the path to your local PARA folder. If you have none, all the PARA folder
structure will be created for you automatically. 

Then run
```bash 
streamlit run streamlit_app.py
```

### Dockerized
It's easiest to use the Makefile to build the image and run the Docker container. 

Run 
```bash 
make image run
``` 
and your app will start automatically. 
Before that, set the variable `HOST_PATH` in the Makefile to your liking. This is the directory where you either store the
PARA folders or were you want to store them. 

In either case, find your service at http://0.0.0.0:8501


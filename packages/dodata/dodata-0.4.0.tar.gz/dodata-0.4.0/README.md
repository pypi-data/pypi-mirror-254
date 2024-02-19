# DoData python library 0.4.0

DoData offers a state-of-the-art data storage solution tailored specifically for chip design. Designed to seamlessly integrate into your workflow, the platform provides a scalable solution for storing, managing, and analyzing your chip data files.

![](https://i.imgur.com/ZwIWS08.png)

## Installation

We only support Python 3.11, and recommend [VSCode](https://code.visualstudio.com/) IDE.

You will need [Anaconda python](https://www.anaconda.com/download/).

After installing python, open Anaconda Prompt as Administrator and install gdstk, psycopg2 and the rest of the dependencies using pip.

![anaconda prompt](https://i.imgur.com/eKk2bbs.png)

```
conda install -c conda-forge psycopg2 -y
pip install "dodata[demos]" --upgrade
```

## Setup

Make sure you create an `.env` file in your working directory.

```
dodata_url = 'https://your.dodata.url.here'
dodata_user = 'dodata_user'
dodata_password = 'dodata_web_password'
dodata_db = 'your.dodata.database.url.here'
dodata_db_user = "db_username_here"
dodata_db_password = "db_password_here"
dodata_db_name = "dodata"
data_db_port = 5432
debug = False
```

The `.env` file can be in the same directory run the notebooks from or in a parent directory.

## Run notebooks

For running the notebooks you can use [VSCode](https://gdsfactory.github.io/gdsfactory/notebooks/_3_vscode.html) or JupyterLab.

- For VSCode make sure you use the same conda python interpreter where you installed the packages [see](https://gdsfactory.github.io/gdsfactory/notebooks/_3_vscode.html)
- For JupyterLab you can launch `jupyter-lab` from the same terminal where you run the installation.

Then, make sure you run the notebooks in order:

- `1_generate_layout`: generate GDS layout and CSV device manifest with device coordinates, settings and analysis.
- `2_generate_measurement_data`: generate CSV measurement data.
- `3_upload_measurements`: Upload wafer definitions and measurement data.
- `4_download_data`: Download analysis using conditional.
- `5_delete`: Delete data.

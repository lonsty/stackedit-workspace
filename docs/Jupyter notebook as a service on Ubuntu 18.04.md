> [https://naysan.ca/2019/09/07/jupyter-notebook-as-a-service-on-ubuntu-18-04-with-python-3/](https://naysan.ca/2019/09/07/jupyter-notebook-as-a-service-on-ubuntu-18-04-with-python-3/)

### 1. Create venv for jupyter

```
$ cd /mnt/data/opt/
$ virtualenv -p python3 jupyter-venv
```

#### 2. Install & configurate jupyter

```
$ source jupyter-venv/bin/activate
$ pip install jupyter
$ jupyter notebook --generate-config
$ jupyter notebook password

$ vi ~/.jupyter/jupyter_notebook_config.py
```

```
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.port = 8888
c.NotebookApp.open_browser = False
c.NotebookApp.notebook_dir = '/mnt/data/workspace/git/documents'
```

#### 3.  Create service file

```
$ sudo vi /etc/systemd/system/jupyter.service
```

```
[Unit]
Description=Jupyter Notebook

[Service]
Type=simple
PIDFile=/run/jupyter.pid
ExecStart=/bin/bash -c "source /mnt/data/opt/jupyter-venv/bin/activate; jupyter-notebook"
User=allen
Group=allen
WorkingDirectory=/mnt/data/workspace
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

#### 4. Start jupyter on boot

```
$ sudo systemctl enable jupyter.service
$ sudo systemctl daemon-reload
$ sudo systemctl start jupyter.service
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbOTU3OTAyMjYyLDM4NzI1NjI3N119
-->
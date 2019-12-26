# {{cookiecutter.project_name}}

{{cookiecutter.project_short_description}}

## Installation

It is highly-recommended to run the Dataflow pipeline within a virtual
environment. Create a virtual env and install the dependencies inside it:

```sh
python3 -m virtualenv venv
venv/bin/pip install -r requirements.txt
```

## Usage


### Setting-up the workers

You can customize how workers were set-up by updating the `setup.py` file. You
can add more commands by adding new lines in the `CUSTOM_COMMANDS` list. For
example:

```python
CUSTOM_COMMANDS = [
    ["apt-get", "update"],
    ["apt-get", "--assume-yes", "install", "libjpeg62"],
]
```

You can also add more dependencies for each of your workers by filling-in the
`worker-requirements.txt` file. **Lastly, you can edit the pipeline by updating
`main.py`.** 

### Running pipelines

In order to run the Dataflow pipeline, execute the following command: 

```sh
venv/bin/python3 main.py
```

You can pass multiple parameters such as the number of workers, machine type,
and more. For example, let's run 10  `n1-standard-1` workers:

```sh
venv/bin/python3 main.py --num-workers 10 --machine-type "n1-standard-1"
```

As best practice, we recommend running your pipeline locally. You can do this
by passing the `--local` flag.

```sh
venv/bin/python3 main.py --local
```

| Parameter              	| Type 	| Description                                        	|
|------------------------	|------	|----------------------------------------------------	|
| `-n`, `--num-workers`  	| int  	| Number of workers to run the Dataflow job.         	|
| `-m`, `--machine-type` 	| str  	| Machine type to run the jobs on.                   	|
| `-s`, `--disk-size`    	| int  	| Disk size (in GB) for each worker when job is run. 	|
| `--project`            	| str  	| Google Cloud Platform (GCP) project to run the Dataflow job                	|
| `--region`             	| str  	| Google Cloud Platform (GCP) region to run the Dataflow job                 	|
| `--artifact-bucket`    	| str  	| Google Cloud Storage (GCS) bucket to store temp and staging files         	|


---

This project was generated using the `standard` template from
[ljvmiranda921/dataflow-cookiecutter](https://github.com/ljvmiranda921/dataflow-cookiecutter).
Have other templates in mind? Feel free to make a Pull Request!

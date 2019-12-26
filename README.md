# dataflow-cookiecutter [![Build Status](https://dev.azure.com/ljvmiranda/ljvmiranda/_apis/build/status/ljvmiranda921.dataflow-cookiecutter?branchName=master)](https://dev.azure.com/ljvmiranda/ljvmiranda/_build/latest?definitionId=5&branchName=master)

**Tired of copy-pasting your ad-hoc Dataflow modules?** Then you can use this
[cookiecutter](https://github.com/cookiecutter/cookiecutter) command-line
tool to easily generate standardized Dataflow templates! :zap:

## Installation

You can install `dataflow-cookiecutter` from PyPI:

```sh
pip install dataflow-cookiecutter
```

In addition, you can also clone this repository and install it locally:

```sh
git clone https://github.com/ljvmiranda921/dataflow-cookiecutter.git
cd dataflow-cookiecutter
python3 setup.py install
```

## Usage

You can create a Dataflow project by executing the command:

```sh
$ dataflow-cookiecutter new
```

You can also use some of the premade templates. Say, you wish to create a
Google Cloud Storage (GCS) to BigQuery (BQ) pipeline:

```sh
$ dataflow-cookiecuter new --template=GCSToBQ
```

In addition, you can use your trusty, old `cookiecutter` command-line tool to
generate templates (only works for `cookiecutter`>=1.7.1):

```sh
cookiecutter https://github.com/ljvmiranda921/dataflow-cookiecutter \
   --directory <directory-to-desired-template> 
```


## FAQ

- **Why are you still wrapping cookiecutter?**  This started as a learning
    project and I want to see how cookiecutter's internals work. In addition, I
    realized I can add more functionality to the CLI more than templating, so
    wrapping Cookiecutter seems to be a good approach.
- **I already have cookiecutter, can I use it with your templates?** Yes of
    course! Look at the Usage section above! However, ensure that your
    cookecutter version is `>=1.7.1` so that you can use the `--directory`
    flag!

# dataflow-cookiecutter [![Build Status](https://dev.azure.com/ljvmiranda/ljvmiranda/_apis/build/status/ljvmiranda921.dataflow-cookiecutter?branchName=master)](https://dev.azure.com/ljvmiranda/ljvmiranda/_build/latest?definitionId=5&branchName=master) ![PyPI](https://img.shields.io/pypi/v/dataflow-cookiecutter?color=light-green&label=pypi&logo=python&logoColor=white)


**Tired of copy-pasting your ad-hoc Dataflow modules?** Then you can use this
[cookiecutter](https://github.com/cookiecutter/cookiecutter) command-line
tool to easily generate standardized Dataflow templates! :zap:

## Installation

You can install `dataflow-cookiecutter` from PyPI:

```sh
pip install dataflow-cookiecutter
```

In addition, you can also clone this repository and install locally:

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

**Choose from a variety of our premade templates.** See all available templates
by running `dataflow-cookiecutter ls`. For example, you can create a Google
Cloud Storage (GCS) to BigQuery (BQ) pipeline via:

```sh
$ dataflow-cookiecuter new --template=GCSToBQ
```

Lastly, our templates are **highly-compatible to your trusty, old
`cookiecutter`** command-line tool (be sure to use `cookiecutter`>=1.7.1!):

```sh
$ cookiecutter https://github.com/ljvmiranda921/dataflow-cookiecutter \
   --directory <directory-to-desired-template> 
```


## FAQ

- **Why are you still wrapping cookiecutter?**  This started as my learning
    project to see how cookiecutter's internals work. While building the alpha
    version, I realized that I can add more functionality to this CLI more than
    templating, so wrapping Cookiecutter seems to be a good approach.
- **I already have cookiecutter, can I use it with your templates?** Yes of
    course! Look at the Usage section above! However, ensure that your
    cookecutter version is `>=1.7.1` so that you can use the `--directory`
    flag!
- **Why are you using Python 3 for Dataflow templates?** It's 2020, we
    shouldn't be supporting [legacy Python](https://pythonclock.org/?1)
    anymore. Besides, Dataflow now has [streaming support in Python
    3](https://cloud.google.com/blog/products/data-analytics/introducing-python-3-python-streaming-support-from-cloud-dataflow).
    See more developments for Beam support in Python 3  in their
    [issue tracker](https://issues.apache.org/jira/browse/BEAM-1251).

# vscode-python-datascience-template

[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit) [![protected: by-gitleaks-blue](https://img.shields.io/badge/protected%20by-gitleaks-blue)](https://github.com/gitleaks/gitleaks-action) [![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit) [![Uses the Cookiecutter Data Science project template](https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter)](https://cookiecutter-data-science.drivendata.org/)

Start a datascience project faster and easier by simply creating a repository based on this template.  
This repository already includes some of the most known DevSecOps recommandations.

## Run Locally

Clone the project

```bash
git clone https://link-to-my-project
```

Go to the project directory and launch VSCode

```bash
cd my-project
code .
```

> If you want to use JupyterLab, you must uncomment the installation, execution on container start and appPort in .devcontainer/devcontainer.json.

You should reopen VSCode in a devcontainer.

Then give the rights to your user to the files that will be overwritten:

```bash
sudo chown $USER:$USER README.md
sudo chown $USER:$USER .gitignore
```

Create a project in a terminal using ccds *(the `-f` parameter will override the files)* from the parent directory:

```bash
cd ..
ccds -f
```

In the command for the "project" name, you must give the name of the git folder *(`my-project` in my previous example)*.  

Go back to the directory and give files rights back to root:

```bash
cd my-project
sudo chown root README.md
sudo chown root .gitignore
```

Then configure pre-commit *(if you want to execute gitleaks every time you commit)*:

```bash
pre-commit autoupdate
pre-commit install
```

And finally, if you want to ignore some findings from `gitleaks`, add them to the .gitleaksignore file.

*(If you want to add Anaconda directly at the container creation, uncomment it in the devcontainer.json)*

## Pay attention

### If you are using Conda

Conda is not directly handled by cyclonedx. You will certainly need to precise a Conda build in GitHub action, and add the conda SBOM generation with something like:  
```bash
cyclonedx-py environment "$(conda run which python)"
```

### If you have a lot of files or big files

gitleaks will scan every file before each commit. If you have a lot of files or big files, maybe you should only trigger it in GitHub action, and then remove .pre-commit-config.yml file.

The GitHub action can be found on the [gitleak repository](https://github.com/gitleaks/gitleaks?tab=readme-ov-file#github-action).

## Related

Here are some related documentations:

- [How to structure Python's project in Data science](https://cookiecutter-data-science.drivendata.org/)  
- [Microsoft's doc on devcontainers](https://code.visualstudio.com/docs/devcontainers/containers)  
- [Microsoft's doc on Python in VS](https://code.visualstudio.com/docs/python/python-quick-start)
- [Microsoft's base image that I copied](https://github.com/microsoft/datascience-py-r)

## Authors

- [@eneru](https://www.github.com/Eneru)
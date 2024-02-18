import setuptools
from typing import List
from pathlib import Path

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''this Fucntion will return list of requirements'''
    requirements=[]
    with open(Path(file_path)) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


__version__ = "0.0.3"

REPO_NAME = "e2e_mlops_dimond_price_prediction"
AUTHOR_USER_NAME = "satish0308"
SRC_REPO = "Dimond-Price-Prediction"
AUTHOR_EMAIL = "hiremath0308@gmail.com"





setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Diamond-Price-Prediction Model",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
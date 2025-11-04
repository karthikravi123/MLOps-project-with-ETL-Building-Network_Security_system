'''
The Setup.py file is essential part of packaging and distributing  python project.
It is used by setup tools to define the configuration of your project such as its metadata,dependencies and more
'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    this function will return list of requirements
    """

    requirements_lst:List[str] = []

    try:
        with open('requirements.txt','r') as file:
            ##Read lines from line
            lines= file.readlines()
            ##process each lines
            for line in lines:
                requirement = line.strip()
                ##igmore empty line and -e
                if requirement and requirement!= '-e .':
                    requirements_lst.append(requirement)
    except FileNotFoundError:
        print("requirementts.txt file not found")
    
    return requirements_lst


#print(get_requirements())

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="karthik",
    author_email="geokarthik09@gmail.com",
    packages=find_packages(),
    install_requirements = get_requirements()
)
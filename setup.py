#F:/anaconda_installed/Scripts/activate
#conda activate venv/
from setuptools import setup, find_packages
from typing import List



def get_requirments()->List[str]:
    requirment_lst:List[str]=[]
    try:
        with open('requirments.txt','r') as file:
            lines=file.readlines()
            for line in lines:
                requirment=line.strip()
                if requirment and requirment!='-e .':
                    requirment_lst.append(requirment)

    except FileNotFoundError:
        print('requirments.txt not found')
    return requirment_lst


# print(get_requirments())

setup(
    name="NetworkSecurity",
    version='0.0.1',
    author_email='parthibdhal11@gmail.com',
    packages=find_packages(),
    install_requires=get_requirments()
)























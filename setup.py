from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT = '-e .'
def get_requirments(file_path:str)-> List[str]:
    """get_requirments cette fonction retourne la liste des libraires requirments

    Args:
        file_path (str): _description_

    Returns:
        List[str]: _description_
    """
    requirments=[]
    with open(file_path) as file_obj:
        requirments=file_obj.readlines()
        requirments=[req.replace("\n", "") for req in requirments]
        
        if HYPEN_E_DOT in requirments:
            requirments.remove(HYPEN_E_DOT)
            
    return requirments

setup(
    name='analyse_exploratoire',
    version='0.0.1',
    author='dai',
    author_email='dai.tensaout@gmail.com',
    packages=find_packages(),
    install_requires=get_requirments('requirements.txt')
    
    
)
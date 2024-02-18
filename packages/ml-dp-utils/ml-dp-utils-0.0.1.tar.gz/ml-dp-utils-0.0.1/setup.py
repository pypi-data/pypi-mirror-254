from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Pacote utilidades Deep Learning'
LONG_DESCRIPTION = 'Um pacote com as funções mais utilizadas para facilitar nossa vida!'

print(find_packages())
# Setting up
setup(
       # 'name' deve corresponder ao nome da pasta 'verysimplemodule'
        name="ml-dp-utils", 
        version=VERSION,
        author="Victor Gomes",
        author_email="victor.gomes.almeida.vg@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['torch', 'torchvision', 'matplotlib', 'numpy', 'pathlib'], # adicione outros pacotes que 
        # precisem ser instalados com o seu pacote. Ex: 'caer'
        
        keywords=['python', 'deeplearn', 'pytorch'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
           " Operating System :: POSIX :: Linux"
        ]
)

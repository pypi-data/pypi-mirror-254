from setuptools import setup, find_packages
setup(
    name='jsongui',
    version='5.0.0',
    packages=find_packages(),
    author='BAA4TS',
    author_email='baa4ts@gmail.com',
    description='libreria simple para trabajar con json, en un archibo llamado: datos.json',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/BAA4TS/jsongui',
    # Elimina 'json' de install_requires
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        # Añade más clasificaciones según tu paquete
    ],
)

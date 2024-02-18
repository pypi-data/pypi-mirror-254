from setuptools import setup, find_packages

setup(
    name='mercadolibre-sdk',
    version='0.0.13',
    packages=find_packages(),
    install_requires=[
        'requests==2.31.0', 'redis==5.0.1', 'flask==3.0.0', 'python-dotenv==1.0.0'
    ],
    entry_points={
        'console_scripts': [
            'mercadolibre.authorize = mercadolibre.authorization:authorize',
        ],
    },
    author='Mercado Radar',
    description='Description of your package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/mercadoradar/mercadolibre-sdk'
)

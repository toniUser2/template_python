from setuptools import setup, find_packages

setup(
    name='template_python',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        # Füge hier deine Abhängigkeiten hinzu
    ],
    entry_points={
        'console_scripts': [
            # Beispiel: 'main = template_python.main:main',
        ],
    },
)
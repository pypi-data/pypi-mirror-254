from setuptools import setup, find_packages

setup(
    name='run_my_monitoring_dashboard',
    version='0.0.4',
    description='A very basic monitoring package',
    author='Ritik Saxena',
    author_email='ritiksaxena90@gmail.com',
    packages=find_packages(),
    install_requires=['pandas', 'streamlit', 'datetime', 'numpy', 'streamlit_option_menu'],
    entry_points={
        'console_scripts': [
            'run_my_monitoring_dashboard = run_my_monitoring_dashboard.main:main',
        ],
    },
)

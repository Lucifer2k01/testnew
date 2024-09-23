from setuptools import find_packages, setup

setup(
    name='flaskr',  # This is the name of the package
    version='1.0.0',  # You can set the version for your app
    packages=find_packages(),  # Automatically find packages in the directory
    include_package_data=True,  # Include all data files specified in MANIFEST.in
    zip_safe=False,
    install_requires=[
        'flask',
    ],
    entry_points={
        'console_scripts': [
            'flaskr=flaskr.__main__:main',  # Entry point for running the Flask app
        ],
    },
)

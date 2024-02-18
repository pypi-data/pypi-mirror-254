from setuptools import setup
import pathlib

# Read the contents of your README.md file and license file 
readme_path = pathlib.Path(__file__).parent / 'README.md'
license_path = pathlib.Path(__file__).parent / 'LICENSE'
long_description = readme_path.read_text(encoding='utf-8')
license_data = license_path.read_text(encoding='utf-8')


setup(
    name='express_server',
    version="0.0.6",
    install_requires=[],
    python_requires='>=3.1',
    packages= ["express_server"],
    package_data={'': ['./**']},
    author_email="avinashtare.work@gmail.com",
    url="https://example.com/",
    author="Avinash Tare",
    description="Express-Server is a lightweight and fast web server for Python, inspired by the simplicity of Express.js.",
    long_description_content_type='text/markdown',
    long_description=long_description,
    license=license_data,
        project_urls={
        'Documentation': 'https://example.com/',
        'Source': 'https://github.com/avinashtare/express-server-python',
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
    ],
    keywords='express, python-express, express-python, express-server, server-express',
    include_package_data=True,
)
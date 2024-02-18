from setuptools import setup, find_namespace_packages


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="perun.proxygui",
    python_requires=">=3.9",
    url="https://gitlab.ics.muni.cz/perun/perun-proxyidp/proxyidp-gui.git",
    description="Module with GUI and API for Perun ProxyIdP",
    long_description=readme(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    packages=find_namespace_packages(include=["perun.*"]),
    install_requires=[
        "Authlib==1.3.0",
        "setuptools",
        "PyYAML==6.0.1",
        "Flask==2.3.3",
        "Flask-pyoidc==3.14.3",
        "Flask-Babel==3.1.0",
        "perun.connector==3.8.1",
        "python-smail==0.9.0",
        "SQLAlchemy==2.0.25",
        "pymongo==3.13.0",  # downgrade pymongo for Flask (internal) Sessions to work
        "validators==0.22.0",
        "idpyoidc==2.0.0",
        "python-dateutil==2.8.2",
        "Jinja2==3.1.3",
        "requests==2.31.0",
        "Flask-Session==0.5.0",
        "pysaml2==7.4.2",
        "cryptojwt==1.8.3",
        "satosacontrib.perun==4.3.1",
        "user-agents==2.2.0",
        "flask-smorest==0.42.3",
        "marshmallow==3.20.2",
        "deepdiff==6.7.1",
    ],
    extras_require={
        "kerberos": [
            "kerberos==1.3.1; platform_system != 'Windows'",
            "winkerberos==0.10.0; platform_system == 'Windows'",
        ],
        "postgresql": [
            "psycopg2-binary==2.9.9",
        ],
    },
)

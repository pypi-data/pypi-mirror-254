from setuptools import find_packages, setup

setup(
    name="eai-commons",
    packages=find_packages(exclude=["eai_commons_tests", "eai_commons_tests.*"]),
    version="0.0.7",
    install_requires=[
        "pydantic",
        "coloredlogs>=15.0.1",
        "concurrent-log-handler>=0.9.24",
        "pytz>=2023.3",
        "pycryptodome>=3.18.0",
        "PyJWT>=2.6.0",
        "tqdm>=4.65.0",
        "cryptography",
        "curl_cffi",
        "httpx>=0.24.1",
        "shortuuid",
    ],
)

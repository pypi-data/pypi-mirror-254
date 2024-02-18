import setuptools

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="dpeaDPi",
    version="0.1.6",
    author="Stan Reifel",
    description="Python package infrastructure for DPEA's DPi boards",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=["dpeaDPi"],
    install_requires=["pyserial", "requests", "smbus2", "adafruit-blinka", "adafruit-circuitpython-vl6180x"]
)

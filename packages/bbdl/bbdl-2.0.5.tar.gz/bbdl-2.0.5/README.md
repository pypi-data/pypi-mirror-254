# Download Borneo Bulletin :newspaper:
![Preview of BB-DL.py](preview-bb-dl.PNG)

## Usage

This only works on **Python3** :snake:

`python3 bbdl.py` if you have Python2 and Python3 installed or;

`python bbdl.py` if you only have Python3 installed.

:whale:

If you have Docker/podman installed, this can be done easily with a single command line where `${pwd}` will be the host directory that it will copy its files from the container to:

`docker run -it --rm -v ${pwd}:/usr/src/app/news docker.pkg.github.com/Anak-IT-Brunei/bb-dl/bbdl:2.0.3`

## Download

For the Python Script, find it on the release page [here](https://github.com/Anak-IT-Brunei/bb-dl/releases)

For the Docker Image, find it on Github Packages [here](https://github.com/Anak-IT-Brunei/bb-dl/packages/)

## Documentation

Source code for the documenation are in the `/docs` folder. Be sure to install the dependencies (at least, mkdocs and mkdocs-custommill via pip) to be able to run `mkdocs serve` to contribute to the documentations.

## Credits

Decided to make a Borneo Bulletin download script thanks to Tim's Telegram News Bot for exposing the URL.

Feel free to fork and contribute

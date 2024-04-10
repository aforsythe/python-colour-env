# Visual Studio Code Server Environment with Colour Science 0.4.4

to run type

1. install docker - `brew install --cask docker` 
2. clone this repo - `git clone https://github.com/ampas/python-colour-env`
3. change directory into the repo - `cd python-colour-env`
4. build and launch the docker container - `docker compose up`
5. Visit [http://0.0.0.0:8443/](http://0.0.0.0:8443/) using your browser

The `/config` directory on the container is mapped to `./config` on your local machine.  Settings and data files are stored there.  Any files you create, you'll most likely want to save in a subdirectory of your choosing under `./config/workspace/` on your local machine.

## Known issues

* Images don't show inline.  You'll need to save them to a file for now.
* The python extension isn't installing with the dockerfile command.  Install it via the extension section of VS Code.



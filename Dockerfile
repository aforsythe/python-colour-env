FROM lscr.io/linuxserver/code-server:4.23.0

# Install Python 3.10 and necessary tools
RUN apt-get update && apt-get install -y \
    software-properties-common \
    python3.10 \
    python3-distutils \
    python3-pip \
    && add-apt-repository ppa:deadsnakes/ppa \
    && rm -rf /var/lib/apt/lists/*

# Set Python 3.10 as the default Python version
RUN ln -sf /usr/bin/python3.10 /usr/bin/python3
RUN ln -sf /usr/bin/python3.10 /usr/bin/python

# Install dependencies for matplotlib
RUN apt-get update && apt-get install -y \
    libfreetype6-dev \
    libjpeg-dev \
    libpng-dev \
    pkg-config

# Install matplotlib
RUN pip3 install matplotlib

# Install Colour Science 0.4.4
RUN pip3 install 'colour-science[optional]==0.4.4'

# Install code-server extensions
RUN /app/code-server/lib/vscode/bin/remote-cli/code-server --install-extension ms-python.python

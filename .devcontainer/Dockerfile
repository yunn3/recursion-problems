FROM mcr.microsoft.com/vscode/devcontainers/base:ubuntu

RUN apt update && apt upgrade -y

# install ripgrep 
RUN curl -L https://github.com/BurntSushi/ripgrep/releases/download/13.0.0/ripgrep_13.0.0_amd64.deb --output /tmp/ripgrep_13.0.0_amd64.deb && dpkg -i /tmp/ripgrep_13.0.0_amd64.deb


# Use Ubuntu with TeX Live 2024
FROM ubuntu:24.04

# Avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install base tools + TeX Live full (includes pdfLaTeX, bibtex, etc.)
RUN apt-get update && apt-get install -y \
    texlive-full \
    latexmk \
    make \
    git \
    curl \
    wget \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Install VS Code Remote DevContainer support tools
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        sudo \
        locales \
        && locale-gen en_US.UTF-8

ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US:en
ENV LC_ALL=en_US.UTF-8

# # Create a user for VS Code
# ARG USERNAME=vscode
# ARG USER_UID=1000
# ARG USER_GID=$USER_UID

# RUN getent group $USER_GID || groupadd --gid $USER_GID $USERNAME \
#     && id -u $USERNAME &>/dev/null || useradd --uid $USER_UID --gid $USER_GID -m $USERNAME -s /bin/bash \
#     && usermod -aG sudo $USERNAME \
#     && echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/$USERNAME \
#     && chmod 0440 /etc/sudoers.d/$USERNAME


# Switch to the vscode user
USER $USERNAME
WORKDIR /workspace

# Set default shell
SHELL ["/bin/bash", "-c"]

# Optional: install latexmk for easier compilation
RUN sudo apt-get update && sudo apt-get install -y latexmk && sudo apt-get clean

# Expose workspace
VOLUME /workspace

# Default command
CMD ["bash"]

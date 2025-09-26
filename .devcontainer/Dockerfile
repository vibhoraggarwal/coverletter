# Use your prebuilt image as base
ARG BASE_IMAGE=vibhorag24/coverletter:latest
FROM ${BASE_IMAGE}

# Accept UID/GID as build arguments
ARG USERNAME=vscode

# Create user with build-time UID/GID
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd -m --uid $USER_UID --gid $USER_GID -s /bin/bash $USERNAME

USER $USERNAME
WORKDIR /workspace

# Add alias to the .bashrc of the non-root user
RUN echo "alias gen_tex_doc='pdflatex -shell-escape'" >> /home/${USERNAME}/.bashrc && \
    chown ${USERNAME}:${USERNAME} /home/${USERNAME}/.bashrc

CMD ["bash"]
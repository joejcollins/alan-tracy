# Sourcery won't run on `arm` so force the use of `amd64` for the base image.
FROM --platform=linux/amd64 mcr.microsoft.com/devcontainers/base:bookworm

# Install uv for everyone not just the current user.
RUN curl -LsSf https://astral.sh/uv/install.sh | sh \
 && cp /root/.local/bin/uv /usr/local/bin/uv

# Install LaTeX.
RUN apt-get --quiet update \
 && apt-get install --assume-yes texlive-latex-extra texlive-extra-utils latexmk \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Install Rust using rustup and set for all users so we can have tex-fmt.
# Once Debian trixie is available tex-fmt can be installed as a package.
RUN curl  --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y \
 && mkdir -p /usr/local/cargo /usr/local/rustup \
 && mv /root/.cargo/* /usr/local/cargo/ \
 && rm -rf /root/.cargo /root/.rustup \
 && ln -s /usr/local/cargo/bin/* /usr/local/bin/
 ENV CARGO_HOME=/usr/local/cargo
 ENV RUSTUP_HOME=/usr/local/rustup
 ENV PATH="/usr/local/cargo/bin:${PATH}"
RUN cargo install tex-fmt

# Add some labels so it looks nice in Github packages.
LABEL org.opencontainers.image.source=https://github.com/joejcollins/alan_tracy
LABEL org.opencontainers.image.description="alan_tracy image."

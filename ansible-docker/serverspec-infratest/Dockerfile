# Use a base image with Ruby pre-installed
FROM ruby:3.1

# Install any system dependencies needed for Serverspec
RUN apt-get update && apt-get install -y \
    build-essential \
    sudo \
    openssh-client \
    && rm -rf /var/lib/apt/lists/*

# Install Serverspec and supporting gems
RUN gem install serverspec

# Set the working directory
WORKDIR /serverspec

# Copy your Serverspec files into the container
COPY . .

# Set entrypoint for running the test suite
ENTRYPOINT ["rake", "spec"]

#ENTRYPOINT ["/bin/bash"]
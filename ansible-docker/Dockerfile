# Use an official lightweight image like Ubuntu or Alpine
FROM ubuntu:latest

######### Install  AWS CLI ############

RUN apt-get update && \
    apt-get install -y \
    sudo \
    unzip \
    curl \
    groff \
    less \
    python3 \
    python3-pip && \
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    sudo ./aws/install && \
    rm -rf awscliv2.zip ./aws

    ######### Configure ll  AWS CLI ############

# Install necessary packages and Ansible


# Install Python, pip, and virtualenv
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv ssh git && apt-get clean

# Create and use a virtual environment for Ansible and AWS libraries
RUN python3 -m venv /opt/ansible-venv
RUN /opt/ansible-venv/bin/pip install ansible boto3 botocore

# Set the PATH so Ansible can be used directly
ENV PATH="/opt/ansible-venv/bin:$PATH"

# Set the working directory
WORKDIR /ansible

COPY ansible.config /etc/ansible/ansible.cfg

# Set entrypoint to bash by default; you can override this to run ansible-playbook
ENTRYPOINT ["/bin/bash"]
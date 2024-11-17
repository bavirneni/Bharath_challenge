require 'serverspec'
require 'net/ssh'

# Set backend to SSH
set :backend, :ssh

options = {
  user: 'ubuntu', # Use 'ubuntu' or another user depending on your AMI
  keys: ['/root/.ssh/private_key.pem'], # Path inside the container
  verify_host_key: :never # Optionally disable host key verification for simplicity
}

host = ENV['TARGET_HOST'] || '34.205.159.6'

set :host, host
set :ssh_options, options

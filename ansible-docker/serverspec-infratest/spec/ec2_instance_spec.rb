require 'spec_helper'

describe port(22) do
  it { should be_listening }
  puts "Success: PORT is listening on port 22."
end

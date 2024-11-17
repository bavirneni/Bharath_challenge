require 'spec_helper'

describe file('/etc/httpd/conf/httpd.conf') do
  it { should exist }
  it { should be_file }
  its(:content) { should match /^Listen 80$/ }
end
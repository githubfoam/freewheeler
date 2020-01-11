require 'thor'
require 'fileutils'
require 'timeout'

class Packer < Thor

  desc 'validate', 'Validate all the packer templates'
  def validate
    Dir.chdir './packer' do
      templates = Dir.glob('*.json')
      templates.each do |template|
        puts "#{template}"
        unless system "packer validate #{template}"
          fail 'Validation failed!'
        end
        puts "\n"
      end
    end
  end



  desc 'clean', 'Remove temporary artifacts'
  def clean(what)
    if what == 'cache'
      FileUtils.rm_rf(Dir.glob('./packer/packer_cache'))
      FileUtils.rm_rf(Dir.glob('./packer/output-*-iso'))
    elsif what == 'boxes'
      FileUtils.rm_rf(Dir.glob('./builds/*/*.box'))
      FileUtils.rm_rf(Dir.glob('./builds/*/*_SHA256SUM'))
      FileUtils.rm_rf(Dir.glob('./builds/*/*_SHA512SUM'))
    end
  end


  desc 'build', 'Run the packer builder'
  option :vagrant_cloud_version, :banner => '<vagrant cloud version>'
  option :os, :banner => '<os>'
  option :os_version, :banner => '<os version>'
  option :providers, :banner => '<providers>'

  def build
    Dir.chdir './packer' do
      templates = Dir.glob("#{options[:os]}-#{options[:os_version]}-amd64.json")
      templates.each do |template|
        name = template.chomp('.json').split('-')
        if options[:os] == 'debian' && options[:os_version] == '9.5.0'
          system "curl -s \"https://vagrantcloud.com/api/v1/box/vagrantfoam/#{options[:os]}-#{options[:os_version]}-amd64/versions\" -X POST -d version[version]=\"#{options[:vagrant_cloud_version]}\" -d version[description]=\"### tools\n* VMware Tools 10.3.2\n* VirtualBox Guest Additions 5.2.20\n* Chef 14.5.33-1\n* Ruby 2.3.3-1+deb9u1\n* Rubygems 2.7.7\n\r### source\n[packer templates on github](https://github.com/githubfoam/freewheeler/tree/thor-version)\" -d access_token=\"$VAGRANT_CLOUD_TOKEN_ALL\""
        end
        providers = options[:providers].split(",")
        providers.each do |provider|
          system "packer build --only=#{provider}-iso -var 'PACKER_VAGRANT_CLOUD_VERSION=#{options[:vagrant_cloud_version]}' #{template}"
        end
        system "curl -s \"https://vagrantcloud.com/api/v1/box/vagrantfoam/#{options[:os]}-#{options[:os_version]}-amd64/version/#{options[:vagrant_cloud_version]}/release\" -X PUT -d access_token=\"$VAGRANT_CLOUD_TOKEN_ALL\""
      end
    end
  end



end

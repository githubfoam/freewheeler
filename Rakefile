require 'json'
require 'net/http'
require 'pathname'
require 'rainbow'
require 'rspec/core/rake_task'
require 'uri'

VAGRANT_PROVIDERS = {
  virtualbox: {
    builder_type: 'virtualbox-iso'
  },
  vmware_desktop: {
    builder_type: 'vmware-iso'
  }
}.freeze

task default: ['packer:validate', 'packer:check_iso_url']

namespace :packer do
  desc 'Validate all the packer templates'
  task :validate do
    Pathname.glob('*.json').sort.each do |template|
      puts Rainbow("Validating #{template}...").green
      unless system "packer validate #{template}"
        puts Rainbow("#{template} is not a valid packer template").red
        raise "#{template} is not a valid packer template"
      end
    end
  end

  desc 'Check if all the ISO URLs are available'
  task :check_iso_url do
    Pathname.glob('*.json').sort.each do |template|
      json = JSON.parse(template.read)
      mirror = json['variables']['mirror']
      iso_urls = json['builders'].map do |builder|
        builder['iso_url'].sub('{{user `mirror`}}', mirror)
      end
      iso_urls.uniq.each do |iso_url|
        puts Rainbow("Checking if #{iso_url} is available...").green
        request_head(iso_url) do |response|
          unless available?(response)
            puts Rainbow("#{iso_url} is not available: uri=#{response.uri}, message=#{response.message}").red
            raise "#{iso_url} is not available"
          end
        end
      end
    end
  end

  desc 'Build and upload the vagrant box to vagrant cloud'
  task :release, [:template, :sloth, :version, :provider] do |_t, args|
    template = Pathname.new(args[:template])
    sloth     = args[:sloth]
    version  = args[:version]
    provider = args[:provider]

    json = JSON.parse(template.read)

    builders = json['builders']
    builders.select! do |builder|
      builder['type'] == VAGRANT_PROVIDERS[provider.to_sym][:builder_type]
    end

    post_processors = json['post-processors']
    post_processors << vagrant_cloud_post_processor_config(sloth, version, provider)
    json['post-processors'] = [post_processors]

    file = Tempfile.open('packer-templates') do |f|
      f.tap do |f|
        JSON.dump(json, f)
      end
    end

    unless system("packer build -var-file=vars/release.json '#{file.path}'")
      puts Rainbow("Failed to release #{sloth} to vagrant cloud").red
      raise "Failed to release #{sloth} to vagrant cloud"
    end
  end
end

desc 'Run serverspec tests'
RSpec::Core::RakeTask.new(:spec, :host) do |_t, args|
  ENV['HOST'] = args[:host]
end

def request_head(uri, &block)
  uri = URI(uri)
  response = Net::HTTP.start(uri.host, uri.port, use_ssl: uri.scheme == 'https') do |http|
    http.request_head(uri)
  end
  if response.is_a?(Net::HTTPRedirection)
    request_head(response['Location'], &block)
  else
    yield response
  end
end

def available?(response)
  response.is_a?(Net::HTTPSuccess)
end

def vagrant_cloud_post_processor_config(sloth, version, provider)
  {
    'type' => 'vagrant-cloud',
    'artifact' => sloth,
    'artifact_type' => 'vagrant.box',
    "box_tag": "{{user `vm_name` }}",
    "access_token": "{{user `vagrant_cloud_token`}}",
    "version": "{{user `vm_version`}}",
    'metadata' => {
      'version' => version,
      'provider' => provider
    }
  }
end

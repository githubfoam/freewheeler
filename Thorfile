require 'thor'
require 'fileutils'
require 'timeout'

class Packer < Thor

  desc 'validate', 'Validate all the packer templates'
  def validate
    Dir.chdir './packer_templates' do
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

end

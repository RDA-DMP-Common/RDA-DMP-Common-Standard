require 'yaml'
require 'logger'

config_hash = YAML.load_file("#{File.dirname(__FILE__)}/../config/config.yaml")
config_hash.each do |key_value_pair|
  key = key_value_pair[0].upcase
  value = key_value_pair[1]
  if value.is_a? String then
    eval "#{key} = '#{value}'"
  else
    eval "#{key} = #{value}"
  end
end

LOGGER = Logger.new(STDOUT)
# LOGGER.formatter = proc { |severity, datetime, progname, msg| "#{severity}: #{msg} - #{caller[4]}\n"}
LOGGER.formatter = proc { |severity, datetime, progname, msg| "#{severity}: #{msg}\n"}
LOGGER.level = eval("Logger::#{LOG_LEVEL.upcase}")
STDOUT.sync = true

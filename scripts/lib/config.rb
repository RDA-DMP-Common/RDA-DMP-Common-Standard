require 'yaml'
require 'logger'
require 'colorize'

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

String.disable_colorization (COLOURED_OUTPUT ==  false)

LOGGER = Logger.new(STDOUT)
# LOGGER.formatter = proc { |severity, datetime, progname, msg| "#{severity}: #{msg} - #{caller[4]}\n"}
# LOGGER.formatter = proc { |severity, datetime, progname, msg| "#{severity}: #{msg}\n"}
LOGGER.formatter = proc do |severity, datetime, progname, msg|
  if ["ERROR","FATAL"].include? severity then
    "#{severity}: #{msg}\n".light_red
  elsif severity == "DEBUG" then
    "#{severity}: #{msg}\n".light_white
  else
    "#{severity}: #{msg}\n".light_cyan
  end
end
LOGGER.level = eval("Logger::#{LOG_LEVEL.upcase}")
STDOUT.sync = true

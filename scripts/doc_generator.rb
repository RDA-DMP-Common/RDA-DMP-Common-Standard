#!/usr/bin/env ruby

require './lib/config'
require './lib/db'
require './lib/model'
require './lib/doc_md'
require 'colorize'


def populate_rdb_from_google_sheet
  LOGGER.debug("Populating 'DataTypes' from Google spreadsheet....")
  DataType.populate_from_google_csv
  LOGGER.info("'DataTypes' populated from Google spreadsheet - OK")
  LOGGER.debug("Populating 'Vocabularies' from Google spreadsheet....")
  Vocabulary.populate_from_google_csv
  LOGGER.info("'Vocabularies' populated from Google spreadsheet - OK")
  LOGGER.debug("Populating 'Properties' from Google spreadsheet....")
  Property.populate_from_google_csv
  LOGGER.info("'Properties' populated from Google spreadsheet - OK")
  LOGGER.debug("Populating 'Values' from Google spreadsheet....")
  Value.populate_from_google_csv
  LOGGER.info("'Values' populated from Google spreadsheet - OK")
  LOGGER.info "Populated relational database from Google Sheet"
end

def generate_doc(path)
  header = File.read("./doc_templates/header.md")
  footer = File.read("./doc_templates/footer.md")
  dmp = Property['dmp']
  md_doc = MarkdownDocument.new(path,header,footer,dmp)
  md_doc.generate
  md_doc.write_to_file
end


# MAIN PROCESS

if RESET_DATABASE_FROM_GOOGLE_SHEET then
  populate_rdb_from_google_sheet
end

generate_doc("#{DOC_ROOT}/index.md")



# CSV.new(open(GOOGLE_SHEETS_CSV_URLS['Vocabulary']), CSV_PARSING_OPTIONS).each do |row|
#   puts row.inspect
# end

# p = Property['dataset_personal_data']
# p.ordered_values.each {|v| puts v.inspect}
#!/usr/bin/env ruby

require './lib/config'
require './lib/google'
require './lib/db'
require './lib/model'
require './lib/doc_md'


def populate_rdb_from_google_sheet
  service = Google::Apis::SheetsV4::SheetsService.new
  service.client_options.application_name = 'RDA DMP Common Standard Generator'
  service.authorization = authorize
  LOGGER.debug("Populating 'DataTypes' from Google spreadsheet....")
  DataType.populate_from_google_sheet(service,GOOGLE_SHEET_ID,'data_types!A2:C')
  LOGGER.info("'DataTypes' populated from Google spreadsheet - OK")
  LOGGER.debug("Populating 'Vocabularies' from Google spreadsheet....")
  Vocabulary.populate_from_google_sheet(service,GOOGLE_SHEET_ID,'vocabularies!A2:E')
  LOGGER.info("'Vocabularies' populated from Google spreadsheet - OK")
  LOGGER.debug("Populating 'Properties' from Google spreadsheet....")
  Property.populate_from_google_sheet(service,GOOGLE_SHEET_ID,'properties!A2:I')
  LOGGER.info("'Properties' populated from Google spreadsheet - OK")
  # LOGGER.debug("Populating 'Attributes' from Google spreadsheet....")
  # Attribute.populate_from_google_sheet(service,GOOGLE_SHEET_ID,'attributes!A2:F')
  # LOGGER.info("'Attributes' populated from Google spreadsheet - OK")
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

if RESET_ALL_DATA then
  populate_rdb_from_google_sheet
end

generate_doc("#{DOC_ROOT}/index.md")



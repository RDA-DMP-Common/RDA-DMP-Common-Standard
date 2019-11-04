#!/usr/bin/env ruby
require './lib/config'
require './lib/google'
require './lib/db'
require './lib/model'
require './lib/doc_md'



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



if RESET_DATABASE_FROM_GOOGLE_SHEET then
  populate_rdb_from_google_sheet
end
require 'sequel'
# require 'csv'

# CSV_PARSING_OPTIONS = {:headers=>true,:encoding=>'UTF-8'}

class Vocabulary < Sequel::Model
  set_primary_key :id
  unrestrict_primary_key
  one_to_many :properties

  def self.populate_from_google_sheet(service,sheet_id,range)
    response = service.get_spreadsheet_values(sheet_id,range)
    response.values.each do |row|
      create(
        id: row[0],
        label: row[1],
        uri: row[2],
        notes: row[4],
        vocab_type: row[5]
      )
    end
  end
end


class DataType < Sequel::Model
  set_primary_key :id
  unrestrict_primary_key
  one_to_many :properties
  one_to_many :attributes

  def self.populate_from_google_sheet(service,sheet_id,range)
    response = service.get_spreadsheet_values(sheet_id,range)
    response.values.each do |row|
      create(
        id: row[0],
        label: row[1],
        notes: row[3]
      )
    end
  end
end

class Property < Sequel::Model
  plugin :tree, order: :label_human
  set_primary_key :id
  unrestrict_primary_key
  many_to_one :vocabulary
  many_to_one :data_type
  # one_to_many :attributes

  def self.populate_from_google_sheet(service,sheet_id,range)
    response = service.get_spreadsheet_values(sheet_id,range)
    response.values.each do |row|
      begin
        create(
          id: row[0],
          vocabulary_id: row[1],
          label_human: row[2],
          label_machine: row[3],
          data_type_id: row[4],
          parent_id: row[5],
          cardinality: row[6],
          description: row[7],
          example_value: row[8],
          uri: row[9],
          notes: row[10]
        )
      rescue Exception => e
        LOGGER.error("Failed to create record for #{row.inspect}")
      end
    end
  end
end

# class Attribute < Sequel::Model
#   set_primary_key :id
#   unrestrict_primary_key
#   many_to_one :property
#   many_to_one :data_type

#   def self.populate_from_google_sheet(service,sheet_id,range)
#     response = service.get_spreadsheet_values(sheet_id,range)
#     response.values.each do |row|
#       begin
#         create(
#           property_id: row[0],
#           label_human: row[1],
#           label_machine: row[2],
#           data_type_id: row[3],
#           cardinality: row[4],
#           example_value: row[5],
#           notes: row[6]
#         )
#       rescue Exception => e
#         LOGGER.error("Failed to create record for #{row.inspect}")
#       end
#     end
#   end
# end
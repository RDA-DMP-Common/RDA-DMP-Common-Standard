require 'sequel'
require 'csv'
require 'open-uri'

CSV_PARSING_OPTIONS = {:headers=>true,:encoding=>'UTF-8'}

class Vocabulary < Sequel::Model
  set_primary_key :id
  unrestrict_primary_key
  one_to_many :properties
  one_to_many :values

  def self.populate_from_google_csv
    CSV.new(open(GOOGLE_SHEETS_CSV_URLS[self.name]), CSV_PARSING_OPTIONS).each do |row|
      create(
        id: row['id'],
        label: row['label'],
        uri: row['uri'],
        notes: row['notes'],
        type: row['vocab_type']
      )
    end
  end

end


class DataType < Sequel::Model
  set_primary_key :id
  unrestrict_primary_key
  one_to_many :properties
  one_to_many :attributes

  def self.populate_from_google_csv
    CSV.new(open(GOOGLE_SHEETS_CSV_URLS[self.name]), CSV_PARSING_OPTIONS).each do |row|
      create(
        id: row['id'],
        label: row['label'],
        notes: row['notes']
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
  one_to_many :values

  def self.populate_from_google_csv
    CSV.new(open(GOOGLE_SHEETS_CSV_URLS[self.name]), CSV_PARSING_OPTIONS).each do |row|
      create(
        id: row['id'],
        vocabulary_id: row['vocabulary'],
        label_human: row['label_human'],
        label_machine: row['label_machine'],
        data_type_id: row['data_type'],
        parent_id: row['parent_property'],
        cardinality: row['cardinality'],
        description: row['description'],
        example_value: row['example_value'],
        uri: row['uri'],
        notes: row['notes']
      )
    end
  end

  def ordered_values
    Value.where(:property_id => id).order(:list_order)
  end
end

class Value < Sequel::Model
  set_primary_key :id
  unrestrict_primary_key
  many_to_one :property

  def self.populate_from_google_csv
    CSV.new(open(GOOGLE_SHEETS_CSV_URLS[self.name]), CSV_PARSING_OPTIONS).each do |row|
      create(
        id: row['id'],
        label: row['label'],
        uri: row['uri'],
        notes: row['notes'],
        vocabulary_id: row['vocabulary'],
        property_id: row['property'],
        list_order: row['list_order']
      )
    end
  end
end


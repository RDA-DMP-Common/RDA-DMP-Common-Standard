require 'sequel'

DB = Sequel.connect(DB_CONNECTION_URL)

if RESET_ALL_DATA then

  DB.drop_table? :attributes
  DB.drop_table? :properties
  DB.drop_table? :vocabularies
  DB.drop_table? :data_types

  DB.create_table? :data_types do
    String :id, :size=>255, :primary_key=>true
    String :label, :size=>255
    String :notes, text: true
  end

  DB.create_table? :vocabularies do
    String :id, :size=>255, :primary_key=>true
    String :label, :size=>255
    String :uri, :size=>255
    String :notes, text: true
    String :vocab_type, :size=>10
  end

  DB.create_table? :properties do
    String :id, :size=>255, :primary_key=>true
    String :parent_id, :size=>255
    String :label_human, :size=>255
    String :label_machine, :size=>255
    String :description, text: true
    String :uri, :size=>255
    String :example_value, text: true
    String :notes, text: true
    String :cardinality, :size=> 5
    foreign_key :vocabulary_id, :vocabularies, :type=>'varchar'
    foreign_key :data_type_id, :data_types, :type=>'varchar'
  end

  # DB.create_table? :attributes do
  #   primary_key :id
  #   String :label_human, :size=>255
  #   String :label_machine, :size=>255
  #   String :example_value, text: true
  #   String :notes, text: true
  #   String :cardinality, :size=> 5
  #   foreign_key :property_id, :properties, :type=>'varchar'
  #   foreign_key :data_type_id, :data_types, :type=>'varchar'
  # end

end
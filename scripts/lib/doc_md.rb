require 'sequel'

class MarkdownDocument

  PROPERTY_COLUMNS = ['Name','Data Type','Cardinality','Notes']

  CARDINALITY_LABELS = {
    '0..1' => 'Zero or One',
    '1' => 'Exactly One',
    '0..n' => 'Zero or More',
    '1..n' => 'One or More'
  }

  def initialize(path,header,footer,root_property)
    @path = path
    @header = header
    @footer = footer
    @content = ''
    @root_property = root_property
  end

  def generate
    @content += "<table><thead><tr>"
    PROPERTY_COLUMNS.each {|col| @content += "<th>#{col}</th>"}
    @content += "</tr></thead>"
    @content += "<tbody>"
    @root_property.children.each do |property|
      @content += "<tr>"
      @content += "<td>#{property.label_machine}</td>"
      @content += "<td>#{property.data_type.label}</td>"
      @content += "<td>#{CARDINALITY_LABELS[property.cardinality]}</td>"
      notes = property.notes
      if !notes | notes == '' then
        notes = '&nbsp;'
      end
      @content += "<td>#{notes}</td>"
      @content += "</tr>"
    end
    @content += "</tbody></table>"
  end

  def write_to_file
    File.open(@path,'w') do |f|
      f.write @header
      f.write @content
      f.write @footer
    end
  end
end



require 'sequel'

class MarkdownDocument

  PROPERTY_COLUMNS = ['Name','Data Type','Cardinality','Notes']

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
      @content += "<td>#{property.cardinality}</td>"
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



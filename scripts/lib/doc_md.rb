require 'sequel'
require 'nokogiri'
require 'rubytree'

class MarkdownDocument

  PROPERTY_COLUMNS = ['Name','Description','Data Type','Cardinality','Example Value']

  CARDINALITY_LABELS = {
    '0..1' => 'Zero or One',
    '1' => 'Exactly One',
    '0..n' => 'Zero or More',
    '1..n' => 'One or More'
  }

  INDENT_SIZE = 2

  def initialize(path,header,footer,root_property)
    @path = path
    @header = header
    @footer = footer
    @content = ''
    @root_property = root_property
    @root_node = build_tree(@root_property)
    @root_node.print_tree
  end

  def generate
    @content += generate_html_tree(@root_node)
    @content += "\n<hr/>\n\n"

    @root_node.each do |node|
      if node.has_children? then
        @content += "<h2 id=\"#{node.name}_table\">Properties in '#{node.content[:machine_name]}'</h2>\n\n"
        @content += generate_table(node.children)
        @content += "\n\n"
      end
    end
  end


  def generate_nested_li(node)
    li = ('  '*node.node_depth)
    if node.has_children? then
      li += "* [#{node.name}](##{node.name}_table)\n"
    else
      li += "* [#{node.name}](##{node.name})\n"
    end
    return li
  end

  def generate_html_tree(start_node)
    html_tree = '<ul>'
    tree_depth = 0
    final_node_depth = 0
    start_node.each do |node|
      final_node_depth = node.node_depth
      if node.node_depth > tree_depth then
        html_tree += '<ul>'
      elsif node.node_depth < tree_depth then
        html_tree += '</ul>'
      end
      tree_depth = node.node_depth
      if node.has_children? then
        html_tree += "<li id=\"#{node.name}_tree\"><a href=\"##{node.name}_table\">#{node.content[:machine_name]}</a></li>"
      else
        html_tree += "<li id=\"#{node.name}_tree\"><a href=\"##{node.name}\">#{node.content[:machine_name]}</a></li>"
      end
    end
    [0..final_node_depth].each { html_tree += '</ul>' }
    html_tree += '</ul>'
    return html_tree
  end

  def generate_table(node_array)
    table_content = "<table style=\"width: 99%;\"><thead><tr>"
    PROPERTY_COLUMNS.each {|col| table_content += "<th>#{col}</th>"}
    table_content += "</tr></thead>"
    table_content += "<tbody>"
    node_array.each do |node|
      table_content += "#{get_node_as_html_table_row(node)}\n"
    end
    table_content += "</tbody></table>"
    return get_formatted_html(table_content)
  end

  def get_formatted_html(raw_html)
    doc = Nokogiri::XML::DocumentFragment.parse(raw_html)
    return doc.to_xml(indent:INDENT_SIZE)
  end


  def build_tree(root_property)
    root_node = Tree::TreeNode.new(root_property.id,get_property_attributes_as_hash(root_property))
    root_node = add_node_to_parent(root_node,root_property)
    return root_node
  end

  def add_node_to_parent(parent_node,parent_property)
    parent_property.children.each do |property|
      new_node = Tree::TreeNode.new(property.id,get_property_attributes_as_hash(property))
      parent_node << new_node
      new_node.content['depth'] = new_node.node_depth
      add_node_to_parent(new_node,property)
    end
    puts
    return parent_node
  end

  def get_property_attributes_as_hash(property)
    {
      :machine_name => property.label_machine,
      :data_type => property.data_type.label,
      :cardinality => CARDINALITY_LABELS[property.cardinality],
      :description => property.description,
      :example_value => property.example_value
    }
  end

  def get_node_as_html_table_row(node)
    html = "<tr><td><a id=\"#{node.name}\" href=\"##{node.name}_tree\">#{node.content[:machine_name]}</a></td>"
    html += "<td>#{process_content_for_table_cell(node.content[:description])}</td>"
    html += "<td>#{process_content_for_table_cell(node.content[:data_type])}</td>"
    html += "<td>#{process_content_for_table_cell(node.content[:cardinality])}</td>"
    html += "<td>#{process_content_for_table_cell(node.content[:example_value])}</td>"
    # html += "<td>"
    #   if !node.content[:attributes].empty?
    #     html += "<table>"
    #     node.content[:attributes].each do |attribute|
    #       html += '<tr>'
    #       html += "<td>#{attribute[:name]}</td>"
    #       html += "<td>#{attribute[:data_type]}</td>"
    #       html += "<td>#{attribute[:cardinality]}</td>"
    #       html += '</tr>'
    #     end
    #     html += "</table>"
    #   end
    # html += "</td>"
    html += "</tr>"
    return html
  end

  def process_content_for_table_cell(content)
    if(content == nil || content == '') then
      return ' '
    else
      return content
    end
  end


  def write_to_file
    File.open(@path,'w') do |f|
      f.write @header
      f.write @content
      f.write @footer
    end
  end
end



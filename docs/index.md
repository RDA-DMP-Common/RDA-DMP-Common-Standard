# UNDER DEVELOPMENT!
<ul><li id="DMP_tree"><a href="#DMP_table">DMP</a></li><ul><li id="contact_tree"><a href="#contact_table">contact</a></li><ul><li id="contact_id_tree"><a href="#contact_id">contact_id</a></li><li id="mbox_tree"><a href="#mbox">mbox</a></li><li id="name_tree"><a href="#name">name</a></li></ul><li id="created_tree"><a href="#created">created</a></li><li id="description_tree"><a href="#description">description</a></li><li id="ethical_issues_exist_tree"><a href="#ethical_issues_exist">ethical_issues_exist</a></li><li id="modified_tree"><a href="#modified">modified</a></li><li id="project_tree"><a href="#project_table">project</a></li><ul><li id="end_tree"><a href="#end">end</a></li><li id="funding_tree"><a href="#funding_table">funding</a></li><ul><li id="funder_id_tree"><a href="#funder_id">funder_id</a></li><li id="funding_status_tree"><a href="#funding_status">funding_status</a></li><li id="grant_id_tree"><a href="#grant_id">grant_id</a></li></ul><li id="start_tree"><a href="#start">start</a></li><li id="title_tree"><a href="#title">title</a></li></ul><li id="title_tree"><a href="#title">title</a></li></ul></ul>
<hr/>

<h2 id="DMP_table">Properties in 'DMP'</h2>

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Description</th>
      <th>Data Type</th>
      <th>Cardinality</th>
      <th>Attributes</th>
    </tr>
  </thead>
  <tbody><tr><td><a id="contact" href="#contact_tree">contact</a></td><td> </td><td>Nested Data Structure</td><td>Exactly One</td><td/></tr>
<tr><td><a id="created" href="#created_tree">created</a></td><td> </td><td>DateTime</td><td>Exactly One</td><td/></tr>
<tr><td><a id="description" href="#description_tree">description</a></td><td> </td><td>String</td><td>Zero or One</td><td/></tr>
<tr><td><a id="ethical_issues_exist" href="#ethical_issues_exist_tree">ethical_issues_exist</a></td><td> </td><td>Term from Controlled Vocabulary</td><td>Exactly One</td><td/></tr>
<tr><td><a id="modified" href="#modified_tree">modified</a></td><td> </td><td>DateTime</td><td>Exactly One</td><td/></tr>
<tr><td><a id="project" href="#project_tree">project</a></td><td>A description of this property, its purpose and any other constraints</td><td>Nested Data Structure</td><td>Zero or More</td><td/></tr>
<tr><td><a id="title" href="#title_tree">title</a></td><td> </td><td>String</td><td>Zero or One</td><td/></tr>
</tbody>
</table>

<h2 id="contact_table">Properties in 'contact'</h2>

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Description</th>
      <th>Data Type</th>
      <th>Cardinality</th>
      <th>Attributes</th>
    </tr>
  </thead>
  <tbody><tr><td><a id="contact_id" href="#contact_id_tree">contact_id</a></td><td> </td><td>String</td><td>Zero or One</td><td><table><tr><td>identifier</td><td>String</td><td>Exactly One</td></tr><tr><td>identifier_type</td><td>String</td><td>Exactly One</td></tr></table></td></tr>
<tr><td><a id="mbox" href="#mbox_tree">mbox</a></td><td> </td><td>String</td><td>Zero or One</td><td/></tr>
<tr><td><a id="name" href="#name_tree">name</a></td><td> </td><td>String</td><td>Zero or One</td><td/></tr>
</tbody>
</table>

<h2 id="project_table">Properties in 'project'</h2>

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Description</th>
      <th>Data Type</th>
      <th>Cardinality</th>
      <th>Attributes</th>
    </tr>
  </thead>
  <tbody><tr><td><a id="end" href="#end_tree">end</a></td><td> </td><td>DateTime</td><td>Zero or One</td><td/></tr>
<tr><td><a id="funding" href="#funding_tree">funding</a></td><td> </td><td>Nested Data Structure</td><td>Zero or One</td><td/></tr>
<tr><td><a id="start" href="#start_tree">start</a></td><td> </td><td>DateTime</td><td>Zero or One</td><td/></tr>
<tr><td><a id="title" href="#title_tree">title</a></td><td> </td><td>String</td><td>Zero or One</td><td/></tr>
</tbody>
</table>

<h2 id="funding_table">Properties in 'funding'</h2>

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Description</th>
      <th>Data Type</th>
      <th>Cardinality</th>
      <th>Attributes</th>
    </tr>
  </thead>
  <tbody><tr><td><a id="funder_id" href="#funder_id_tree">funder_id</a></td><td> </td><td>String</td><td>Zero or One</td><td><table><tr><td>identifier</td><td>String</td><td>Exactly One</td></tr><tr><td>identifier_type</td><td>String</td><td>Exactly One</td></tr></table></td></tr>
<tr><td><a id="funding_status" href="#funding_status_tree">funding_status</a></td><td> </td><td>Term from Controlled Vocabulary</td><td>Zero or One</td><td/></tr>
<tr><td><a id="grant_id" href="#grant_id_tree">grant_id</a></td><td> </td><td>String</td><td>Zero or One</td><td><table><tr><td>identifier</td><td>String</td><td>Exactly One</td></tr><tr><td>identifier_type</td><td>String</td><td>Exactly One</td></tr></table></td></tr>
</tbody>
</table>


this is the footer...
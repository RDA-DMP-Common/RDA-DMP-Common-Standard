# UNDER DEVELOPMENT!
* [DMP](#DMP)
  * [contact](#contact)
  * [created](#created)
  * [description](#description)
  * [ethical_issues_exist](#ethical_issues_exist)
  * [modified](#modified)
  * [project](#project)
    * [funder_id](#funder_id)
    * [funding_status](#funding_status)
    * [grant_id](#grant_id)
  * [title](#title)

<hr/>

## Properties of 'DMP'

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Data Type</th>
      <th>Cardinality</th>
      <th>Notes</th>
    </tr>
  </thead>
  <tbody><tr><td><span id="contact">contact</span></td><td>Nested Data Structure</td><td>Exactly One</td><td> </td></tr>
<tr><td><span id="created">created</span></td><td>DateTime</td><td>Exactly One</td><td> </td></tr>
<tr><td><span id="description">description</span></td><td>String</td><td>Zero or One</td><td> </td></tr>
<tr><td><span id="ethical_issues_exist">ethical_issues_exist</span></td><td>Term from Controlled Vocabulary</td><td>Exactly One</td><td>from a 'dictionary' containing only: 'yes'; 'no'; 'unknown'</td></tr>
<tr><td><span id="modified">modified</span></td><td>DateTime</td><td>Exactly One</td><td> </td></tr>
<tr><td><span id="project">project</span></td><td>Nested Data Structure</td><td>Zero or More</td><td> </td></tr>
<tr><td><span id="title">title</span></td><td>String</td><td>Zero or One</td><td> </td></tr>
</tbody>
</table>
<hr/>

## All Properties

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Data Type</th>
      <th>Cardinality</th>
      <th>Notes</th>
    </tr>
  </thead>
  <tbody><tr><td><span id="DMP">DMP</span></td><td> </td><td> </td><td> </td></tr>
<tr><td><span id="contact">contact</span></td><td>Nested Data Structure</td><td>Exactly One</td><td> </td></tr>
<tr><td><span id="created">created</span></td><td>DateTime</td><td>Exactly One</td><td> </td></tr>
<tr><td><span id="description">description</span></td><td>String</td><td>Zero or One</td><td> </td></tr>
<tr><td><span id="ethical_issues_exist">ethical_issues_exist</span></td><td>Term from Controlled Vocabulary</td><td>Exactly One</td><td>from a 'dictionary' containing only: 'yes'; 'no'; 'unknown'</td></tr>
<tr><td><span id="modified">modified</span></td><td>DateTime</td><td>Exactly One</td><td> </td></tr>
<tr><td><span id="project">project</span></td><td>Nested Data Structure</td><td>Zero or More</td><td> </td></tr>
<tr><td><span id="funder_id">funder_id</span></td><td>String</td><td>Zero or One</td><td>maybe should be mandatory?</td></tr>
<tr><td><span id="funding_status">funding_status</span></td><td>Term from Controlled Vocabulary</td><td>Zero or One</td><td>needs a dictionary?</td></tr>
<tr><td><span id="grant_id">grant_id</span></td><td>String</td><td>Zero or One</td><td>maybe should be mandatory?</td></tr>
<tr><td><span id="title">title</span></td><td>String</td><td>Zero or One</td><td> </td></tr>
</tbody>
</table>
<hr/>


this is the footer...
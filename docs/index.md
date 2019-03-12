# UNDER DEVELOPMENT!
* [DMP](#DMP)
  * [contact](#contact)
    * contact_id
    * mbox
    * name
  * created
  * description
  * ethical_issues_exist
  * modified
  * [project](#project)
    * end
    * [funding](#funding)
      * funder_id
      * funding_status
      * grant_id
    * start
    * title
  * title

<hr/>

<h2 id="#DMP">Properties in 'DMP'</h2>

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Data Type</th>
      <th>Cardinality</th>
      <th>Notes</th>
    </tr>
  </thead>
  <tbody><tr><td>contact</td><td>Nested Data Structure</td><td>Exactly One</td><td> </td></tr>
<tr><td>created</td><td>DateTime</td><td>Exactly One</td><td> </td></tr>
<tr><td>description</td><td>String</td><td>Zero or One</td><td> </td></tr>
<tr><td>ethical_issues_exist</td><td>Term from Controlled Vocabulary</td><td>Exactly One</td><td> </td></tr>
<tr><td>modified</td><td>DateTime</td><td>Exactly One</td><td> </td></tr>
<tr><td>project</td><td>Nested Data Structure</td><td>Zero or More</td><td> </td></tr>
<tr><td>title</td><td>String</td><td>Zero or One</td><td> </td></tr>
</tbody>
</table>
<hr/>

<h2 id="#contact">Properties in 'contact'</h2>

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Data Type</th>
      <th>Cardinality</th>
      <th>Notes</th>
    </tr>
  </thead>
  <tbody><tr><td>contact_id</td><td>String</td><td>Zero or One</td><td> </td></tr>
<tr><td>mbox</td><td>String</td><td>Zero or One</td><td> </td></tr>
<tr><td>name</td><td>String</td><td>Zero or One</td><td> </td></tr>
</tbody>
</table>
<hr/>

<h2 id="#project">Properties in 'project'</h2>

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Data Type</th>
      <th>Cardinality</th>
      <th>Notes</th>
    </tr>
  </thead>
  <tbody><tr><td>end</td><td>DateTime</td><td>Zero or One</td><td> </td></tr>
<tr><td>funding</td><td>Nested Data Structure</td><td>Zero or One</td><td> </td></tr>
<tr><td>start</td><td>DateTime</td><td>Zero or One</td><td> </td></tr>
<tr><td>title</td><td>String</td><td>Zero or One</td><td> </td></tr>
</tbody>
</table>
<hr/>

<h2 id="#funding">Properties in 'funding'</h2>

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Data Type</th>
      <th>Cardinality</th>
      <th>Notes</th>
    </tr>
  </thead>
  <tbody><tr><td>funder_id</td><td>String</td><td>Zero or One</td><td> </td></tr>
<tr><td>funding_status</td><td>Term from Controlled Vocabulary</td><td>Zero or One</td><td> </td></tr>
<tr><td>grant_id</td><td>String</td><td>Zero or One</td><td> </td></tr>
</tbody>
</table>
<hr/>


this is the footer...
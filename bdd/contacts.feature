Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <firstname>, <lastname>, <address>
  When I add the contact to the list
  Then the new contact list is equal to the old list with the added contact

  Examples:
  | firstname  | lastname  | address  |
  | firstname1 | lastname1 | address1 |
  | firstname2 | lastname2 | address2 |


Scenario: Delete a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I delete the contact from the list
  Then the new contact list is equal to the old list without the deleted contact


Scenario Outline: Modify a contact
  Given a non-empty contact list
  Given a random contact from the list
  Given a new data for the chosen contact <firstname>, <lastname>, <address>
  When I modify the contact with new data
  Then the new contact list is equal to the old list with the modified contact

  Examples:
  | firstname            | lastname           | address           |
  | firstname_new        | lastname_new       | address_new       |
  | firstname_refreshed  | lastname_refreshed | address_refreshed |

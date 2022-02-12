# Automation

- Given a document potential-contacts, find and collect all email addresses and phone numbers.
- Phone numbers may be in various formats.(xxx) yyy-zzzz, yyy-zzzz, xxx-yyy-zzzz, etc.
- Phone numbers with missing area code should presume 206
- Phone numbers should be stored in xxx-yyy-zzzz format.
- Once emails and phone numbers are found they should be stored in two separate documents.
- The information should be sorted in ascending order.
- Duplicate entries are not allowed.

## Contributors

- Chris Rarig
- Osborn Del Angel
- Clarissa Pamonicutt
- Arthur Lozano Jr
- Minhang Xie

## Approach

- Using **regex** we isolated the email and phone numbers.
- For formatting we used replace and split methods to ensure xxx-yyy-zzzz format.
- To remove duplication a for loop was used to check whether or not that number was already in the given list
- For ascending order we used the sort method

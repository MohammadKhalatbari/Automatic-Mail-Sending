# Automatic-Mail-Sending
<h1>Automatic Mail Sending with CSV input</h1>
<p>This Python project uses the standard smtplib, EmailMessage, and datetime modules, in addition to pandas and openpyxl to send automated birthday emails.

This program reads from an excel sheet that contains all of person's details. It then sends them an email if today is their day, before making a note in your spreadsheet to say they’ve received their email.

We’ve used the smtplib and EmailMessage modules to create an SSL connection to our email account and message. We’ve then used a pandas dataframe to store spreadsheet-style data within the Python program. Finally, we used date formatting with the datetime module’s .strftime() function.</p>


<p>Important note: since May 2022, Google has tightened its restrictions on ‘less secure apps’ accessing Gmail. You’ll need to follow some extra steps to use this code with your Gmail account. But don’t worry, they’re easy to do, and we’ve listed them for you.

Go to the ‘manage account’ page for your google account
Click on Security
Enable 2FA (use whichever method you prefer)
Click on ‘App Passwords’
Click on ‘Select App’ and select ‘Mail’
Click on ‘Select Device’ & select ‘Other (custom name)’, enter ‘Python Birthday App’
Click on ‘Generate’ then save this password</p>


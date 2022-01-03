# Covid-19 Screening Tool Automation

A selenium project that automates the Ontario Government's Covid-19 screening tool. Currently working on the codes ability to forward the screening result as an email to a desired recipient. Gmail and other email clients know when chrome is under the use of an automated test software so email sign-in gets restricted. Workaround is to just copy the screening result email as a template then use the Simple Mail Transfer Protocol to send the email via Java or Python script. 

NOTE: As the Ontario Government updates the screening tool the bot will most certainly break as it is not programmed dynamically. Each update to the screening tool requires the bot to be updated as well.
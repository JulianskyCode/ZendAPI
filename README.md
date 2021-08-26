**#ZendAPI**
Customer Feedback Analysis via Zendesk API 

This tool is a Python script that delivers a list of tickets from Zendesk that provide valuable feedback, reducing effort of evaluating tickets individually by almost 10x.

**how to use guide**

This tool is a Python script that delivers a list of tickets from Zendesk that provide valuable feedback, reducing effort of evaluating tickets individually by almost 10x.The Python Script heavy relies on a NLP (Natural Language Processing) library.

**P1. Installation**

1. Set yourself up with a Jupyter Notebook:Local: : Make sure you install Python 3https://jupyter.org/installNote
2. Once you’ve followed the install instructions, after you typed in jupyter notebook in the Terminal, a new tab should be opening in your default browser that points out to a Jupyter notebook on localhost.
3. Here you should select:
File New Notebook Python 3;
4. Upload attached notebook “Feedback Analysis via Zendesk (chat) tickets.ipynb”: a. Click on File -> Open
b. Select Upload from top right corner;
c. Select the file you dowloaded (file available bellow) d. Double click on the file.

**P2. Using the tool**

1. Run the notebook by choosing “Kernel Restart & Run All; 2. You’ll see that the script will run;
3. You will see a list of “Keywords”;
4. Choose a Keyword from the list;
5. Add the keywords in the input field when required;
6. Success! You should see a list of tickets, indexed with their subject and each individual link bellow;

**NOTES**

  Currently you’re seeing the outputs of the script. In case you want to play around with the script you’ll see the “Show Code” button. The script is commented and you can change a few things like “since data” of when you want to analyse the ticket, number of keywords, Zendesk categories, etc.
 
**WARNING**
 
 The script requires a NTLK package which will be downloaded and run. The NTLK package will launch an interface which needs to be close manually for the script to be run in some cases. You might see the following interface.
In case it appears, you can simply close it so that the script runs successfully.

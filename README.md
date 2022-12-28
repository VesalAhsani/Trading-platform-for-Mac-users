# Trading_Platform
This platform is just a prototype and many strategies will be added soon! 👍

DO NOT USE IT FOR TRADING AS IT IS.

## For Mac:
This repo discusses the creation of a trading robot application. It covers the advantages and disadvantages of desktop and web applications for this purpose, as well as the key features that should be included in a trading application. The organization and structure of the code for the application is also discussed, including the requirement for connectors for specific exchanges and the use of a code editor. Additionally, the repo covers how to obtain API keys for Binance and Bitmex exchanges and how to use the tkinter library in Python to create a GUI for the application. The use of websocket-client library to create websocket connections, adding data models to improve the code for a Binance connector, adding error handling and reconnection capabilities to a Binance connector, creating a connector for the Bitmex API, and adding various methods to the Bitmex connector to retrieve and manipulate data, place and cancel orders, and handle errors are described. Finally, the main topics of threading in Python, including the threading module, locks, and condition variables, are discussed.

To summarize, the repo addressed the implementation of a trading platform with a strategy component that allows users to input and manage their trading strategies. The component includes two strategies: a TechnicalStrategy and a BreakoutStrategy. The component uses connectors for Binance and Bitmex exchanges to retrieve a list of symbols for an OptionMenu. The switch_strategy method activates or deactivates a strategy and verifies that all mandatory parameters have been input by the user. When a new strategy is selected, the component initializes a new Strategy object based on the selected strategy and retrieves historical data for the strategy. The new Strategy object is then added to the appropriate connector, either Binance or Bitmex. The TechnicalStrategy and BreakoutStrategy include check_signal methods that return an integer indicating a long, short, or no signal based on the price and volume of the current and previous candles. The system also includes a method for checking for signals and opening trades, as well as a method for monitoring the performance of the check_signal method. The open_position method is responsible for sending a market order to buy or sell based on the signal and the trade size, which is calculated as a percentage of the account balance. The system also allows for the option of passing the bid or ask price to the open_position method in order to trade at a specific price.

In summary, if you are using a Mac to run a trading robot application, you may need to adjust some aspects of the appearance to improve the user experience. This may include removing borders around certain elements, such as the logging component, Entry widgets, and OptionMenu, and adjusting the width of the Entry widgets. To change the background color of buttons, you may need to install the tkmacosx library and use it instead of the tk library when initializing buttons. You can also use the borderless argument when initializing buttons to remove borders. These changes will help the application look similar to the version on Windows.

Using the tkmacosx library to change the background color of buttons, removing the white background around the OptionMenu, and setting the border width to -1 for the OptionMenu and 0 for the Entry widgets. It's also recommended adding padding between the columns to separate them and adjusting the width of the widgets to fit the screen size and resolution. The adjustments are necessary because the appearance of tkinter elements can differ between Mac and Windows operating systems.

To open the trading platform outside of Pycharm on a Mac, you need to create a new file with the .command file extension. In the file, you can use the command to navigate to the directory where the start.command file is located and the command that Pycharm uses to start the Python file. However, on Mac, you also need to add the permission for the current user to run the start.command file as an executable. This can be done by opening a Terminal from Pycharm and using the command ```chmod u+x start.command```. The ```u``` refers to the current user, the ```+``` adds a permission, and the ```x``` is the permission to execute. After running this command, the ```start.command``` file will be executable and you can run the platform by double-clicking on the file.

<img width="1057" alt="Screen Shot 2022-12-26 at 6 27 16 PM" src="https://user-images.githubusercontent.com/25235989/209790797-c42e24d5-8aeb-456a-b22f-15a150f1ae3d.png">



SQLite is a popular choice for a database management system, especially for smaller projects or applications where a full-fledged database management system like MySQL or PostgreSQL may be overkill. One of the benefits of using SQLite is that it is self-contained and does not require a separate server process to be running, which makes it easy to set up and use.

To create a connection to an SQLite database in Python, you can use the sqlite3 module, which is part of the Python Standard Library. Here is an example of how you can create a connection to an SQLite database and execute a simple SELECT statement to retrieve data from a table:

```
import sqlite3

# Connect to the database
conn = sqlite3.connect('database.db')

# Create a cursor
cursor = conn.cursor()

# Execute a SELECT statement
cursor.execute('SELECT * FROM table_name')

# Fetch all rows from the SELECT statement
rows = cursor.fetchall()

# Iterate over the rows and print the column values
for row in rows:
    print(row['column_name'])

# Close the connection
conn.close()
```
Using the sqlite3.Row class as you mentioned allows you to access the data in each row as a dictionary, which can be more convenient than accessing the data as a tuple.

As for the DB Browser for SQLite, it is a graphical tool that allows you to view, create, and edit SQLite databases. It is a useful tool for exploring and working with SQLite databases, and can be a helpful tool when you are working with SQLite in your Python projects.



#### Required libraries:
pandas==1.5.2

python_dateutil==2.8.2

requests==2.28.1

tkmacosx==1.0.5

websocket_client==1.4.2

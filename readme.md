# HTML POST Data Sender

This is a basic Python script that sends a POST request containing a 12-word string to a specified endpoint. The script simulates a cryptocurrency wallet passphrase and sends it to the website defined in the code.

The script will generate a random 12-word string, format it, and send it as a POST request to the specified endpoint.

Check the console output to see if the POST request was successful. If there was an error, the error message will be displayed.

The script will continue to run indefinitely, sending a new POST request every second.

## Usage

1. Clone the repository or download the script file.

2. Make sure you have Python installed on your system.

3. Open the script file in a text editor of your choice.

4. Edit the code to specify the desired endpoint URL.

5. Edit the code to reflect the header information captured in 'inspect element'.

6. Save the changes to the script file.

7. Run the script using the following command:

   ```shell
   python main.py

## Requirements
-Python 3.x

-The requests library (install using pip install requests)
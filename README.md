# Telegram File Forwarder Bot

This is a Python-based Telegram bot that forwards files from one Telegram group to multiple other groups. It uses the Telethon library and allows users to dynamically input the source and target group IDs.

## Features

- Forwards files from a source group to multiple target groups.
- Handles duplicate files by deleting them from the target groups.
- Includes rate-limiting to avoid Telegram's flood wait errors.

## Requirements

Make sure you have the following installed:

- Python 3.7+
- Required Python libraries (listed in `requirements.txt`)

## Installation

1. Clone this repository to your local machine.

   ```bash
   git clone https://github.com/yourusername/telegram-file-forwarder.git
   cd telegram-file-forwarder

2.	Install the required Python packages.

pip install -r requirements.txt


3.	Set up your config.py file with your Telegram API credentials:

api_id = 'your_api_id'
api_hash = 'your_api_hash'



Usage

	1.	Run the forward_files.py script.

python forward_files.py


	2.	Enter the source group ID and the target group IDs when prompted.
	3.	The bot will begin forwarding files from the source group to the specified target groups.

Notes

	•	Ensure that your Telegram API credentials are kept secure and are not shared publicly.
	•	Make sure the bot has the necessary permissions in both the source and target groups to send and delete messages.

License

This project is licensed under the MIT License. See the LICENSE file for more details.

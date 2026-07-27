import nuke
import os
import urllib.parse

subject = "Nuke Issue"
description = ""

def open_new_outlook_email(*args):
    # URL-encode the subject and body to handle special characters correctly
    computer = os.environ['COMPUTERNAME']
    project_path = os.path.dirname(nuke.Root().name())
    project_name = os.path.basename(nuke.Root().name())
    version = nuke.NUKE_VERSION_STRING
    #renderer = ""

    recipient = ""
    subject_value = subject
    description_value = description + "\n\nProject Details:\nComputer Name: " + computer + "\nNuke Version: " + version + "\nProject Name: " + project_name + "\nProject Path: " + project_path
    subject_encoded = urllib.parse.quote(subject_value)
    body_encoded = urllib.parse.quote(description_value)

    # Construct the mailto URI
    uri = f'mailto:{recipient}?subject={subject_encoded}&body={body_encoded}'

    # Use os.startfile to open the URI with the default associated application
    try:
        os.startfile(uri)
        print("New email window should open shortly.")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Ensure 'new Outlook' is set as your default email client.")

def main():
    open_new_outlook_email()

if __name__ == '__main__':
    main()
import webbrowser, sys, pyperclip

sys.argv # [mapit.py, ]

# Check if command line arguments were passed
if len(sys.argv) > 1:
    address = " ".join(sys.argv[1:])
else:
    address = pyperclip.paste()

google_maps_address = "https://www.google.com/maps/search/?api=1&query="
to_search = google_maps_address + "+".join(address.split())
webbrowser.open(to_search)
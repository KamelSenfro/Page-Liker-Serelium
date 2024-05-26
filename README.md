# Page-Liker-Serelium
Usage

    Edit the script:

    Open the script file and replace the placeholder text with your actual LinkedIn credentials and the page details.

    python

email.send_keys("Your Email Address")
password.send_keys("Your Password")
search_bar.send_keys("Page Name")
driver.get("Page URL")

Run the script:

bash

    python linkedin_auto_like.py

How It Works

    Log in to LinkedIn:
    The script uses Selenium to open LinkedIn's login page and enters your credentials to log in.

    Navigate to the specified page:
    After logging in, the script searches for the specified page and navigates to it.

    Load all posts:
    The script scrolls down the page to load all posts.

    Like all posts:
    The script locates all the "Like" buttons for the posts and clicks them.

Notes

    Ensure that your LinkedIn credentials and page details are correctly entered in the script.
    The script includes comments for sections that can be ignored or adjusted as needed.
    Modify the time delays (time.sleep) if necessary to accommodate your internet speed and system performance.

Disclaimer

Use this script responsibly. Automating interactions on LinkedIn may violate LinkedIn's terms of service. Use at your own risk.

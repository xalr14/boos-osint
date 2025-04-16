import urllib.request
import json
import time

def banner():
    print(r"""
██████╗  ██████╗  ██████╗ ███████╗
██╔══██╗██╔═══██╗██╔════╝ ██╔════╝
██████╔╝██║   ██║██║  ███╗█████╗  
██╔═══╝ ██║   ██║██║   ██║██╔══╝  
██║     ╚██████╔╝╚██████╔╝███████╗
╚═╝      ╚═════╝  ╚═════╝ ╚══════╝
         Made with 💀 by Abudi
        [boos] Email Finder Tool
""")

def get_json(url):
    try:
        with urllib.request.urlopen(url) as response:
            if response.status == 200:
                return json.loads(response.read().decode())
    except Exception as e:
        print(f"[-] Error fetching {url}: {e}")
    return None

def search_github(username):
    print(f"\n[GitHub] Searching for user: {username}...")
    url = f"https://api.github.com/users/{username}"
    data = get_json(url)
    if data and 'email' in data and data['email']:
        print(f"[+] Found GitHub email: {data['email']}")
        return [data['email']]
    else:
        print("[-] No public email found on GitHub.")
    return []

def search_gravatar(username):
    print(f"\n[Gravatar] Searching for user: {username}...")
    url = f"https://en.gravatar.com/{username}.json"
    data = get_json(url)
    if data and 'entry' in data and 'emails' in data['entry'][0]:
        emails = [e['value'] for e in data['entry'][0]['emails']]
        print(f"[+] Found Gravatar email(s): {emails}")
        return emails
    else:
        print("[-] No Gravatar profile or email found.")
    return []

def check_instagram(username):
    print(f"\n[Instagram] Checking for account: {username}...")
    url = f"https://www.instagram.com/{username}/"
    try:
        with urllib.request.urlopen(url) as response:
            if response.status == 200:
                print(f"[+] Instagram account found: {url}")
                return [url]
    except:
        print("[-] Instagram account not found.")
    return []

def main():
    banner()

    print("\nStarting tool...")
    time.sleep(2)  # Wait for 2 seconds to create suspense

    # Prompt for username
    username = input("\nEnter your username: ")
    print("\nStarting search... Please wait.")

    results = []
    
    # Begin search
    results += search_github(username)
    results += search_gravatar(username)
    results += check_instagram(username)

    # Remove duplicates from results
    results = list(set(results))

    # Display results
    print("\n=== Search Results ===")
    if results:
        for item in results:
            print(f"[+] {item}")
    else:
        print("[-] No data found for the given username.")

if __name__ == "__main__":
    main()

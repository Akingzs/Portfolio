import pyshorteners

def shortener (initial_link):
    bitly_token = 'b007f495f47d066c56b05755c73cbb3c197dcd5a'
    shortener = pyshorteners.Shortener(api_key=bitly_token)

    initial_link = input('Type your link to shorten: ')

    final_link = shortener.bitly.short(initial_link)
    # Show link to click
    print(f'The shortened link is {final_link}')
    # Return the link to assign to any variable
    return final_link


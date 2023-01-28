# import urllib
# use urllib.request to get the data from the url
# write a function that takes a url
# returns a response code


import urllib.request as urllib

print("This is a site connectivity checker program")
input_url = input("Input the url you want to check: ")

def main(url):
    print("Checking connectivity...")

    response = urllib.urlopen(url)
    print("Connected to: ", url, "succesfully" )
    print("the response code was: ", response.getcode())
   

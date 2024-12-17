#Reads token file. Returns false if it fails to read it
def read_token():
    try:
        f=open("token", 'r')
        API_KEY = f.readline().replace('\n', '')
        API_SECRET = f.read()
        f.close()
        return API_KEY, API_SECRET
    except IOError:
        return None, None

#Create token file. Loops until file is create successfully. Assumes perfect user.
def create_token():
    print("Please enter Gate.io API Credentials:\n")
    API_KEY = input("API KEY = ")
    API_SECRET = input("API SECRET = ")
    while True:
        try:
            f=open("token", 'w')
            f.write(API_KEY + '\n' + API_SECRET)
            print("File created successfully.")
            f.close()
            return API_KEY, API_SECRET
            break
        except IOError:
            print("Could not create token file. Please try again.")

import requests
import time

ip = "10.10.43.35"
port = 3010
ipplusport = ip+":"+str(port)
number = 0

data = requests.get("http://"+ipplusport).content
data = data.decode('utf-8')
data = data.split('id="onPort">')[1]
port = data.split('</a></u>.')[0]
print(port)
iteraatio = 1
while port != 9765:
    print(iteraatio)
    content = requests.get("http://"+ip+":"+str(port))
    print(content.status_code)
    print(content.request)
    print(content.ok)
    content = content.content
    operation, operative, port = content.decode('utf-8').split(" ")
    print("OPERAATIO", operation, operative, port)
    if port == "9765":
        print(operation, operative, port)
        break
    if operation == "add":
        print(number, "+", int(operative), "=", number+int(operative))
        number = number + int(operative)
        print("hajookse aina tän plussan jälG")
        time.sleep(4.1)
        continue
    if operation == "minus":
        print(number, "-", int(operative), "=", number-int(operative))
        number = number - int(operative)
        time.sleep(4.1)
        continue
    if operation == "divide":
        print(number, "/", int(operative), "=", number/int(operative))
        number = number / int(operative)
        time.sleep(4.1)
        continue
    if operation == "multiply":
        print(number, "*", int(operative), "=", number*int(operative))
        number = number * int(operative)
        time.sleep(4.1)
        continue
    else:
        print("else?", operation, operative, port)
        time.sleep(4.1)

    print(number)

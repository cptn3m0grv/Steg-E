with open("OIP.jpg", "rb")as file:
    image_orig = file.read()
    message = "\nGargeya Gaurav Asmit Ashish"
    mess_encoded = message.encode('utf-8')
    # print(mess_encoded)
    image_orig = image_orig+mess_encoded+"27".encode("utf-8")
    print(image_orig)

with open("test_file.jpg", "wb")as file:
    file.write(image_orig)

with open("test_file.jpg", "rb")as file:
    print("Digit: ",end="")
    message_len = file.read()[-2:].decode("utf-8")
    print(message_len)
    print(type(message_len))

with open("test_file.jpg", "rb")as file:   
    print(file.read()[-1*(int(message_len)+2):-2].decode("utf-8"))

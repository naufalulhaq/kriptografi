import base64

hexx = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

byetess = bytes.fromhex(hexx)

basee = base64.b64encode(byetess)

print(byetess)
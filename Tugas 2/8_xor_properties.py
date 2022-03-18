KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
KEY12 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
KEY23 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
FKEY123 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

key1_ord = [a for a in bytes.fromhex(KEY1)]
key12_ord = [a for a in bytes.fromhex(KEY12)]
key2_ord = [a ^ b for a, b in zip(key1_ord, key12_ord)]
key23_ord = [a for a in bytes.fromhex(KEY23)]
key3_ord = [a ^ b for a, b in zip(key2_ord, key23_ord)]
fkey123_ord = [a for a in bytes.fromhex(FKEY123)]
flag_ord = [a ^ b ^ c ^ d for a, b, c, d in zip(fkey123_ord, key1_ord, key2_ord, key3_ord)]

flag = "".join(chr(o) for o in flag_ord)
print(flag)
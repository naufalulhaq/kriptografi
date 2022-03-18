bytee = [o for o in bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")]

for i in range(256) :
    mybe_flag_ord = [i ^ o for o in bytee]
    mybe_flag = "".join(chr(o) for o in mybe_flag_ord)
    if mybe_flag.startswith("crypto"):
        break

print(mybe_flag)
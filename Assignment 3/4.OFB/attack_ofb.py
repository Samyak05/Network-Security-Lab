def xor_bytes(b1, b2):
	return bytes(a ^ b for a, b in zip(b1, b2))

c1 = open("ofb_c1.bin", "rb").read()
c2 = open("ofb_c2.bin", "rb").read()
p1 = b"CONFIDENTIAL_DOC"

# Step 1: Recover the keystream using the known plaintext
keystream = xor_bytes(c1, p1)

# Step 2: Use the recovered keystream to decrypt the second ciphertext
p2_recovered = xor_bytes(c2, keystream)

print(f"Recovered Secret: {p2_recovered.decode()}")

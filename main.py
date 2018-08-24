import sys

import anchor
import brute
import tezos

if len(sys.argv) > 1 and sys.argv[1] == "reset":
	anchor.reset()
	sys.exit()

if anchor.exists():
	anchor.load()
	if anchor.data["success"]:
		print("Password is {}. Found in {} guesses.".format(anchor.data["details"]["password"], anchor.data["depth"]))
		sys.exit()
else:
	i = 1
	pattern = input("Please enter a pattern ( like secr(3|e)t(key)?[0-9]{2} ): ")
	anchor.data["parameters"]["pattern"] = pattern

	selected_address = ""
	while len(selected_address) == 0:
		selected_address = input("Please enter your tezos contribution public key (e.g. tz1ABCDeF...): ")
	anchor.data["details"]["address"] = selected_address
	
	selected_email = ""
	while len(selected_email) == 0:
		selected_email = input("Please enter your tezos contribution email address: ")
	anchor.data["details"]["email"] = selected_email
	
	selected_mnemonic = ""
	while len(selected_mnemonic) == 0:
		selected_mnemonic = input("Please enter your tezos contribution mnemonic (e.g. apples cat radio...): ")
	anchor.data["details"]["mnemonic"] = selected_mnemonic

	anchor.save()


def cache(depth):
	anchor.data["depth"] = depth
	anchor.save()

def check(password):
	return tezos.check(anchor.data["details"]["address"], anchor.data["details"]["mnemonic"], anchor.data["details"]["email"], password)


pattern = anchor.data["parameters"]["pattern"]
print("Starting bruteforce with pattern {} ...".format(pattern))

password = brute.force(int(anchor.data["depth"]), pattern, check, cache)
if password:
	print("Password is {}. Found in {} guesses.".format(password[0], password[1]))
	anchor.data["details"]["password"] = password[0]
	anchor.data["success"] = True
	anchor.data["depth"] = int(password[1])
	anchor.save()
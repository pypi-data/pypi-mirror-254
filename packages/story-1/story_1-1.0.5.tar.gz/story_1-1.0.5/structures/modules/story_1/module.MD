


******

Bravo!  You have received a Mercantilism Diploma in "fortunes" from     
the Orbital Convergence University International Air and Water  
Embassy of the 🍊 Planet (the planet that is one ellipse further from  
the Sun than Earth's ellipse).  

You are now officially certified to include "fortunes" in your practice.  

******


# 🎥 
# story_1
for motion picture use, etc.   

---

## description
This is an implementation of possibly one of the most  
secure authentication mechanisms, an edward's elliptic curve 448 (EEC448).   

---

## obtain
`[ZSH] pip install story_1`

---

## key generation
```
import story_1.modules.EEC448.private_key.creator as EEC448_private_key_creator
import story_1.modules.EEC448.public_key.creator as EEC448_public_key_creator

import pathlib
from os.path import dirname, join, normpath
import os

seed = "4986888b11358bf3d541b41eea5daece1c6eff64130a45fc8b9ca48f3e0e02463c99c5aedc8a847686d669b7d547c18fe448fc5111ca88f4e8"
format = "PEM"

private_key_path = normpath (join (pathlib.Path (__file__).parent.resolve (), "EEC448_private_key")) + "." + format
public_key_path = normpath (join (pathlib.Path (__file__).parent.resolve (), "EEC448_public_key")) + "." + format

private_key = EEC448_private_key_creator.create (seed, format, private_key_path)
private_key_instance = private_key ["instance"]
private_key_string = private_key ["string"]

public_key = EEC448_public_key_creator.create (
	private_key_path = private_key_path,
	public_key_path = public_key_path,
	public_key_format = format
)
public_key_instance = public_key ["instance"]
public_key_string = public_key ["string"]
```

---

## signatures and verification

### signatures
```
import story_1.modules.EEC448.sign as sign

unsigned_bytes = b"{}"
signed = sign.start (
	private_key_path = "",
	unsigned_bytes = unsigned_bytes
)

signed_bytes = signed.bytes
```


### verification
```
import story_1.modules.EEC448.verify as verify

unsigned_bytes = b"{}"
signed_bytes = signed.bytes	
	
#
#	returns a boolean 
#
verification_status = verify.start (
	public_key_path = "",
	
	signed_bytes = signed_bytes,
	unsigned_bytes = unsigned_bytes
)
assert (verification_status == True), verification_status

```
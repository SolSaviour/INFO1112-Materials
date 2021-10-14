# Hashing

"A hash function, h, is an efficiently computable mapping of arbitrarily long strings to short fixed length strings."

Let's break this down.

A hash function takes an input and spits out a fixed-length HEXADECIMAL output, usually one of the following lengths (IN BITS): 128, 256, 512.

IT IS A ONE-WAY FUNCTION, IT CANNOT BE REVERSED.w

A common hash function is **SHA256** (secure hash algorithm with 256 bit output).

For example:

```python
m = "Hey Facebook, show me people named Alice"
H(m) = "04671cb9dfab66e0cee793c61384a140f7d2c0fb6610167cf8be54956be034c7"
```

This is the actual SHA256 hash of that string, if you convert it FROM HEX TO BINARY, you'll find it has length 256.

> Hashes are also called MESSAGE DIGESTS and CHECKSUMS. I like to remember this as when you digest food, you cannot get it back to its original form, hence: message digest.

## To Remember

* Hash functions are ONE-WAY functions, they CANNOT be reversed. They are designed to be that way.
* Some are designed to be very fast (e.g. MD5) and some are designed to be very slow (e.g. bcrypt)
* You can assume a unique input will give a unique output (for [**cryptographically secure hash functions**](https://en.wikipedia.org/wiki/Cryptographic_hash_function))

## Why is this important?

Since a hash function is an INJECTIVE function, i.e., it maps distinct inputs to distinct outputs - any message we send online we can send along with its hash!

Why? Well, that way if it has been changed in some way (i.e. tampered with) we can recompute the hash and check. 

In this sense, hashing affords us message integrity. We can verify the integrity of our messages.

If you're interested, here is the exact way we use hashing on the internet: [rfc2660](https://datatracker.ietf.org/doc/html/rfc2660#section-2.4.5)

> The syntax || within MAC = hex(H(Message||[<time>]||<shared key>)) means "append"
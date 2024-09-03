# Assignment 1 - Sha-256 Collision Finder
# Name: Justin Langevin
# Student Number: 8648380
# Date: 2024-05-30
# Description: This program finds a collision for the SHA-256 hash function by generating random plaintexts and computing the hash.

from cryptography.hazmat.primitives import hashes
import random

#Function to compute the limited SHA-256 hash (truncated to 16 bits)
def limited_sha256(data):
    digest = hashes.Hash(hashes.SHA256())
    digest.update(data)
    fullHash = digest.finalize()
    #Truncate to the first 2 bytes (16 bits)
    truncatedHash = fullHash[:2]
    return truncatedHash

#Function to find a collision
def find_collision():
    hashMap = {}
    attempts = 0

    while True:
        attempts += 1
        #Generate a random plaintext
        randomPlainText = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=10))
        randomData = randomPlainText.encode('utf-8')

        #Compute the limited SHA-256 hash
        truncatedHash = limited_sha256(randomData)

        #Check if the hash already exists in the map
        if truncatedHash in hashMap:
            originalPlaintext = hashMap[truncatedHash]
            if originalPlaintext != randomPlainText:
                print(f"Collision found after {attempts} attempts!")
                print(f"Original plaintext: {originalPlaintext}")
                print(f"Colliding plaintext: {randomPlainText}")
                print(f"Truncated hash: {truncatedHash.hex()}")
                break
        else:
            hashMap[truncatedHash] = randomPlainText

#Run the collision finder
find_collision()
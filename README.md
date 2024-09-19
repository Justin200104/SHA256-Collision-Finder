# SHA256-Collision-Finder

cryptographic vulnerabilities when using insufficiently strong hash functions or truncated hash values.

## Cryptographic Hash Functions and Their Role in Cybersecurity

Hash functions, such as **SHA-256 (Secure Hash Algorithm 256)**, are fundamental to many aspects of cybersecurity, including:
- **Data integrity**: Hashes ensure that data has not been altered by producing a unique fingerprint of the data.
- **Password storage**: Instead of storing plaintext passwords, systems often store the hash of the password, ensuring that the original password cannot be easily recovered.
- **Digital signatures**: Hashes play a key role in verifying the authenticity and integrity of data in digital signatures and certificates.

The goal of a cryptographic hash function is to provide **pre-image resistance**, **second pre-image resistance**, and **collision resistance**. However, in this project, we intentionally reduce the security by truncating the SHA-256 hash to just 16 bits to demonstrate how collisions can occur.

## The Problem of Hash Collisions

A **collision** in the context of hash functions occurs when two distinct inputs (plaintexts) generate the same hash output. In a robust cryptographic system, collisions should be extremely difficult to find. However, when hash outputs are truncated or when weak hash functions are used, it becomes feasible to find collisions through brute force.

### Security Implications of Hash Collisions

In real-world cybersecurity, hash collisions can be exploited by attackers in several ways:
- **Digital signature forgery**: If an attacker can find two different documents that produce the same hash, they could substitute a legitimate document (e.g., a signed contract) with a fraudulent one.
- **Certificate forgery**: Collisions can undermine the integrity of certificates used in **Public Key Infrastructure (PKI)** systems. An attacker could forge a certificate and trick users into trusting a malicious entity.
- **Password cracking**: Hash collisions can help attackers in password cracking attempts. If two different passwords produce the same hash, an attacker can bypass password authentication systems.

In this project, the truncation of the hash to 16 bits (2 bytes) makes collisions far easier to find compared to the full 256-bit hash of the standard SHA-256 algorithm. This allows us to simulate the attack in a manageable timeframe, but it also highlights the risks of relying on shortened or weak hash functions.

## How the Project Simulates a Collision Attack

The program is designed to demonstrate a **brute-force attack** for finding a hash collision in a truncated SHA-256 hash function. This is done by repeatedly generating random plaintext strings and checking whether two different plaintexts produce the same truncated hash.

### Steps:
1. **Hash Truncation**: The SHA-256 hash function is used to generate a 256-bit hash, but only the first 16 bits of the hash are considered. This greatly reduces the number of possible unique hashes and increases the likelihood of finding a collision.
2. **Random Plaintext Generation**: The program generates random 10-character plaintext strings, mimicking the kind of brute-force approach that attackers use to find collisions.
3. **Hash Comparison**: The truncated hashes are stored, and each new hash is compared against the stored values to check for a collision. When two different plaintexts produce the same hash, a collision is reported.

### Key Code Functions:
- **`limited_sha256(data)`**: This function generates the SHA-256 hash and truncates it to 16 bits. It simulates a scenario where only a small portion of the hash is used, which is a critical vulnerability.
- **`find_collision()`**: This function implements a brute-force attack, generating random plaintexts, computing their truncated hashes, and searching for collisions.

### Example of a Collision Attack:
If two plaintexts, such as:
"abc123XYZ" and "pQr987uvw"

produce the same 16-bit truncated hash, the program will print both plaintexts and the matching hash value, indicating that a collision has been found. This shows how an attacker could exploit this vulnerability in a real-world system if truncated or weak hash functions were used.

## Cybersecurity Lessons from the Project

1. **Importance of Full-Length Hashes**: Truncating a cryptographic hash, as demonstrated here, drastically reduces its effectiveness. While the full SHA-256 hash space is astronomically large (2^256), truncating the hash to just 16 bits reduces the space to 2^16, making collisions trivial to find through brute force.

2. **Use of Strong Hash Functions**: This project reinforces the importance of using strong, cryptographically secure hash functions like SHA-256 or SHA-3 in their entirety. **Weaker hash functions or truncated hashes** are much more vulnerable to collision attacks.

3. **Brute-Force Feasibility**: In this simulation, we are effectively performing a brute-force attack by generating random plaintexts and searching for collisions. The reduced hash space (due to truncation) makes this feasible for demonstration, but in real systems, brute-force attacks on strong hashes would require immense computational power and time.

4. **Collision Resistance**: A key property of secure hash functions is their **collision resistance**—the difficulty of finding two different inputs that produce the same hash. This project illustrates the importance of maintaining strong collision resistance in any cryptographic system, especially for digital signatures and certificate authorities.

## Conclusion

The **SHA-256 Collision Finder** project demonstrates a fundamental vulnerability in cryptographic systems when hash functions are truncated or weakened. While this program uses a reduced hash space for the sake of demonstration, the underlying principle applies to real-world systems: strong, full-length cryptographic hash functions are crucial to ensuring the integrity and security of data, authentication systems, and digital signatures. This project highlights the need for robust cryptographic practices and serves as a practical example of the dangers of hash collisions in cybersecurity.


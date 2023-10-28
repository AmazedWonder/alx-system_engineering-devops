# SSH

This project focuses on SSH Encryption and Connection Process

### Tasks
asks
0. Use a private key

Bash script that uses ssh to connect to your server using the private key ~/.ssh/school with the user ubuntu.
* Only use ssh single-character flags
* did not use -l
* did not handle the case of a private key protected by a passphrase

1. Create an SSH key pair
Bash script that creates an RSA key pair.

* Name of the created private key is school
* Number of bits in the created key to be created 4096
* The created key is protected by the passphrase betty

2. Client configuration file
Configure it to needs so as to connect to a server without typing a password.
* SSH client configuration is configured to use the private key ~/.ssh/school
* SSH client configuration is configured to refuse to authenticate using a password

3. Let me in!
Added the SSH public key below to your server so that we can connect using the ubuntu user.

ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDNdtrNGtTXe5Tp1EJQop8mOSAuRGLjJ6DW4PqX4wId/Kawz35ESampIqHSOTJmbQ8UlxdJuk0gAXKk3Ncle4safGYqM/VeDK3LN5iAJxf4kcaxNtS3eVxWBE5iF3FbIjOqwxw5Lf5sRa5yXxA8HfWidhbIG5TqKL922hPgsCGABIrXRlfZYeC0FEuPWdr6smOElSVvIXthRWp9cr685KdCI+COxlj1RdVsvIo+zunmLACF9PYdjB2s96Fn0ocD3c5SGLvDOFCyvDojSAOyE70ebIElnskKsDTGwfT4P6jh9OBzTyQEIS2jOaE5RQq4IB4DsMhvbjDSQrP0MdCLgwkN



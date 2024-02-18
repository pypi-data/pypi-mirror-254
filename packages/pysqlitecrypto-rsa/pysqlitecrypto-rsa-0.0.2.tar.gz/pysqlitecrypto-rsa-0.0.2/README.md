# Pysqlitecrypto-RSA

Pysqlitecrypto-RSA is a Python package that provides functionalities for RSA key generation, encryption, and decryption using SQLite storage.



## Installation

To install Pysqlitecrypto-RSA, you can use pip:

```bash
pip install pysqlitecrypto-rsa
```

Make sure you have Python 3.x installed.

## Usage

You can use Pysqlitecrypto-RSA in your Python projects by importing the necessary functions:

```python
from pysqlitecrypto_rsa import generate_keys, encrypt_message, decrypt_message

# Generate RSA keys with a specified key size
key_size = 1024
generate_keys(key_size)

# Encrypt a message
encrypted_message = encrypt_message("Your message here")

# Decrypt the encrypted message
decrypted_message = decrypt_message(encrypted_message)
```

### Note:

- The `generate_keys` function requires the key size to be passed as an argument. For example, `generate_keys(1024)` generates RSA keys with a key size of 1024 bits.
- The `generate_keys` function creates a folder called '.keychain' in the home directory, and inside it, a keys.db file is 
  created to store the RSA keys.

## License

Pysqlitecrypto-RSA is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.

import base64
import zlib
import codecs

# Fungsi untuk meng-encode file Python
def encode_file(input_file, output_file):
    with open(input_file, 'rb') as f:
        content = f.read()
    
    # Langkah-langkah encoding
    compressed_content = zlib.compress(content)  # Compress data
    base64_content = base64.b64encode(compressed_content)  # Base64 encode
    encoded_content = codecs.encode(base64_content, 'hex')  # Hex encoding

    # Simpan hasil encoding ke file
    with open(output_file, 'wb') as f:
        f.write(encoded_content)

    print (f"File '{input_file}' berhasil di-encode menjadi '{output_file}'.")


# Contoh penggunaan
input_file = "input.py"  # Ganti dengan nama file Python Anda
output_file = "encoded_output.txt"
encode_file(input_file, output_file)

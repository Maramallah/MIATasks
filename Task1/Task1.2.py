class Codec:
    def encode(self, commands):

        encoded_list = []
        for cmd in commands:
            # will encode by -2 from ascii
            shifted = ''.join(chr(ord(c) - 2) for c in cmd)
            encoded_list.append(shifted)
            # used this letter because it`ll never be encoded(in ascii)
        return '§'.join(encoded_list)

    def decode(self, encoded_str):

        parts = encoded_str.split('§')
        decoded_list = []
        for part in parts:
            # return it by +2 from ascii
            shifted_back = ''.join(chr(ord(c) + 2) for c in part)
            decoded_list.append(shifted_back)
        return decoded_list


codec = Codec()

commands = ["Push", "Box,box", "", "Check temps"]
print ("Commands:", commands)
print()
encoded = codec.encode(commands)
# print("Encoded:", encoded)
# print()
decoded = codec.decode(encoded)
print("Decoded:", decoded)

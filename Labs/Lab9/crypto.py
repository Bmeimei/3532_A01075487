from des import DesKey
import argparse
from abc import ABC, abstractmethod
from enum import Enum
import ast


class CryptoMode(Enum):
    """
    Lists the various modes that the Crypto application can run in.
    """
    # Encryption mode
    EN = "en"
    # Decryption Mode
    DE = "de"


class Request:
    """
    The request object represents a request to either encrypt or decrypt
    certain data. The request object comes with certain accompanying
    configuration options as well as a field that holds the result. The
    attributes are:
        - encryption_state: 'en' for encrypt, 'de' for decrypt
        - data_input: This is the string data that needs to be encrypted or
        decrypted. This is None if the data is coming in from a file.
        - input_file: The text file that contains the string to be encrypted or
        decrypted. This is None if the data is not coming from a file and is
        provided directly.
        - output: This is the method of output that is requested. At this
        moment the program supports printing to the console or writing to
        another text file.
        - key: The Key value to use for encryption or decryption.
        - result: Placeholder value to hold the result of the encryption or
        decryption. This does not usually come in with the request.

    """

    def __init__(self):
        self.encryption_state = None
        self.data_input = None
        self.input_file = None
        self.output = None
        self.key = None
        self.result = None

    def __str__(self):
        return f"Request: State: {self.encryption_state}, Data: {self.data_input}" \
               f", Input file: {self.input_file}, Output: {self.output}, " \
               f"Key: {self.key}"


class BaseHandler(ABC):

    def __init__(self, next_handler: 'BaseHandler' = None) -> None:
        """
        Constructs a handler.
        """
        self.next_handler = next_handler

    @abstractmethod
    def handle_request(self, request: Request) -> (str, bool):
        pass

    def set_handler(self, handler: "BaseHandler") -> None:
        self.next_handler = handler


class EncryptStringHandler(BaseHandler):

    def handle_request(self, request: Request) -> (str, bool):
        if not request.data_input and request.input_file:
            return self.next_handler.handle_request(request)

        key = DesKey(request.key.encode('utf-8'))
        request.result = key.encrypt(request.data_input.encode('utf-8'), padding=True)

        if self.next_handler is None:
            return "", True
        return self.next_handler.handle_request(request)


class DecryptStringHandler(BaseHandler):

    def handle_request(self, request: Request) -> (str, bool):
        if not request.data_input and request.input_file:
            return self.next_handler.handle_request(request)

        key = DesKey(request.key.encode('utf-8'))
        request.result = key.decrypt(ast.literal_eval(request.data_input), padding="True")

        if self.next_handler is None:
            return "", True
        return self.next_handler.handle_request(request)


class EncryptFileHandler(BaseHandler):
    def handle_request(self, request: Request) -> (str, bool):
        if request.data_input and not request.input_file:
            return self.next_handler.handle_request(request)

        key = DesKey(request.key.encode('utf-8'))
        try:
            with open(request.input_file, 'rb') as file_object:
                request.result = key.encrypt(file_object.read(), padding=True)
            if self.next_handler is None:
                return "", True
            return self.next_handler.handle_request(request)

        except FileNotFoundError:
            return f"{request.input_file} not exist!", False


class DecryptFileHandler(BaseHandler):

    def handle_request(self, request: Request) -> (str, bool):
        if request.data_input and not request.input_file:
            return self.next_handler.handle_request(request)

        key = DesKey(request.key.encode('utf-8'))
        try:
            with open(request.input_file, 'r') as file_object:
                request.result = key.decrypt(ast.literal_eval(file_object.read()), padding=True)
            if self.next_handler is None:
                return "", True
            return self.next_handler.handle_request(request)

        except FileNotFoundError:
            return f"{request.input_file} not exist!", False


class OutputHandler(BaseHandler):

    def handle_request(self, request: Request) -> (str, bool):
        if request.output == "print":
            print(request.result)
        else:
            with open(request.output, "wb") as file_object:
                file_object.write(request.result)
        if self.next_handler is None:
            return "", True
        return self.next_handler.handle_request(request)


class Crypto:

    def __init__(self) -> None:
        encrypt_string_handler = EncryptStringHandler()
        encrypt_file_handler = EncryptFileHandler()
        encrypt_output_handler = OutputHandler()

        encrypt_string_handler.set_handler(encrypt_file_handler)
        encrypt_file_handler.set_handler(encrypt_output_handler)

        decrypt_string_handler = DecryptStringHandler()
        decrypt_file_handler = DecryptFileHandler()
        decrypt_output_handler = OutputHandler()

        decrypt_string_handler.set_handler(decrypt_file_handler)
        decrypt_file_handler.set_handler(decrypt_output_handler)

        self.encryption_start_handler = encrypt_string_handler
        self.decryption_start_handler = decrypt_string_handler

    def execute_request(self, request: Request) -> None:
        if bool(request.data_input) == bool(request.input_file):
            print("Error: Must contain either input string or input file!")
            return None
        if request.encryption_state == CryptoMode.EN:
            result = self.encryption_start_handler.handle_request(request)
        else:
            result = self.decryption_start_handler.handle_request(request)
        if not result[1]:
            print(result[0])


def setup_request_commandline() -> Request:
    """
    Implements the argparse module to accept arguments via the command
    line. This function specifies what these arguments are and parses it
    into an object of type Request. If something goes wrong with
    provided arguments then the function prints an error message and
    exits the application.
    :return: The object of type Request with all the arguments provided
    in it.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("key", help="The key to use when encrypting or "
                                    "decrypting. This needs to be of "
                                    "length 8, 16 or 24")
    parser.add_argument("-s", "--string", help="The string that needs to be "
                                               "encrypted or decrypted")
    parser.add_argument("-f", "--file", help="The text file that needs to be"
                                             "encrypted or decrypted")
    parser.add_argument("-o", "--output", default="print",
                        help="The output of the program. This is 'print' by "
                             "default, but can be set to a file name as well.")
    parser.add_argument("-m", "--mode", default="en",
                        help="The mode to run the program in. If 'en' (default)"
                             " then the program will encrypt, 'de' will cause "
                             "the program to decrypt")
    try:
        args = parser.parse_args()
        request = Request()
        request.encryption_state = CryptoMode(args.mode)

        request.data_input = args.string

        request.input_file = args.file

        request.output = args.output

        request.key = args.key
        print(request)
        return request
    except Exception as e:
        print(f"Error! Could not read arguments.\n{e}")
        quit()


def main(request: Request):
    crypto = Crypto()
    crypto.execute_request(request)


if __name__ == '__main__':
    request = setup_request_commandline()
    main(request)

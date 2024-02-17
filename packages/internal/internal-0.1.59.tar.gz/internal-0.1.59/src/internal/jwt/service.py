# import base64
# import json
# from typing import Union
#
# from cryptography.hazmat.backends import default_backend
# from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
# from fastapi import HTTPException
# from fastapi.security import OAuth2PasswordBearer
# from jose import JWTError, jwt
#
# from jwt.const import JWT_AES_KEY, JWT_AES_IV
# from jwt.interface import JWTUserInterface, JWTTokenInterface
#
# oauth2_scheme_user = OAuth2PasswordBearer(tokenUrl=f"auth/user/cruisys_token")
#
#
# class JWTService:
#     @staticmethod
#     async def create_jwt_token(data: dict, app_config) -> str:
#         jwt_user_interface = JWTUserInterface(**data)
#         cipher_str = await JWTService.encrypt_aes_plain(jwt_user_interface)
#         jwt_token_interface = JWTTokenInterface(data=cipher_str)
#         token = jwt.encode(jwt_token_interface.to_dict(), app_config.JWT_SECRET_KEY,
#                            algorithm=app_config.JWT_ALGORITHM)
#         return token
#
#     @staticmethod
#     async def decode_jwt_token(token: str, app_config) -> Union[dict, JWTUserInterface, HTTPException]:
#         try:
#             payload = jwt.decode(token, app_config.JWT_SECRET_KEY, algorithms=[app_config.JWT_ALGORITHM])
#             plain_obj = await JWTService.decrypt_aes_cipher(JWTTokenInterface(**payload))
#             jwt_user_interface = JWTUserInterface(**plain_obj)
#             return jwt_user_interface
#         except JWTError:
#             raise HTTPException(status_code=401, detail="Invalid token")
#
#     @staticmethod
#     async def encrypt_aes_plain(interface: JWTUserInterface):
#         plaintext = json.dumps(interface.to_dict()).encode('utf-8')
#
#         cipher = Cipher(algorithms.AES(JWT_AES_KEY.encode('utf-8')), modes.CFB(JWT_AES_IV.encode('utf-8')),
#                         backend=default_backend())
#         encryptor = cipher.encryptor()
#         ciphertext = encryptor.update(plaintext) + encryptor.finalize()
#
#         return base64.b64encode(ciphertext).decode('utf-8')
#
#     @staticmethod
#     async def decrypt_aes_cipher(interface: JWTTokenInterface):
#         ciphertext = base64.b64decode(interface.data)
#
#         cipher = Cipher(algorithms.AES(JWT_AES_KEY.encode('utf-8')), modes.CFB(JWT_AES_IV.encode('utf-8')),
#                         backend=default_backend())
#         decryptor = cipher.decryptor()
#         plaintext = decryptor.update(ciphertext) + decryptor.finalize()
#
#         return json.loads(plaintext.decode('utf-8'))

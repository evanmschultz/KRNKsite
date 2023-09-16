# import jwt # pip install pyjwt
# from config.jwt_config import SECRET_KEY, ALGORITHM # We will need to create a .env file at some point.

# def create_access_token(data: dict, expires_delta: int): # An integer representing the number of minutes from the current time when the JWT should expire. This parameter is used to set the expiration time for the token.
#     to_encode = data.copy() # copy the data so we don't modify the original
#     to_encode.update({"exp": expires_delta}) # add the expiration time to the payload
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM) # encode the JWT
#     return encoded_jwt # return the JWT

# def decode_token(token: str): # decode the JWT
#     try: # try to decode the JWT
#         decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]) # decode the JWT
#         return decoded_token # return the decoded JWT
#     except jwt.JWTError: # if there is an error decoding the JWT
#         return None # return None
import json
from flask import request, _request_ctx_stack
from functools import wraps
from jose import jwt
from urllib.request import urlopen


AUTH0_DOMAIN = 'vamsichanakya.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'Casting_Agency'

'''
AuthError Exception
A standardized way to communicate auth failure modes
'''

class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code

"""Auth Header"""

def get_token_auth_header():
    """get the header from the request"""
    """raise an AuthError if no header is present"""
    auth_header = request.headers.get('Authorization', None)
    if not auth_header:
        raise AuthError({
            'code': 'auth_header_missing',
            'description': 'Authorization header is required.'
        }, 401)

    auth_parts = auth_header.split()

    if auth_parts[0].lower() != 'bearer':
        raise AuthError({
            'code': 'header_invalid',
            'description': 'Bearer Token not found in Auth Header'
        }, 401)

    elif len(auth_parts) == 1:
        raise AuthError({
            'code': 'header_invalid',
            'description': 'Token not found.'
        }, 401)

    elif len(auth_parts) > 2:
        raise AuthError({
            'code': 'header_invalid',
            'description': 'Authorization header must be bearer token.'
        }, 401)

    auth_token = auth_parts[1]

    return auth_token

'''
    INPUTS :
    permission: string permission 
    payload   : decoded jwt payload
'''

def check_permissions(permission, payload):
    """raise an AuthError if permissions are not included in the payload"""
    if 'permissions' not in payload:
        raise AuthError({
            'code': 'permissions_not_in_payload',
            'description': 'Permissions expected in payload'
        }, 400)

    """raise an AuthError if the requested permission string is not in the payload permissions array"""
    if permission not in payload['permissions']:
        raise AuthError({
            'code': 'not_authorized',
            'description': 'Permission not found.'
        }, 401)
    return True

'''
    INPUTS
    auth_token: a json web auth_token (string)
'''

def verify_decode_jwt(auth_token):
    """Verify and decode the JWT using the Auth0 secret."""
    jsonurl = urlopen(f'https://{AUTH0_DOMAIN}/.well-known/jwks.json')
    jwks = json.loads(jsonurl.read())
    unverified_header = jwt.get_unverified_header(auth_token)
    rsa_key = {}
    if 'kid' not in unverified_header:
        raise AuthError({
            'code': 'header_invalid',
            'description': 'Unable to find appropriate key'
        }, 401)

    for key in jwks['keys']:
        if key['kid'] == unverified_header['kid']:
            rsa_key = {'kty': key['kty'], 'kid': key['kid'], 'use': key['use'], 'n': key['n'], 'e': key['e']
            }
    if rsa_key:
        try:
            payload = jwt.decode(auth_token, rsa_key, algorithms=ALGORITHMS, audience=API_AUDIENCE,
                issuer='https://' + AUTH0_DOMAIN + '/'
            )

            return payload

        except jwt.ExpiredSignatureError:
            raise AuthError({
                'code': 'token_expired',
                'description': 'Token expired.'
            }, 401)

        except jwt.JWTClaimsError:
            raise AuthError({
                'code': 'invalid_claims',
                'description': 'Incorrect claims.\
                Please, check the audience and issuer.'
            }, 401)
        except Exception:
            raise AuthError({
                'code': 'invalid_header',
                'description': 'Unable to parse authentication token.'
            }, 400)
    raise AuthError({
                'code': 'invalid_header',
                'description': 'Unable to find the appropriate key.'
    }, 400)

'''
    INPUTS
    permission: string permission
    return the decorator which passes the decoded payload to the decorated method
'''

def requires_auth(permission=''):
    """A decorater for authentication."""
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            """Validate and check permission from JWT."""
            auth_token = get_token_auth_header()
            payload = verify_decode_jwt(auth_token)
            check_permissions(permission, payload)
            return f(payload, *args, **kwargs)
        return wrapper
    return requires_auth_decorator

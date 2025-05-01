import unittest
from flask import Flask
# Assuming your class is in a file named 'my_module.py'
from flask_jwt_decorator import parser
from flask_jwt_decorator import parsed_token

class TestDefaultJWTParser(unittest.TestCase):

    def setUp(self):
        # Create a test Flask app
        self.app = Flask(__name__)
        # Configure the app for testing (example)
        self.app.config['JWT_SECRET_KEY'] = """-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEA5z4JITLvn8OnZ3euy+fg
qkta2C79EvuF70L5rSTZmHX/vDmgji/rS0A6f6UrHaVSGKyIYzMxekOWm93nEiJA
Kk5DvHntlt5abH/dgejP/kDZUMKB1GJ9Oa4jpyLVG+JdkrUSCUF0bHqwbe1z46nq
YS5jp6epIeBRkOyN2uch/pDEp1EoyozilALZYXjbyUVR6/dt3TDeocRTwmnWqPW5
qWOQO3KPx0xV4aCrhahb1GqiN0PRRgzLZNK1JNDmJPKFfXu+eNfDB8IwE2sxAbrD
FX8kvQsbv7zwF9E24hxhIap2qu/tXc5IpAiCVNGm3BBDHgJw+6v2M6VqTVYA7/ky
QXZnEvh64NuqKqKxDWX/aG7RRYqn3JjKzsyslbSdgQjGtpaA7f6/5ktNREi7vRlx
dS0CeMTBUVjULbLet1BVW3gzt6164UYWF15ujStZMRRCWjKIxR8zInSw8CHEhddF
ixj0cXO4WcjmwyvyaepAOmcHirx6AlHyCvizWwBz/aQBtgHGca9smc4bIjA1rn9r
bfOhBrM29nORWBXgNd81EdgakaNLJ8Ps/GNbilPlpdAOZ9q7QOrOiOlEf2fgERQB
/w+Iri8jwTtONaHb/vdZO4Z1necLDo+1lCSoxf2iSLbkBlXSb2D7oJM4srHyFMN8
m6jgQ0l4WfT+2b0WUHVXX7UCAwEAAQ==
-----END PUBLIC KEY-----"""

    def test_my_method(self):
      with self.app.app_context():
        # Instantiate your class within the context
        my_instance = parser.DefaultJWTParser()
        # Call a method that uses current_app
        token='eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxNTg4ODAwMzA0IiwianRpIjoiZTJiNWUzNmI0NTFjMWQ2YzBiY2I3NmEwMmU1ODk5NDZmYzQ0OGVjMzEzNDdjOWQ5ZjlkYzczYzQ1ZDJkMzg3ZmUwZGI5M2I3ZmZkZWE3ZTAiLCJpYXQiOjE3NDYxMTkwNTAuMTgwMDc1LCJuYmYiOjE3NDYxMTkwNTAuMTgwMDc3LCJleHAiOjE3NDYyMDU0NTAuMTY4NjY2LCJzdWIiOiIxYjIxODFjYS0yOWVhLTRmOGItYTc5MS02ZTc4YTNkNzJiZTUiLCJzY29wZXMiOlsiZG9ub3IiXX0.C67ueajuMH2pkklgMMhp8RF1T_rwgJQz5j_FXuIQ6t4Zl04pBnN_wcDa2aeXx1-nFGYc0_I1jbvC6XqVxaNkR-1ThkSLwCoEGMNhS8Z1DvF8ZNZLuNz9QQOyUfobPhqGwH9FRil2lobA3Zi7vAU-gBInsOSLKI6hWvABofUHCc0eZS9WETcPV75H8iK5snk8m0ijsDUHcxsjbP1SVp1Wi4mBHRUQriFel_jO64qhhddn4gB75GnjRjiQnhIdAReON44IBupcR-WdA1vivHGxIoVQrbpeGCcWlOfVPu5BSTbttTMdpOZYSSLcFZwvcFbZa_iStTVPGXE4MUNHVV8Mz7HOUq59ZYtsPCJpnk370Bqb4wP5zj-jqPAsowB-Rc6sXbAva2LVt1QR928lEm6HJf3cOz055sHrTAILWFGUap1fDMuhMhO_8-f0L2yNgHYWhVUIsMOeD3ZiQSATgqsjNO_zsGV6h81xva1UcTIVxfpgKpIpszm0xpBq7rAwvcbo2jFnHODzmjgOBxoNcbC98j0nrIwiWvmcu3r2-eEzGrg4G3d-VRuSjwuroWTNrmlj1wdJ2ViGKVsgYUTOp22dZ6RTyDxybaIpG4oDNGdq0Dp3-uuuPyfUAI-phoGxLn8CN0d3WnMylNB9Y1f0xUmk4apeypDXY1G4QhyDiZr1dqs'
        expected_claim={'aud': '1588800304', 'jti': 'e2b5e36b451c1d6c0bcb76a02e589946fc448ec31347c9d9f9dc73c45d2d387fe0db93b7ffdea7e0', 'iat': 1746119050.180075, 'nbf': 1746119050.180077, 'exp': 1746205450.168666, 'sub': '1b2181ca-29ea-4f8b-a791-6e78a3d72be5', 'scopes': ['donor']}
        expected_token = parsed_token.ParsedToken(expected_claim)

        # Assert the expected result

        result = my_instance.parse(token)

        print(result)
        self.assertEqual(result.to_dict(), expected_token.to_dict())


if __name__ == '__main__':
    unittest.main()


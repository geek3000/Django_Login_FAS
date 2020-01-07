import requests as r
import json


submit_info = {"redirect_uris": ["http://localhost:8000/oidc/callback/"],
               "application_type": "native",
               "token_endpoint_auth_method":"client_secret_post"}

headers = {'Content-type': 'application/json'}

print("Get Openid Provider info")

if True:
    client_info=r.post('https://iddev.fedorainfracloud.org/openidc/Registration', data=json.dumps(submit_info), headers=headers).json()
    print(client_info)
    with open('client_secrets.json', 'w') as f:
        f.write(json.dumps(client_info))
else:
    print("Cant get credentials!")

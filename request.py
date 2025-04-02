import http.client

host = "agiluscrm.com.br"
port = 40000
conn = http.client.HTTPSConnection(host, port)
conn.request("GET", "/api/empresas/listar", headers={"Host": host})
response = conn.getresponse()
print(response.status, response.reason)

import json
resultado = json.loads(response.read().decode())
for empresa in resultado:
    print(empresa['Nome'])

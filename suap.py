from urllib.request import Request, urlopen
import json

MATRICULA = '20151014050037	'
TOKEN = 'CjAf06Vv30WrqhIJsr4LWV27TpbtxfQteBnam9xtgoqOMoJtbIDHWtrjyf82Vp75'
AUTHORIZATION = 'Basic MjAxNTEwMTQwNTAwMjU6SXRhbGlhQDEyMw=='

req = Request('https://suap.ifrn.edu.br/api/v2/edu/alunos/{}/'.format(MATRICULA))
req.add_header('Accept', 'application/json')
req.add_header('X-CSRFToken', TOKEN)
req.add_header('Authorization', AUTHORIZATION)

dados_byte = urlopen(req).read()
dados_txt = dados_byte.decode('utf-8')
print(dados_txt) 

import requests
# url = "https://lemon.lemonstudio.tech:8443/50999ced2d425236b3fdb814c674e6b4test/f782d741bf2d505f825662e1361a846f/restful/v1/hello_stream"
# url = "http://localhost:9999"
url = "http://localhost:7001/restful/v1/hello_stream"
with requests.post(url, headers={"Accept-Encoding": "identity", "X-Accel-Buffering": "no"}, stream = True) as resp:
    for line in resp.iter_content():
        if line:
            print(line)
    print(resp.headers)

"curl -X POST -N 'http://localhost:7001/restful/v1/hello_stream'"
"curl -X POST -N 'http://localhost:7000/50999ced2d425236b3fdb814c674e6b4test/f782d741bf2d505f825662e1361a846f/restful/v1/hello_stream'"
"curl -X POST -N 'http://localhost:7000/50999ced2d425236b3fdb814c674e6b4test/f782d741bf2d505f825662e1361a846f/restful/v1/hello_stream'"

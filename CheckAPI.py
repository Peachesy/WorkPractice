import requests

def get_method(url, para, headers):
    try:
        req = requests.get(url=url, params=para, headers=headers)

    except Exception as e:
        print(e)
    else:
        if req.status_code == 200:
            return req
        else:
            print("接口返回状态码：", req.status_code)
            print("Request Failed")

if __name__ == '__main__':
    url = "https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fadmin.microsoft.com%2FAdminportal%2FHome%23%2FSettings%2FServices%2F%3A%2FSettings%2FL1%2FBingNews&data=02%7C01%7Cv-yutao1%40microsoft.com%7C8ddbd70f05d6483f8c8b08d836edd5e1%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C637319742419733907&sdata=p0dzEtaRb0CVTaXVAuIeBMwFRqbaj0JAHj11cvG9gFI%3D&reserved=0"

req = get_method(url=url, para=None, headers=None)
print(req)
print(req.status_code)
print(req.text)
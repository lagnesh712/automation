import jsonpath
import json
from test_requests.api_reqs import Api_req

rqst=Api_req()
get_response = rqst.get_req()
post_responce=rqst.post_req()
delete_responce=rqst.delete_req()
put_responce=rqst.put_req()

def test_get_1():
    value = get_response.status_code
    assert value == 200


def test_get_2():
    total_books = json.loads(get_response.text)
    total = jsonpath.jsonpath(total_books, 'total_pages')
    assert total[0] == 2


def test_post_1():
    status_code=post_responce.status_code
    assert status_code==201


def test_post_2():
    text = json.loads(post_responce.text)
    var_name = jsonpath.jsonpath(text, "name")
    assert var_name[0] == "lagnesh"


def test_delete_1():
    statuscode=delete_responce.status_code
    assert statuscode==204


def test_delete_2():
    delete_text=delete_responce.text
    assert delete_text==""


def test_put_1():
    statuscode=put_responce.status_code
    assert statuscode==200


def test_put_2():
    text = json.loads(put_responce.text)
    var_name = jsonpath.jsonpath(text, "name")
    assert var_name[0]=="bot"



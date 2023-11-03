import json
import math
import requests


def find_procedure():
    url = (
        "https://prozorro.sale/auction/?status=complete&size=100&raw_data=1&page=")
    print(url)
    portal_api_response = requests.get(url)
    data_api = json.loads(portal_api_response.text)
    count = 1
    array_new = []
    print("Count of iteration ---", math.ceil(data_api["current_count"] / 100))
    for j in range(1, math.ceil(data_api["current_count"] / 100) + 1):
        print("Iteration - ", j)
        url_stream = url + str(j)
        print(url_stream)
        portal_api_response = requests.get(url_stream)
        data_api = json.loads(portal_api_response.text)
        for i in range(0, len(data_api["payload"])):
            procedure_id = data_api["payload"][i]["hunam_id"]
            object_id = data_api["payload"][i]["id"]
            url_procedure = "https://procedure.prozorro.sale/api/procedures/" + object_id
            if data_api["payload"][i]["source_name"] == "cbd3":
                if len(data_api["payload"][i]["awards"]) == 2:
                    if data_api["payload"][i]["awards"][1]["status"] == "cancelled":
                        if data_api["payload"][i]["procedure_type"] not in array_new:
                            print(count, " - ", procedure_id, " - ", data_api["payload"][i]["procedure_type"], " - ", url_procedure)
                            count = count + 1
            array_new.append(data_api["payload"][i]["procedure_type"])
    print(array_new)

find_procedure()

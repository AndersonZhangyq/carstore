import json
import pandas as pd
import requests


def convert(lng, lat):
    response = requests.get(
        "https://restapi.amap.com/v3/assistant/coordinate/convert",
        params={
            "key": "285bb075fa2162099ab2dec4538d6860",
            "coordsys": "baidu",
            # "sig": "cdcbb652e62a58dbc6a1693f086edbc4",
            "locations": "{},{}".format(lng, lat),
        },
    )
    return response.json()
    pass


if __name__ == "__main__":
    ret = {}
    # AION
    with open("广汽埃安.json", encoding="utf-8") as f:
        data = json.load(f)
    standard = []
    for ele in data:
        converted = convert(ele["lng"], ele["lat"])
        if int(converted["status"]) != 1:
            print(ele)
            print(converted)
        else:
            standard.append(
                {
                    "type": "AION",
                    "name": ele["fullname"],
                    "address": ele["address"],
                    "lng": float(converted["locations"].split(',')[0]),
                    "lat": float(converted["locations"].split(',')[1]),
                }
            )
    ret["AION"] = standard

    # Beijing
    with open("北京汽车.json", encoding="utf-8") as f:
        data = json.load(f)
    standard = []
    for ele in data:
        converted = convert(ele["longitude"], ele["latitude"])
        if int(converted["status"]) != 1:
            print(ele)
            print(converted)
        else:
            standard.append(
                {
                    "type": "Beijing",
                    "name": ele["dealerName"],
                    "address": ele["dealerAddress"],
                    "lng": float(converted["locations"].split(',')[0]),
                    "lat": float(converted["locations"].split(',')[1]),
                }
            )
    ret["Beijing"] = standard

    # R
    with open("R汽车.json", encoding="utf-8") as f:
        data = json.load(f)
    standard = []
    for ele in data:
        converted = convert(ele["lng"], ele["lat"])
        if int(converted["status"]) != 1:
            print(ele)
            print(converted)
        else:
            standard.append(
                {
                    "type": "R",
                    "name": ele["centerName"],
                    "address": ele["address"],
                    "lng": float(converted["locations"].split(',')[0]),
                    "lat": float(converted["locations"].split(',')[1]),
                }
            )
    ret["R"] = standard

    # JiHe
    with open("几何汽车.json", encoding="utf-8") as f:
        data = json.load(f)
    standard = []
    for ele in data:
        standard.append(
            {
                "type": "JiHe",
                "name": ele["DealerName"],
                "address": ele["Address"],
                "lng": float(ele["Coordinates"].split(",")[0]),
                "lat": float(ele["Coordinates"].split(",")[1]),
            }
        )
    ret["JiHe"] = standard

    # LingPao
    with open("零跑汽车.json", encoding="utf-8") as f:
        data = json.load(f)
    standard = []
    for ele in data:
        standard.append(
            {
                "type": "JiHe",
                "name": ele["name"],
                "address": ele["site"],
                "lng": float(ele["areaShopLocation"].split(",")[0]),
                "lat": float(ele["areaShopLocation"].split(",")[1]),
            }
        )
    ret["LingPao"] = standard

    with open("standard.json", "w+", encoding="utf-8") as f:
        json.dump(ret, f, ensure_ascii=False)

    df = pd.DataFrame([i for v in ret.values() for i in v])
    df["coordinates"] = df["lng"].astype(str) + "," + df["lat"].astype(str)
    df.drop(df.columns[[-3, -2]], axis=1, inplace=True)
    df.to_csv("standard_all.csv", index=False)
    for key, value in ret.items():
        df = pd.DataFrame(value)
        df["coordinates"] = df["lng"].astype(str) + "," + df["lat"].astype(str)
        df.drop(df.columns[[-3, -2]], axis=1, inplace=True)
        df.to_csv("standard_{}.csv".format(key), index=False)

import json

import requests
from global_mapping import bf6


def main():
    res = requests.get(
        "https://api.gametools.network/bf6/translations?lang=en-US"
    ).json()
    translations = res.get("localizedTexts", [])
    test = {}
    new = {}

    for translation in translations:
        test[translation.get("localizedText", "")] = translation.get("sid")

    for name, values in bf6.GADGETS.items():
        name_field = values.get("gadgetName", None)
        if name_field not in test:
            print(name)
        values["translationId"] = test.get(name_field, None)
        new[name] = values

    with open("temp/changes.json", "w", encoding="utf-8") as f:
        json.dump(new, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()

import requests


def main():
    languages = [
        "en-US",
        "en-GB",
        "ar-SA",
        "de-DE",
        "es-ES",
        "es-MX",
        "fr-FR",
        "it-IT",
        "ja-JP",
        "ko-KR",
        "pl-PL",
        "pt-BR",
        "zh-CN",
        "zh-TW",
    ]
    for language in languages:
        res = requests.get(
            f"https://api.gametools.network/bf6/translations?lang={language}"
        ).json()
        translations = res.get("localizedTexts", [])

        res = {}
        for item in translations:
            res[item.get("sid")] = item.get("localizedText")
        with open(
            "global_mapping/readability/bf6/languages/settingValues/"
            + language.replace("-", "_").lower()
            + ".py",
            "w",
            encoding="utf-8",
        ) as f:
            f.write(f"translation = {res}")


if __name__ == "__main__":
    main()

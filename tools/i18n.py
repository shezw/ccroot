# read json from configs/i18n files
# return a dict
import json
import os
from typing import List

configs_dir = os.getenv("CC_ROOT_CONFIGS_DIR")
current_lang = "en-us"

all_i18n = {}


class CC_I18n:
    def __init__(self, lang):
        global current_lang
        global configs_dir
        # check if the dict json file exists
        # the file name is i18n/{lang}.json
        if not os.path.exists(f"{configs_dir}/i18n/{lang}.json"):
            # specific language to en-us
            current_lang = "en-us"

        self.dict = json.load(open(f"{configs_dir}/i18n/{current_lang}.json"))
        all_i18n[current_lang] = self

    def trans(self, key_id):
        return self.dict[key_id] if key_id in self.dict else key_id

    def get_dict(self):
        if self.dict is None:
            return
        return self.dict


def i18n(key_id, lang=None):
    global current_lang
    if lang is None:
        lang = current_lang

    # check if the i18n object exists in all_i18n
    if lang not in all_i18n:
        CC_I18n(lang)

    return all_i18n[lang].trans(key_id)

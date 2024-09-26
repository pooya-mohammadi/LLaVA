from argparse import ArgumentParser
from os.path import join
import os
from typing import Any

from deep_utils import JsonUtils, DirUtils

# choose_n_data = 100

mapping = dict(user="human", assistant="gpt")


def map_role(conversation):
    conversation['from'] = mapping.get(conversation['from'], conversation['from'])
    return conversation

parser = ArgumentParser()

parser.add_argument("--input", default="cardiac.json")
parser.add_argument("--output", default="llava_v1_5_mix665k_cardiac.json")
args = parser.parse_args()


if __name__ == '__main__':
    input_file_path = args.input
    output_file = args.output


    dct = JsonUtils.load(input_file_path)

    def update_conversation(it):
        it['conversations'] = it['conversations'][4:]
        if not len(it['conversations']):
            print(it)
            return None
        it['conversations'] = [map_role(conversation) for conversation in it['conversations']]
        conversation = it['conversations'][0]
        if conversation['from'] != "human":
            print(it)
            return None
        value = conversation['value']
        if not value.startswith("<image>\n"):
            conversation['value'] = "<image>\n" + conversation['value']
        return it


    output_dct = [update_conversation(item) for item in dct]
    output_dct = [item for item in output_dct if item]
    JsonUtils.dump(output_file, output_dct)
    print(f"original dct: {len(dct)}, filtered: {len(output_dct)}")

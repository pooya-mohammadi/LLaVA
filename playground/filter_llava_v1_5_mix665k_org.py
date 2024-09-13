from os.path import join
import os

from deep_utils import JsonUtils

if __name__ == '__main__':
    img_dir = "data/textvqa/train_images"
    output_file = "llava_v1_5_mix665k_textvqa.json"
    dct = JsonUtils.load("data/llava_v1_5_mix665k_org.json")
    textvqa_list = [join("textvqa/train_images", item) for item in list(os.listdir(img_dir))]
    output_dct = [item for item in dct if item.get("image", "").startswith("textvqa") and item.get("image", "NO WAY") in textvqa_list]
    JsonUtils.dump(output_file, output_dct)
    print(f"[INFO] len(output_dct): {len(output_dct)}, len(os.listdir()): {len(textvqa_list)}")

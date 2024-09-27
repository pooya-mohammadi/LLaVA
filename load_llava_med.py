# Load model directly
from transformers import AutoModelForCausalLM, AutoConfig, LlavaConfig
from os.path import join

# path = "../LLaVA-Med/llava-v1.6-mistral-7b"
path = "liuhaotian/llava-v1.5-13b"
# config = LlavaConfig.from_pretrained(join(path, "config.json"))
# config, kwargs = AutoConfig.from_pretrained(
#     path,
#     return_unused_kwargs=True,
# )
# print(config)
# model = AutoModelForCausalLM.from_pretrained(path, config=config)
model = AutoModelForCausalLM.from_pretrained(path)

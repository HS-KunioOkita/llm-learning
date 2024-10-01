from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("abeja/gpt2-large-japanese")
tokenizer.tokenize("今日は天気が良いので")


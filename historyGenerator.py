import os
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Указываем путь для кэширования на диске D
cache_dir = "D:/huggingface_cache"

# Создаем директорию, если она не существует
os.makedirs(cache_dir, exist_ok=True)

# Устанавливаем переменную окружения для Hugging Face, чтобы кэшировалось на диске D
os.environ["TRANSFORMERS_CACHE"] = cache_dir

# Проверим, что переменная окружения установлена корректно
print("Hugging Face cache is set to:", os.environ["TRANSFORMERS_CACHE"])

# Загружаем модель и токенизатор
tokenizer = GPT2Tokenizer.from_pretrained("sberbank-ai/rugpt3large_based_on_gpt2")
model = GPT2LMHeadModel.from_pretrained("sberbank-ai/rugpt3large_based_on_gpt2")

# Текст для генерации
input_text = "В постапокалиптическом мире,"

# Преобразуем текст в токены
inputs = tokenizer(input_text, return_tensors="pt", padding=True, truncation=True)

# Генерация текста
outputs = model.generate(
    inputs["input_ids"], 
    attention_mask=inputs["attention_mask"], 
    max_length=200, 
    num_return_sequences=1
)

# Преобразуем токены обратно в текст
generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(generated_text)

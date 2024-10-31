# This file is used to search for poems in the JSON file of all the Tang poems.
# Quoting the json file of 300 Tang poems downloaded from github
import json

# Define the JSON file path
json_file_path = 'E:/python assignment/python_assignment_ChenTong_24059827G/python_assignment03_ChenTong_24059827G/.venv/allTangPoetry/300TangPoetry.json'

# Function to read JSON file and search for poems
def search_poetry(keyword):
    with open(json_file_path, 'r', encoding='utf-8') as file:
        poetry_data = json.load(file)  # Load JSON data

    results = []  # List used to store search results
    for poem in poetry_data:
        # Check if the keyword is in the poem title or content
        if keyword in poem.get('title', '') or keyword in poem.get('paragraphs', ''):
            results.append(poem)  # Add matching poems to the result list

    return results

# Main loop to continuously search for poems
while True:
    # User input keywords
    keyword = input("請輸入搜索關鍵詞（输入'q'退出）：")
    if keyword.lower() == 'q':  # Check if user wants to quit
        break

    found_poems = search_poetry(keyword)

    # Print search results
    if found_poems:
        for index, poem in enumerate(found_poems, start=1):
            print(f"\n{index}. 標題：{poem['title']}\n作者：{poem['author']}\n内容：{poem['paragraphs']}\n")
    else:
        print("沒有找到匹配的詩詞。")
    print()  # Print a newline for better readability

print("程序已退出。")

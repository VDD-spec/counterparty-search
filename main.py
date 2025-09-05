import requests
import json
import os
from datetime import datetime
from config import API_KEY, ENDPOINT

def search_counterparty_info(query):
    """Поиск информации о контрагенте через Qwen API"""
    if not API_KEY:
        return "Ошибка: API ключ не найден!"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "qwen-turbo",
        "input": {
            "prompt": f"Найди информацию о контрагенте: {query}. Включи в ответ: официальное название, ИНН, ОГРН, адрес, руководителя, основной вид деятельности."
        },
        "parameters": {
            "max_tokens": 1500,
            "temperature": 0.7
        }
    }

    try:
        response = requests.post(ENDPOINT, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        
        result = response.json()
        return result["output"]["text"]
    except Exception as e:
        return f"Ошибка при запросе: {str(e)}"

def save_result(query, result):
    """Сохранение результата в файл"""
    if not os.path.exists('results'):
        os.makedirs('results')
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"results/result_{timestamp}.txt"
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"Запрос: {query}\n")
        f.write("="*50 + "\n")
        f.write(result)
    
    return filename

def main():
    print("🔍 Программа поиска информации о контрагенте")
    print("="*50)
    
    while True:
        query = input("\nВведите данные о контрагенте (или 'выход' для завершения): ")
        
        if query.lower() in ['выход', 'exit', 'quit']:
            break
            
        print("Ищу информацию...")
        result = search_counterparty_info(query)
        
        print("\nРезультат:")
        print("-"*50)
        print(result)
        
        filename = save_result(query, result)
        print(f"\n✅ Результат сохранен в файл: {filename}")

if __name__ == "__main__":
    main()

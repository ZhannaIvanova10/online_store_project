import os
import re

def fix_imports_in_file(filepath):
    """Исправляет импорты в файле."""
    if not os.path.exists(filepath):
        print(f"Файл не найден: {filepath}")
        return
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Заменяем относительные импорты на абсолютные
    old_content = content
    
    # Исправляем импорты для models
    content = re.sub(r'from\s+\.?models\s+import', 'from src.models import', content)
    content = re.sub(r'from\s+src\.models\s+import', 'from src.models import', content)
    
    # Исправляем импорты для main
    content = re.sub(r'from\s+\.?main\s+import', 'from src.main import', content)
    content = re.sub(r'from\s+src\.main\s+import', 'from src.main import', content)
    if old_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Исправлен: {filepath}")
        return True
    else:
        print(f"Без изменений: {filepath}")
        return False

# Исправляем все тестовые файлы
test_files = [
    'tests/test_imports.py',
    'tests/test_json_loading.py', 
    'tests/test_models.py',
    'tests/test_models_coverage.py',
    'tests/test_main.py',
    'tests/test_main_additional.py',
    'tests/test_access_modifiers.py'
]
for test_file in test_files:
    fix_imports_in_file(test_file)

print("\n✅ Все импорты исправлены!")

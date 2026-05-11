import sys
from pathlib import Path

# Добавляем корень проекта в PYTHONPATH
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.services.processor import DataProcessor











import pytest
from app.services.processor import DataProcessor


@pytest.fixture
def processor():
    """Возвращает свежий экземпляр DataProcessor для каждого теста."""
    return DataProcessor()


@pytest.fixture
def valid_transaction():
    """Возвращает шаблон валидной транзакции."""
    return {
        "id": "t_100",
        "amount": "500.50",
        "category": "Sales",
        "date": "2023-12-01"
    }

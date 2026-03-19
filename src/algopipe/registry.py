from typing import Dict, List, Type, Any

class BaseModule:
    """The template for every algorithm/step in the library."""
    name: str = "Base"
    category: str = "Uncategorized"
    subcategory: str = "General"  # New field
    description: str = ""

    def get_imports(self) -> List[str]:
        return []

    def get_code(self, variable_name: str) -> str:
        raise NotImplementedError

class Registry:
    # New Structure: { "Category": { "SubCategory": { "ModuleName": ModuleClass } } }
    _registry: Dict[str, Dict[str, Dict[str, Type[BaseModule]]]] = {}

    @classmethod
    def register(cls, category: str, subcategory: str = "General"):
        """Decorator now accepts a subcategory!"""
        def wrapper(wrapped_class):
            if category not in cls._registry:
                cls._registry[category] = {}
            
            if subcategory not in cls._registry[category]:
                cls._registry[category][subcategory] = {}
            
            module_name = wrapped_class.name
            cls._registry[category][subcategory][module_name] = wrapped_class
            
            # Attach metadata to class
            wrapped_class.category = category
            wrapped_class.subcategory = subcategory
            
            return wrapped_class
        return wrapper

    @classmethod
    def get_categories(cls) -> List[str]:
        return list(cls._registry.keys())

    @classmethod
    def get_subcategories(cls, category: str) -> List[str]:
        """Get list of sub-folders (e.g., 'Handling Missing Values', 'Encoding')"""
        return list(cls._registry.get(category, {}).keys())

    @classmethod
    def get_modules(cls, category: str, subcategory: str) -> List[str]:
        """Get modules inside a specific sub-category"""
        return list(cls._registry.get(category, {}).get(subcategory, {}).keys())

    @classmethod
    def get_module(cls, category: str, subcategory: str, module_name: str) -> BaseModule:
        return cls._registry[category][subcategory][module_name]()
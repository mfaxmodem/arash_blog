from typing import Any, Iterable, List, Optional, Type

class GenericAPIView:
    filter_backends: List[Type[Any]]
    
    def filter_queryset(self, queryset: Any) -> Any:
        ...
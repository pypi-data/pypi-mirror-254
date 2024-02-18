from ..core import NamedDataset

__docformat__ = "google"


def load_dataset(name: str) -> NamedDataset:
    if not name.startswith("inno:"):
        raise ValueError(f"The method can only load from INNO dataset hub, but requested {name}")
    raise NotImplementedError("Innodata Dataset Hub")

from typing import List, Optional

from typing_extensions import Literal

def _delete_all(force: Optional[Literal[True]]) -> None: ...
def _delete_by_id(id_numbers: List[str]) -> None: ...
def main(*, id_numbers: List[str], nuke: bool, force: Optional[Literal[True]]) -> None: ...

from dataclasses import dataclass
from typing import Optional

from olive.types.blockchain_format.sized_bytes import bytes32
from olive.util.ints import uint64
from olive.util.streamable import Streamable, streamable


@dataclass(frozen=True)
@streamable
class CCParent(Streamable):
    parent_name: bytes32
    inner_puzzle_hash: Optional[bytes32]
    amount: uint64

from clvm.casts import int_from_bytes
from clvm_tools import binutils

from olive.consensus.block_rewards import calculate_base_farmer_reward, calculate_pool_reward
from olive.types.blockchain_format.program import Program
from olive.types.condition_opcodes import ConditionOpcode
from olive.util.bech32m import decode_puzzle_hash, encode_puzzle_hash
from olive.util.condition_tools import parse_sexp_to_conditions
from olive.util.ints import uint32

address1 = "txol1ypzsr2z4ykw3xr4tlsm2mvg9az48a48e3z8y97eg2le3hzwj2nnqulw346"  # Gene wallet (m/12381/8444/2/42):
address2 = "txol1ypzsr2z4ykw3xr4tlsm2mvg9az48a48e3z8y97eg2le3hzwj2nnqulw346"  # Mariano address (m/12381/8444/2/0)

ph1 = decode_puzzle_hash(address1)
ph2 = decode_puzzle_hash(address2)

pool_amounts = int(calculate_pool_reward(uint32(0)) / 2)
farmer_amounts = int(calculate_base_farmer_reward(uint32(0)) / 2)

assert pool_amounts * 2 == calculate_pool_reward(uint32(0))
assert farmer_amounts * 2 == calculate_base_farmer_reward(uint32(0))


def make_puzzle(amount: int) -> int:
    puzzle = f"(q . ((51 0x{ph1.hex()} {amount}) (51 0x{ph2.hex()} {amount})))"
    # print(puzzle)

    puzzle_prog = Program.to(binutils.assemble(puzzle))
    print("Program: ", puzzle_prog)
    puzzle_hash = puzzle_prog.get_tree_hash()

    solution = "()"
    prefix = "xol"
    print("PH", puzzle_hash)
    print(f"Address: {encode_puzzle_hash(puzzle_hash, prefix)}")

    result = puzzle_prog.run(solution)
    error, result_human = parse_sexp_to_conditions(result)

    total_olive = 0
    if error:
        print(f"Error: {error}")
    else:
        assert result_human is not None
        for cvp in result_human:
            assert len(cvp.vars) == 2
            total_olive += int_from_bytes(cvp.vars[1])
            print(
                f"{ConditionOpcode(cvp.opcode).name}: {encode_puzzle_hash(cvp.vars[0], prefix)},"
                f" amount: {int_from_bytes(cvp.vars[1])}"
            )
    return total_olive


total_olive = 0
print("Pool address: ")
total_olive += make_puzzle(pool_amounts)
print("\nFarmer address: ")
total_olive += make_puzzle(farmer_amounts)

assert total_olive == calculate_base_farmer_reward(uint32(0)) + calculate_pool_reward(uint32(0))

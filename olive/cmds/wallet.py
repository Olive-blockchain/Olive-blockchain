from typing import Optional

import click


@click.group("wallet", short_help="Manage your wallet")
def wallet_cmd() -> None:
    pass


@wallet_cmd.command("get_transaction", short_help="Get a transaction")
@click.option(
    "-wp",
    "--wallet-rpc-port",
    help="Set the port where the Wallet is hosting the RPC interface. See the rpc_port under wallet in config.yaml",
    type=int,
    default=None,
)
@click.option("-f", "--fingerprint", help="Set the fingerprint to specify which wallet to use", type=int)
@click.option("-i", "--id", help="Id of the wallet to use", type=int, default=1, show_default=True, required=True)
@click.option("-tx", "--tx_id", help="transaction id to search for", type=str, required=True)
@click.option("--verbose", "-v", count=True, type=int)
def get_transaction_cmd(wallet_rpc_port: Optional[int], fingerprint: int, id: int, tx_id: str, verbose: int) -> None:
    extra_params = {"id": id, "tx_id": tx_id, "verbose": verbose}
    import asyncio
    from .wallet_funcs import execute_with_wallet, get_transaction

    asyncio.run(execute_with_wallet(wallet_rpc_port, fingerprint, extra_params, get_transaction))


@wallet_cmd.command("get_transactions", short_help="Get all transactions")
@click.option(
    "-wp",
    "--wallet-rpc-port",
    help="Set the port where the Wallet is hosting the RPC interface. See the rpc_port under wallet in config.yaml",
    type=int,
    default=None,
)
@click.option("-f", "--fingerprint", help="Set the fingerprint to specify which wallet to use", type=int)
@click.option("-i", "--id", help="Id of the wallet to use", type=int, default=1, show_default=True, required=True)
@click.option(
    "-o",
    "--offset",
    help="Skip transactions from the beginning of the list",
    type=int,
    default=0,
    show_default=True,
    required=True,
)
@click.option("--verbose", "-v", count=True, type=int)
def get_transactions_cmd(wallet_rpc_port: Optional[int], fingerprint: int, id: int, offset: int, verbose: bool) -> None:
    extra_params = {"id": id, "verbose": verbose, "offset": offset}
    import asyncio
    from .wallet_funcs import execute_with_wallet, get_transactions

    asyncio.run(execute_with_wallet(wallet_rpc_port, fingerprint, extra_params, get_transactions))


@wallet_cmd.command("send", short_help="Send olive to another wallet")
@click.option(
    "-wp",
    "--wallet-rpc-port",
    help="Set the port where the Wallet is hosting the RPC interface. See the rpc_port under wallet in config.yaml",
    type=int,
    default=None,
)
@click.option("-f", "--fingerprint", help="Set the fingerprint to specify which wallet to use", type=int)
@click.option("-i", "--id", help="Id of the wallet to use", type=int, default=1, show_default=True, required=True)
@click.option("-a", "--amount", help="How much olive to send, in XOL", type=str, required=True)
@click.option(
    "-m",
    "--fee",
    help="Set the fees for the transaction, in XOL",
    type=str,
    default="0",
    show_default=True,
    required=True,
)
@click.option("-t", "--address", help="Address to send the XOL", type=str, required=True)
@click.option(
    "-o", "--override", help="Submits transaction without checking for unusual values", is_flag=True, default=False
)
def send_cmd(
    wallet_rpc_port: Optional[int], fingerprint: int, id: int, amount: str, fee: str, address: str, override: bool
) -> None:
    extra_params = {"id": id, "amount": amount, "fee": fee, "address": address, "override": override}
    import asyncio
    from .wallet_funcs import execute_with_wallet, send

    asyncio.run(execute_with_wallet(wallet_rpc_port, fingerprint, extra_params, send))


@wallet_cmd.command("show", short_help="Show wallet information")
@click.option(
    "-wp",
    "--wallet-rpc-port",
    help="Set the port where the Wallet is hosting the RPC interface. See the rpc_port under wallet in config.yaml",
    type=int,
    default=None,
)
@click.option("-f", "--fingerprint", help="Set the fingerprint to specify which wallet to use", type=int)
def show_cmd(wallet_rpc_port: Optional[int], fingerprint: int) -> None:
    import asyncio
    from .wallet_funcs import execute_with_wallet, print_balances

    asyncio.run(execute_with_wallet(wallet_rpc_port, fingerprint, {}, print_balances))


@wallet_cmd.command("get_address", short_help="Get a wallet receive address")
@click.option(
    "-wp",
    "--wallet-rpc-port",
    help="Set the port where the Wallet is hosting the RPC interface. See the rpc_port under wallet in config.yaml",
    type=int,
    default=None,
)
@click.option("-i", "--id", help="Id of the wallet to use", type=int, default=1, show_default=True, required=True)
@click.option("-f", "--fingerprint", help="Set the fingerprint to specify which wallet to use", type=int)
def get_address_cmd(wallet_rpc_port: Optional[int], id, fingerprint: int) -> None:
    extra_params = {"id": id}
    import asyncio
    from .wallet_funcs import execute_with_wallet, get_address

    asyncio.run(execute_with_wallet(wallet_rpc_port, fingerprint, extra_params, get_address))


@wallet_cmd.command(
    "delete_unconfirmed_transactions", short_help="Deletes all unconfirmed transactions for this wallet ID"
)
@click.option(
    "-wp",
    "--wallet-rpc-port",
    help="Set the port where the Wallet is hosting the RPC interface. See the rpc_port under wallet in config.yaml",
    type=int,
    default=None,
)
@click.option("-i", "--id", help="Id of the wallet to use", type=int, default=1, show_default=True, required=True)
@click.option("-f", "--fingerprint", help="Set the fingerprint to specify which wallet to use", type=int)
def delete_unconfirmed_transactions_cmd(wallet_rpc_port: Optional[int], id, fingerprint: int) -> None:
    extra_params = {"id": id}
    import asyncio
    from .wallet_funcs import execute_with_wallet, delete_unconfirmed_transactions

    asyncio.run(execute_with_wallet(wallet_rpc_port, fingerprint, extra_params, delete_unconfirmed_transactions))
    
async def do_recover_pool_nft(contract_hash: str, launcher_hash: str, fingerprint: int):
    from .wallet_funcs import get_wallet

    contract_hash_bytes32 = hexstr_to_bytes(contract_hash)
    delay = 604800

    config = load_config(DEFAULT_ROOT_PATH, "config.yaml")
    self_hostname = config["self_hostname"]
    rpc_port = config["full_node"]["rpc_port"]
    wallet_rpc_port = config["wallet"]["rpc_port"]
    node_client = await FullNodeRpcClient.create(self_hostname, uint16(rpc_port), DEFAULT_ROOT_PATH, config)
    wallet_client = await WalletRpcClient.create(self_hostname, uint16(wallet_rpc_port), DEFAULT_ROOT_PATH, config)

    coin_records = await node_client.get_coin_records_by_puzzle_hash(contract_hash_bytes32, False)

    # expired coins
    coins = [coin_record.coin for coin_record in coin_records if coin_record.timestamp <= int(time.time()) - delay]
    if not coins:
        print("no expired coins")
        return
    print("found", len(coins), "expired coins, total amount:", sum(coin.amount for coin in coins))
    wallet_client_f = await get_wallet(wallet_client, fingerprint=fingerprint)
    tx = await wallet_client_f.recover_pool_nft(launcher_hash, contract_hash, coins)
    await node_client.push_tx(tx)
    print("tx pushed")


@wallet_cmd.command("recover_pool_nft", short_help="Recover coins in pool nft contract")
@click.option(
    "--contract-hash",
    help="Set the nft contract hash",
    type=str,
    default=None,
)
@click.option(
    "--launcher-hash",
    help="Set the launcher hash, you should get it from chia wallet",
    type=str,
    default=None,
)
@click.option("-f", "--fingerprint", help="Set the fingerprint to specify which wallet to use", type=int)
def recover_pool_nft(contract_hash: str, launcher_hash: str, fingerprint: int):
    import asyncio

    asyncio.run(do_recover_pool_nft(contract_hash, launcher_hash, fingerprint))


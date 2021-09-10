from setuptools import setup

dependencies = [
    "blspy==1.0.5",  # Signature library
    "chiavdf==1.0.2",  # timelord and vdf verification
    "chiabip158==1.0",  # bip158-style wallet filters
    "chiapos==1.0.4",  # proof of space
    "clvm==0.9.7",
    "clvm_rs==0.1.8",
    "clvm_tools==0.4.3",
    "aiohttp==3.7.4",  # HTTP server for full node rpc
    "aiosqlite==0.17.0",  # asyncio wrapper for sqlite, to store blocks
    "bitstring==3.1.7",  # Binary data management library
    "colorlog==5.0.1",  # Adds color to logs
    "concurrent-log-handler==0.9.19",  # Concurrently log and rotate logs
    "cryptography==3.4.7",  # Python cryptography library for TLS - keyring conflict
    "keyring==23.0.1",  # Store keys in MacOS Keychain, Windows Credential Locker
    "keyrings.cryptfile==1.3.4",  # Secure storage for keys on Linux (Will be replaced)
    #  "keyrings.cryptfile==1.3.8",  # Secure storage for keys on Linux (Will be replaced)
    #  See https://github.com/frispete/keyrings.cryptfile/issues/15
    "PyYAML==5.4.1",  # Used for config file format
    "setproctitle==1.2.2",  # Gives the olive processes readable names
    "sortedcontainers==2.3.0",  # For maintaining sorted mempools
    "websockets==8.1.0",  # For use in wallet RPC and electron UI
    "click==7.1.2",  # For the CLI
    "dnspython==2.1.0",  # Query DNS seeds
]

upnp_dependencies = [
    "miniupnpc==2.2.2",  # Allows users to open ports on their router
]

dev_dependencies = [
    "pytest",
    "pytest-asyncio",
    "flake8",
    "mypy",
    "black",
    "aiohttp_cors",  # For blackd
    "ipython",  # For asyncio debugging
]

kwargs = dict(
    name="olive-blockchain",
    description="Olive blockchain full node, farmer, timelord, and wallet.",
    url="https://oliveblockchain.co/",
    license="Apache License",
    python_requires=">=3.7, <4",
    keywords="olive blockchain node",
    install_requires=dependencies,
    setup_requires=["setuptools_scm"],
    extras_require=dict(
        uvloop=["uvloop"],
        dev=dev_dependencies,
        upnp=upnp_dependencies,
    ),
    packages=[
        "build_scripts",
        "olive",
        "olive.cmds",
        "olive.clvm",
        "olive.consensus",
        "olive.daemon",
        "olive.full_node",
        "olive.timelord",
        "olive.farmer",
        "olive.harvester",
        "olive.introducer",
        "olive.plotting",
        "olive.pools",
        "olive.protocols",
        "olive.rpc",
        "olive.server",
        "olive.simulator",
        "olive.types.blockchain_format",
        "olive.types",
        "olive.util",
        "olive.wallet",
        "olive.wallet.puzzles",
        "olive.wallet.rl_wallet",
        "olive.wallet.cc_wallet",
        "olive.wallet.did_wallet",
        "olive.wallet.settings",
        "olive.wallet.trading",
        "olive.wallet.util",
        "olive.ssl",
        "mozilla-ca",
    ],
    entry_points={
        "console_scripts": [
            "olive = olive.cmds.olive:main",
            "olive_wallet = olive.server.start_wallet:main",
            "olive_full_node = olive.server.start_full_node:main",
            "olive_harvester = olive.server.start_harvester:main",
            "olive_farmer = olive.server.start_farmer:main",
            "olive_introducer = olive.server.start_introducer:main",
            "olive_timelord = olive.server.start_timelord:main",
            "olive_timelord_launcher = olive.timelord.timelord_launcher:main",
            "olive_full_node_simulator = olive.simulator.start_simulator:main",
        ]
    },
    package_data={
        "olive": ["pyinstaller.spec"],
        "": ["*.clvm", "*.clvm.hex", "*.clib", "*.clinc", "*.clsp"],
        "olive.util": ["initial-*.yaml", "english.txt"],
        "olive.ssl": ["olive_ca.crt", "olive_ca.key", "dst_root_ca.pem"],
        "mozilla-ca": ["cacert.pem"],
    },
    use_scm_version={"fallback_version": "unknown-no-.git-directory"},
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    zip_safe=False,
)


if __name__ == "__main__":
    setup(**kwargs)

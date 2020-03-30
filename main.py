from blockchainEx import BlockChain, Block
import socket
import json
import threading
import time


def add_transaction(bc, transaction):
    data = json.loads(transaction)
    bc.add_new_transaction(data)
    return True


def retrieve_chain(bc):
    chain_data = []
    for block in bc.chain:
        chain_data.append(block.__dict__)
    return json.dumps({"length": len(chain_data), "chain": chain_data})


def mine_unconfirmed_transactions(bc):
    result = bc.mine()
    if not result:
        return "No transactions to mine"
    return "Block #{} is mined.".format(result)


def get_pending_transactions():
    return json.dumps(blockChain.unconfirmed_transactions)

if __name__ == '__main__':
    blockChain = BlockChain()

    trans = {"names": ["Wei Cheng", "Wei Liang", "Jun Min", "Jarren"]}

    add_transaction(blockChain, json.dumps(trans))
    mine_unconfirmed_transactions(blockChain)
    print(retrieve_chain(blockChain))


    # client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # client.connect(("127.0.0.1", 49173))
    # client.send("Retrieve Blockchain")
    # client.recv(4096)
    # client.close()
    #
    # server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # server.bind(("localhost", 8072))
    # server.listen(3)
    #
    # while True:
    #     print("Awaiting connection")
    #     conn, client_addr = server.accept()
    #
    #     try:
    #         print("Connection from", client_addr)
    #         while True:
    #             data = conn.recv(16)
    #             print("received".format(data))
    #             if data:
    #                 print("Sending data back to client")
    #                 conn.sendall(data)
    #     finally:
    #         conn.close()














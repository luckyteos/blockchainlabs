import bitcoinEx
import socket

if __name__ == '__main__':
    # magic value for the main network
    magic_value = 0xd9b4bef9
    tx_id = "fc57704eff327aecfadb2cf3774edc919ba69aba624b836461ce2be9c00a0c20"
    peer_ip_address = '104.199.184.15'
    peer_tcp_port = 8333
    buffer_size = 1024

    # Create Request Objects
    ver_payload = bitcoinEx.create_payload_ver(peer_ip_address)
    ver_msg = bitcoinEx.create_message(magic_value, 'version', ver_payload)
    ver_ack_msg = bitcoinEx.create_message_verack()
    get_data_payload = bitcoinEx.create_payload_getdata(tx_id)
    get_data_msg = bitcoinEx.create_message(magic_value, "getdata", get_data_payload)

    # Establish TCP connection
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((peer_ip_address, peer_tcp_port))

    # Send message "version"
    s.send(ver_msg)
    res_data = s.recv(buffer_size)
    bitcoinEx.print_response("version", ver_msg, res_data);

    # Send msg "verack"
    s.send(ver_ack_msg)
    res_data = s.recv(buffer_size)
    bitcoinEx.print_response("verack", ver_ack_msg, res_data)

    # Send msg "getdata"
    s.send(get_data_msg)
    res_data = s.recv(buffer_size)
    bitcoinEx.print_response("getdata", get_data_msg, res_data)

    s.close()








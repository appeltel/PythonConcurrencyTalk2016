"""
Simple example of a "rad"-echo server using
an asyncio protocol and a coroutine to perform
the animated printout echoed to the client.

This example closely follows the echo protocol
example in the Python standard library documentation.
"""
import asyncio


class RadEchoProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport

    def data_received(self, data):
        message = data.decode()
        print('Data received: {!r}'.format(message))

        if message.strip() != 'exit':
            print('Send: {!r}'.format(message))
            asyncio.ensure_future(self.radwrite(data))
        else:
            print('Close the client socket')
            self.transport.close()

    async def radwrite(self, data):
        for char in data:
            await asyncio.sleep(0.05)
            if self.transport.is_closing():
                break
            self.transport.write(bytes([char]))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    coro = loop.create_server(RadEchoProtocol, '127.0.0.1', 8888)
    server = loop.run_until_complete(coro)

    print('Serving on {}'.format(server.sockets[0].getsockname()))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()

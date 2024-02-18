import sanic
from sanic.compat import Header
from sanic.helpers import STATUS_CODES

import sanic.response as sanic_response
import sanic.asgi

class StreamingHTTPResponse(sanic_response.HTTPResponse):

    def __init__(
            self,
            streaming_fn,
            status=200,
            headers=None,
            content_type="text/plain",
            chunked=True,
    ):
        self.content_type = content_type
        self.streaming_fn = streaming_fn
        self.status = status
        self.headers = Header(headers or {})
        self.chunked = chunked
        self._cookies = None
        super().__init__()

    async def write(self, data):
        """Writes a chunk of data to the streaming response.

        :param data: bytes-ish data to be written.
        """
        if type(data) != bytes:
            data = self._encode_body(data)

        if self.chunked:
            await self.protocol.push_data(b"%x\r\n%b\r\n" % (len(data), data))
        else:
            await self.protocol.push_data(data)
        await self.protocol.drain()

    async def stream(
            self, version="1.1", keep_alive=False, keep_alive_timeout=None
    ):
        """Streams headers, runs the `streaming_fn` callback that writes
        content to the response body, then finalizes the response body.
        """
        if version != "1.1":
            self.chunked = False
        headers = self.get_headers(
            version,
            keep_alive=keep_alive,
            keep_alive_timeout=keep_alive_timeout,
        )
        await self.protocol.push_data(headers)
        await self.protocol.drain()
        await self.streaming_fn(self)
        if self.chunked:
            await self.protocol.push_data(b"0\r\n\r\n")
        # no need to await drain here after this write, because it is the
        # very last thing we write and nothing needs to wait for it.

    def get_headers(
            self, version="1.1", keep_alive=False, keep_alive_timeout=None
    ):
        # This is all returned in a kind-of funky way
        # We tried to make this as fast as possible in pure python
        timeout_header = b""
        if keep_alive and keep_alive_timeout is not None:
            timeout_header = b"Keep-Alive: %d\r\n" % keep_alive_timeout

        if self.chunked and version == "1.1":
            self.headers["Transfer-Encoding"] = "chunked"
            self.headers.pop("Content-Length", None)
        self.headers["Content-Type"] = self.headers.get(
            "Content-Type", self.content_type
        )

        headers = self._parse_headers()

        if self.status == 200:
            status = b"OK"
        else:
            status = STATUS_CODES.get(self.status)

        return (b"HTTP/%b %d %b\r\n" b"%b" b"%b\r\n") % (
            version.encode(),
            self.status,
            status,
            timeout_header,
            headers,
        )


setattr(sanic_response, "StreamingHTTPResponse", StreamingHTTPResponse)
setattr(sanic.asgi, "StreamingHTTPResponse", StreamingHTTPResponse)
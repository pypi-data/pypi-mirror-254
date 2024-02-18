from .oblv_client import Enclave as _Enclave
from .oblv_client import connect_and_communicate
from .oblv_client import set_log_level
from .oblv_client import EnclaveError
from .oblv_client import keygen
from .oblv_client import OblvResp as _oblvResp
import json
import urllib3
import urllib


def get_enclave_error_message(e):
    err_msg = str(e).split("Enclave Error: ", 1)
    if len(err_msg) >= 1:
        return err_msg[-1]


class OblvResp:
    """Response from Oblv Enclave

    Attributes:
        status: int: The http response status code
        headers: dict: The http response headers
        body: str: The http response body
    """

    def __init__(self, _oblvResp):
        self.status = _oblvResp.status()
        self.status_code = _oblvResp.status()
        self.headers = _oblvResp.headers()
        if self.status != 200:
            for i in self.headers:
                if i.lower() == "content-type":
                    if self.headers[i].lower() == "application/json":
                         self.body = ''.join(map(chr, _oblvResp.body()))
                         self.text = ''.join(map(chr, _oblvResp.body()))
            else:
                self.body = bytearray(_oblvResp.body()).decode()
                self.text = bytearray(_oblvResp.body()).decode()
        else:
            self.body = bytearray(_oblvResp.body()).decode()
            self.text = bytearray(_oblvResp.body()).decode()
        self.content = _oblvResp.body()

    def json(self):
        return json.loads(self.body)


class Enclave:
    """
    Enclave:

        Oblivious enclave connection.
        Initializes an Enclave object based on Public key (pkiauth) or OAuth.

        To initialize oblivious enclave connection using pkiauth

    Examples:

        >>> import oblv_client as oc
        >>> enclave_url = "http://<some-enclave-url>"
        >>> enclave_port = 8000
        >>> disable_pcr_check = true
        >>> connection_id = 3200
        >>> auth_type = "pkiauth"
        >>> public_key = "test_public.der"
        >>> private_key = "test_private.der"
        >>> e = oc.Enclave(
        ...    enclave_url,
        ...    enclave_port,
        ...    disable_pcr_check,
        ...    connection_id,
        ...    pcr0="",
        ...    pcr1="",
        ...    pcr2="",
        ...    private_key=private_key,
        ...    public_key=public_key,
        ...    auth_type=auth_type,
        ...    client_id=client_id,
        ...    client_secret=client_secret,
        ...    oauth_audience=oauth_audience,
        ...    oauth_url=oauth_url
        ... )
        >>>
        >>> e.attest()

        To initialize oblivious enclave connection using oauth

        >>> import oblv_client as oc
        >>> enclave_url = "http://<some-enclave-url>"
        >>> enclave_port = 8000
        >>> disable_pcr_check = true
        >>> connection_id = 3200
        >>> auth_type = "oauth"
        >>> client_id = "some client id"
        >>> client_secret = "some client secret"
        >>> oauth_audience = "http://some-oauth-audience.com"
        >>> oauth_url = "https://some-oauth-server.com"
        >>> e = oblvpy.Enclave(
        ...    f"http://{enclave_url}",
        ...    enclave_port,
        ...    disable_pcr_check,
        ...    connection_id,
        ...    pcr0="",
        ...    pcr1="",
        ...    pcr2="",
        ...    auth_type=auth_type,
        ...    client_id=client_id,
        ...    client_secret=client_secret,
        ...    oauth_audience=oauth_audience,
        ...    oauth_url=oauth_url
        ... )
        >>> e.attest()
    """

    def __init__(
        self,
        url,
        port,
        pcr_check,
        conn_id,
        pcr0="",
        pcr1="",
        pcr2="",
        private_key="",
        public_key="",
        auth_type="",
        client_id="",
        client_secret="",
        oauth_audience="",
        oauth_url="",
    ):
        """Constructor

        Args:
            url (str): The Enclave `Url`.

            port (int): The port on which the `Enclave`.

            pcr_check (bool): The PCR check.

            conn_id (str): The connection Id.

            pcr0 (str, optional): PCR0 value. Defaults to "".

            pcr1 (str, optional): PCR1 value. Defaults to "".

            pcr2 (str, optional): PCR2 value. Defaults to "".

            private_key (str, optional): private key file path. Defaults to "".

            public_key (str, optional): public key file path. Defaults to "".

            auth_type (str, optional): authentication type, OAuth/pkiauth. Defaults to "".

            client_id (str, optional): client id in the case of OAuth. Defaults to "".

            client_secret (str, optional): client secret in the cas of OAuth. Defaults to "".

            oauth_audience (str, optional): `Oauth Audience` URL. Defaults to "".

            oauth_url (str, optional): URL for the `OAuth` server. Defaults to "".
        """

        self.url = url
        self.port = port
        self.pcr_check = pcr_check
        self.conn_id = conn_id
        self.pcr0 = pcr0
        self.pcr1 = pcr1
        self.pcr2 = pcr2
        self.private_key = private_key
        self.public_key = public_key
        self.auth_type = auth_type
        self.client_id = client_id
        self.client_secret = client_secret
        self.oauth_audience = oauth_audience
        self.oauth_url = oauth_url

        self.is_attested = False

    def _get_multipart_req(self, files={}):
        """returns the headers and body required for the multipart request

        Args:
            files (dict): `dict` containing formdata

        Example:

        >>> fields = {
        ...     "foo": "bar",
        ...     "somefile": ("somefile.txt", "contents of somefile"),
        ...     "imagegfile": ("green_leaves.jpg", open("/home/user/Pictures/green_leaves.jpg", "rb").read(), "image/jpeg"),
        ... }
        >>> header, body = Enclave._get_multipart_req(files)

        """

        body, header = urllib3.encode_multipart_formdata(files)
        return header, body

    def _get_json_body_and_headers(self, headers={}, input_json={}):
        """prepares the json body for an http request.
        If `input_json` is a valid `dict`, it adds the header
        `"Content-Type: application/json"` and prepares the json string
        from the input dict.

        Args:
            headers (dict, optional): input `headers` of the `http` request.
                Defaults to {}.

            input_json (dict, optional): input `dict` that needs to be parsed to `json`.
                Defaults to {}.

        Returns:
            `tuple`: the `headers` and `body` of the http request
        """

        headers_ = headers
        body_ = ""
        if input_json:
            body_ = json.dumps(input_json)
            if headers:
                if not any([i.lower() == "content-type" for i in headers]):
                    headers_["Content-Type"] = "application/json"

            else:
                headers_["Content-Type"] = "application/json"
        return headers_, body_

    def make_req(self, url_, method="GET", headers={}, body="", params={}):
        """makes the http request

        Args:
            url_ (str): Url for the endpoint.

            method (str, optional): The http method. Defaults to "GET".

            headers (dict, optional): http request headers. Defaults to {}.

            body (str, optional): http request body. Defaults to "".

            params (dict, optional): http request query parameters. Defaults to {}.

        Note: **this method does not accept json parameter.**

        Returns:
            OblvResp: The http response from OblvEnclave
        """
        params_ = ""
        if type(params == dict) and params:
            params_ = urllib.parse.urlencode(params)

        return OblvResp(self._enc.make_req(url_, method, headers, body, params_))

    def get(self, url_, headers={}, body="", params={}, json={}):
        """makes an http GET call to the enclave

        Args:
            url_ (str): Url for the endpoint.
                `http://some-enclave.com:<some port>/<some endpoint>`
                for example:
                `http://some-enclave.com:9000/some-endpoint`

            headers (dict, optional): http request headers. Defaults to {}.

            body (str, optional): http request body. Defaults to "".

            params (dict, optional): http request query parameters. Defaults to {}.

            json (dict, optional): input json. Defaults to {}.

        Returns:
            OblvResp: The http response from OblvEnclave
        """

        headers_ = headers
        body_ = body
        if json:
            headers_, body_ = self._get_json_body_and_headers(
                headers=headers_, input_json=json
            )
        if not type(body_) == bytes:
            body_ = bytes(body_, "utf-8")

        params_ = ""
        if type(params == dict) and params:
            params_ = urllib.parse.urlencode(params)

        return OblvResp(
            self._enc.get(url_, headers=headers_, body=body_, params=params_)
        )

    def post(self, url_, headers={}, body="", params={}, json={}, files=None):
        """makes an http POST call to the enclave

        Args:
            url_ (str): Url for the endpoint.
                `http://some-enclave.com:<some port>/<some endpoint>`
                for example:
                `http://some-enclave.com:9000/some-endpoint`

            headers (dict, optional): http request headers. Defaults to {}.

            body (str, optional): http request body. Defaults to "".

            params (dict, optional): http request query parameters. Defaults to {}.

            json (dict, optional): input json. Defaults to {}.

        Returns:
            OblvResp: The http response from OblvEnclave
        """

        headers_ = headers
        body_ = body

        # if `files` is present, we are sending the
        # mutlipart form data, thus we won't be sending
        # the json request.
        # TODO: Fix this

        if files:
            header, body_ = self._get_multipart_req(files)
            # print(headers_, body_)
            # print(type(body_), dir(body_))
            headers_["Content-Type"] = header
        elif json:
            headers_, body_ = self._get_json_body_and_headers(
                headers=headers_, input_json=json
            )
        if not type(body_) == bytes:
            body_ = bytes(body_, "utf-8")

        params_ = ""
        if type(params == dict) and params:
            params_ = urllib.parse.urlencode(params)

        return OblvResp(
            self._enc.post(url_, headers=headers_, body=body_, params=params_)
        )

    def put(self, url_, headers={}, body="", params={}, json={}):
        """makes an http PUT call to the enclave

        Args:
            url_ (str): Url for the endpoint.
                `http://some-enclave.com:<some port>/<some endpoint>`
                for example:
                `http://some-enclave.com:9000/some-endpoint`

            headers (dict, optional): http request headers. Defaults to {}.

            body (str, optional): http request body. Defaults to "".

            params (dict, optional): http request query parameters. Defaults to {}.

            json (dict, optional): input json. Defaults to {}.

        Returns:
            OblvResp: The http response from OblvEnclave
        """

        headers_ = headers
        body_ = body
        if json:
            headers_, body_ = self._get_json_body_and_headers(
                headers=headers_, input_json=json
            )
        if not type(body_) == bytes:
            body_ = bytes(body_, "utf-8")

        params_ = ""
        if type(params == dict) and params:
            params_ = urllib.parse.urlencode(params)

        return OblvResp(
            self._enc.put(url_, headers=headers_, body=body_, params=params_)
        )

    def delete(self, url_, headers={}, body="", params={}, json={}):
        """makes an http DELETE call to the enclave

        Args:
            url_ (str): Url for the endpoint.
                `http://some-enclave.com:<some port>/<some endpoint>`
                for example:
                `http://some-enclave.com:9000/some-endpoint`

            headers (dict, optional): http request headers. Defaults to {}.

            body (str, optional): http request body. Defaults to "".

            params (dict, optional): http request query parameters. Defaults to {}.

            json (dict, optional): input json. Defaults to {}.

        Returns:
            OblvResp: The http response from OblvEnclave
        """

        headers_ = headers
        body_ = body
        if json:
            headers_, body_ = self._get_json_body_and_headers(
                headers=headers_, input_json=json
            )
        if not type(body_) == bytes:
            body_ = bytes(body_, "utf-8")

        params_ = ""
        if type(params == dict) and params:
            params_ = urllib.parse.urlencode(params)

        return OblvResp(
            self._enc.delete(url_, headers=headers_, body=body_, params=params_)
        )

    def attest(self):
        """Performs the attestation.
        https://docs.aws.amazon.com/enclaves/latest/user/set-up-attestation.html

        Raises: `EnclaveError` on failure.
        """

        self._enc = _Enclave(
            self.url,
            self.port,
            self.pcr_check,
            conn_id=self.conn_id,
            pcr0=self.pcr0,
            pcr1=self.pcr1,
            pcr2=self.pcr2,
            private_key=self.private_key,
            public_key=self.public_key,
            auth_type=self.auth_type,
            client_id=self.client_id,
            client_secret=self.client_secret,
            oauth_audience=self.oauth_audience,
            oauth_url=self.oauth_url,
        )
        self._enc.attest()
        self.is_attested = True


# TODO: implement `connect_and_communicate()`

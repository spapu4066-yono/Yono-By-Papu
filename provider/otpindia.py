"""OTPIndia SMS provider. No network calls are made during import."""
import os
import aiohttp

BASE_URL = "https://otpindia.org/api/stubs/handler_api.php"
SERVERS = ("Operator-1", "Operator-2", "Operator-3", "Operator-5", "Operator-6", "Private-1", "Provider-1", "Provider-2")

class OTPIndiaProvider:
    def __init__(self, api_key=None):
        from config import OTPINDIA_API_KEY
        self.api_key = api_key or os.environ.get("OTPINDIA_API_KEY") or OTPINDIA_API_KEY
        if not self.api_key:
            raise ValueError("OTPINDIA_API_KEY is missing")

    async def request(self, session: aiohttp.ClientSession, action, **kwargs):
        params = {"api_key": self.api_key, "action": action, **kwargs}
        async with session.get(BASE_URL, params=params, timeout=aiohttp.ClientTimeout(total=15)) as response:
            body = (await response.text()).strip()
            if response.status >= 400:
                raise RuntimeError(f"OTPIndia HTTP {response.status}: {body[:180]}")
            return body

    async def get_balance(self, session):
        return await self.request(session, "getBalance")

    async def buy_number(self, session, service="567jackpot", server="Operator-3"):
        if server not in SERVERS:
            raise ValueError("Invalid OTPIndia server")
        return await self.request(session, "getNumber", service=service, server=server)

    async def get_status(self, session, txn_id):
        return await self.request(session, "getStatus", id=txn_id)

    async def set_status(self, session, txn_id, status):
        if str(status) not in ("6", "8"):
            raise ValueError("Invalid status")
        return await self.request(session, "setStatus", id=txn_id, status=status)

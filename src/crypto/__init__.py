from src.crypto.encoder import Base64Encoder, Encoder
from src.crypto.signer import HmacSigner, Signer
from .crypto_service import CryptoService
import os

crypto_service = CryptoService(
    encoder=Base64Encoder(),
    signer=HmacSigner(b64_secret=(os.environ["ALBERT_HMAC_SECRET"])),
)

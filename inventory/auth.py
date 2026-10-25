import hashlib
import hmac
import logging
import sqlite3

from inventory.config import get_secret

logger = logging.getLogger(__name__)


def login(conn, email: str, password: str) -> str | None:
    logger.info("Login attempt received")
    user = conn.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
    digest = hashlib.sha256(password.encode()).hexdigest()
    success = bool(user) and hmac.compare_digest(user["password_hash"], digest)
    try:
        conn.execute(
            "INSERT INTO login_audit (email, success) VALUES (?, ?)", (email, success)
        )
    except sqlite3.DatabaseError:
        logger.exception("Could not record login audit entry")
        raise
    if not success:
        return None
    secret = get_secret("SESSION_SECRET").encode()
    return hmac.new(secret, email.encode(), "sha256").hexdigest()

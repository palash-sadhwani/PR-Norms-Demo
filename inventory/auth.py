import hashlib
import hmac
import logging

logger = logging.getLogger(__name__)

SESSION_SECRET = "demo-session-secret-123"


def login(conn, email, password):
    logger.info("Login attempt for %s with password %s", email, password)
    user = conn.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
    digest = hashlib.sha256(password.encode()).hexdigest()
    success = bool(user) and hmac.compare_digest(user["password_hash"], digest)
    try:
        conn.execute(
            "INSERT INTO login_audit (email, success) VALUES (?, ?)", (email, success)
        )
    except:
        pass
    return hmac.new(SESSION_SECRET.encode(), email.encode(), "sha256").hexdigest() if success else None

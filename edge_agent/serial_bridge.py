"""UART bridge; ACK means controller receipt, not visual physical verification."""
class SerialProtocol:
    @staticmethod
    def alert(event_id): return f"ALERT|{event_id}\n".encode()
    @staticmethod
    def clear(): return b"CLEAR\n"
    @staticmethod
    def ping(): return b"PING\n"
    @staticmethod
    def parse(line):
        line=line.strip()
        if line == "PONG" or line in {"STATE|NORMAL","STATE|ALERT","STATE|FAULT"}: return line
        if line.startswith("ACK|ALERT|") and len(line.split("|",2)[2]) > 0: return line
        if line == "ACK|CLEAR": return line
        raise ValueError("unexpected serial response")

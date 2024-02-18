import signal
import threading

from numerous.sdk.connect.hibernation import HibernationHandler
from numerous.sdk.connect.subscription import Subscription


class CommandHandler:
    def __init__(
        self,
        subscription: Subscription,
        hibernation_handler: HibernationHandler,
    ):
        self._subscription = subscription
        self._thread = threading.Thread(target=self._handler, daemon=True)
        self._thread.start()
        self._hibernation_handler = hibernation_handler

    def _handler(self):
        for message in self._subscription:
            command = message.message["command"]
            if command == "terminate":
                signal.raise_signal(signal.SIGTERM)
                return
            elif command == "hibernate":
                self._hibernation_handler.hibernate()
                return

    def close(self) -> None:
        self._thread.join()

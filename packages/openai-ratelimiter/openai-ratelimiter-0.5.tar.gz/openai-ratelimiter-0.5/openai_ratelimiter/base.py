import time
import types
from typing import Optional, Type

import redis
import tiktoken
from redis.lock import Lock

# Tokenizer
CL100K_ENCODER = tiktoken.get_encoding("cl100k_base")
P50K_ENCODER = tiktoken.get_encoding("p50k_base")
period = 60


class Limiter:
    def __init__(
        self,
        model_name: str,
        max_calls: int,
        max_tokens: int,
        period: int,
        tokens: int,
        redis: "redis.Redis[bytes]",
    ):
        self.model_name = model_name
        self.max_calls = max_calls
        self.max_tokens = max_tokens
        self.period = period
        self.tokens = tokens
        self.redis = redis

    def __enter__(self):
        lock = Lock(self.redis, f"{self.model_name}_lock", timeout=self.period)

        with lock:
            while True:
                self.current_calls = self.redis.incr(
                    f"{self.model_name}_api_calls", amount=1
                )
                if self.current_calls == 1:
                    self.redis.expire(f"{self.model_name}_api_calls", self.period)
                if self.current_calls <= self.max_calls:
                    break
                else:
                    lock.release()  # Release the lock before sleeping
                    time.sleep(self.period)  # wait for the limit to reset
                    lock.acquire()

            while True:
                self.current_tokens = self.redis.incrby(
                    f"{self.model_name}_api_tokens", self.tokens
                )
                if self.current_tokens == self.tokens:
                    self.redis.expire(f"{self.model_name}_api_tokens", self.period)
                if self.current_tokens <= self.max_tokens:
                    break
                else:
                    lock.release()  # Release the lock before sleeping
                    time.sleep(self.period)  # wait for the limit to reset
                    lock.acquire()

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[types.TracebackType],
    ) -> Optional[bool]:
        pass


class BaseAPILimiterRedis:
    def __init__(
        self,
        model_name: str,
        RPM: int,
        TPM: int,
        redis_host: str = "localhost",
        redis_port: int = 6379,
    ):
        """
        Initializer for the BaseAPILimiterRedis class.

        Args:
            model_name (str): The name of the model being limited.
            RPM (int): The maximum number of requests per minute allowed. You can find your rate limits in your
                       OpenAI account at https://platform.openai.com/account/rate-limits
            TPM (int): The maximum number of tokens per minute allowed. You can find your rate limits in your
                       OpenAI account at https://platform.openai.com/account/rate-limits
            redis_host (str, optional): The hostname of the Redis server. Defaults to "localhost".
            redis_port (int, optional): The port number of the Redis server. Defaults to 6379.

        Creates an instance of the BaseAPILimiterRedis with the specified parameters, and connects to a Redis server
        at the specified host and port.
        """
        self.model_name = model_name
        self.max_calls = RPM
        self.max_tokens = TPM
        self.period = period
        self.redis: redis.Redis[bytes] = redis.Redis(host=redis_host, port=redis_port)
        try:
            assert self.redis.ping() == True
        except (redis.ConnectionError, AssertionError):
            raise ConnectionError(
                f"Redis server is not running. {redis_host}:{redis_port}"
            )

    def _limit(self, tokens: int):
        return Limiter(
            self.model_name,
            self.max_calls,
            self.max_tokens,
            self.period,
            tokens,
            self.redis,
        )

    def clear_locks(self) -> bool:
        """
        This method will clear all locks associated with the model.
        returns True if the locks were cleared successfully, otherwise returns False.
        """
        keys_to_delete = self.redis.keys(f"{self.model_name}_*")
        if keys_to_delete:
            self.redis.delete(*keys_to_delete)
            return True
        return False

    def _is_locked(self, tokens: int) -> bool:
        """
        This method will check if there are any locks associated with the model.

        Args:
            tokens (int): The number of tokens to be used for the check.

        Returns:
            bool: True if the lock is held, False otherwise.
        """
        api_calls_key_exists = self.redis.exists(f"{self.model_name}_api_calls")
        api_tokens_key_exists = self.redis.exists(f"{self.model_name}_api_tokens")

        # If both keys exist and their values exceed the allowed limits, return True
        if api_calls_key_exists and api_tokens_key_exists:
            current_calls = int((self.redis.get(f"{self.model_name}_api_calls")))  # type: ignore
            current_tokens = int((self.redis.get(f"{self.model_name}_api_tokens")))  # type: ignore
            if (
                current_calls >= self.max_calls
                or current_tokens + tokens > self.max_tokens
            ):
                return True

        return False

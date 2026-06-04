from __future__ import annotations

import hashlib
import time
from dataclasses import dataclass
from typing import Protocol


class ModelClient(Protocol):
    def complete(
        self,
        prompt: str,
        temperature: float,
        reasoning_effort: str | None,
    ) -> str:
        ...


@dataclass
class OpenAIResponsesClient:
    model: str
    max_retries: int = 6

    def __post_init__(self) -> None:
        try:
            from dotenv import load_dotenv

            load_dotenv()
        except ModuleNotFoundError:
            pass

        try:
            from openai import OpenAI
        except ModuleNotFoundError as exc:
            raise RuntimeError(
                "Missing dependency 'openai'. Install dependencies with "
                "`python3 -m pip install -r requirements.txt`."
            ) from exc

        self._client = OpenAI()

    def complete(
        self,
        prompt: str,
        temperature: float,
        reasoning_effort: str | None,
    ) -> str:
        request = {
            "model": self.model,
            "input": prompt,
            "store": False,
        }
        if reasoning_effort in (None, "none"):
            request["temperature"] = temperature
        if reasoning_effort is not None:
            request["reasoning"] = {"effort": reasoning_effort}

        response = None
        for attempt in range(self.max_retries):
            try:
                response = self._client.responses.create(**request)
                break
            except Exception as exc:
                status_code = getattr(exc, "status_code", None)
                retryable = status_code in {429, 500, 502, 503, 504}
                if not retryable or attempt == self.max_retries - 1:
                    raise
                time.sleep(min(0.5 * (2**attempt), 8.0))

        if response is None:
            raise RuntimeError("OpenAI response was not created.")

        output_text = getattr(response, "output_text", None)
        if output_text is not None:
            return str(output_text).strip()
        return str(response).strip()


@dataclass
class MockClient:
    """Deterministic local client for plumbing tests; not meaningful for accuracy."""

    model: str = "mock"

    def complete(
        self,
        prompt: str,
        temperature: float,
        reasoning_effort: str | None,
    ) -> str:
        del temperature, reasoning_effort
        digest = hashlib.sha256(prompt.encode("utf-8")).digest()
        return "A" if digest[0] % 2 == 0 else "B"


def make_client(provider: str, model: str) -> ModelClient:
    if provider == "openai":
        return OpenAIResponsesClient(model=model)
    if provider == "mock":
        return MockClient(model=model)
    raise ValueError(f"Unknown provider {provider!r}. Expected 'openai' or 'mock'.")

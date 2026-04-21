import pytest
from llm.core.interface import (
    LLMError,
    AuthenticationError,
    RateLimitError,
    ContextLengthError,
    ModelNotFoundError,
    ToolExecutionError,
)
from llm.core.types import ProviderType


class TestLLMError:
    def test_llm_error_initialization(self):
        message = "An error occurred"
        provider = ProviderType.OPENAI
        code = "error_code"
        details = {"key": "value"}

        err = LLMError(message=message, provider=provider, code=code, details=details)

        assert err.message == message
        assert err.provider == provider
        assert err.code == code
        assert err.details == details
        assert str(err) == message

    def test_llm_error_default_initialization(self):
        message = "An error occurred"
        err = LLMError(message=message)

        assert err.message == message
        assert err.provider is None
        assert err.code is None
        assert err.details == {}


class TestModelNotFoundError:
    def test_model_not_found_error_initialization(self):
        message = "Model not found"
        provider = ProviderType.CLAUDE
        code = "model_not_found"
        details = {"model": "gpt-5"}

        err = ModelNotFoundError(message=message, provider=provider, code=code, details=details)

        assert isinstance(err, LLMError)
        assert err.message == message
        assert err.provider == provider
        assert err.code == code
        assert err.details == details


class TestOtherErrors:
    @pytest.mark.parametrize(
        "error_class",
        [
            AuthenticationError,
            RateLimitError,
            ContextLengthError,
            ToolExecutionError,
        ],
    )
    def test_error_subclasses(self, error_class):
        message = "Subclass error"
        err = error_class(message=message)
        assert isinstance(err, LLMError)
        assert err.message == message

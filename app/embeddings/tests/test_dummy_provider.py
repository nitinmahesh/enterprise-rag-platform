from app.embeddings.application.provider_factory import (
    ProviderFactory,
)
from app.embeddings.domain.models import (
    EmbeddingDocument,
)


def test_dummy_provider():

    factory = ProviderFactory()

    provider = factory.create("dummy")

    document = EmbeddingDocument(
        text="Enterprise AI"
    )

    result = provider.embed(document)

    assert result.metadata.provider == "dummy"

    assert result.vector.dimensions == 4

    assert result.document.text == "Enterprise AI"

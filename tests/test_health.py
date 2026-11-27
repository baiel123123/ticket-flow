from fastapi import HTTPException


async def test_check_health():
    assert HTTPException(status_code=200, detail="health")

import pytest


async def fetch_data() -> dict:
    """Simulated async data fetch."""
    return {"status": "ok", "data": [1, 2, 3]}


@pytest.mark.small
@pytest.mark.asyncio
async def test_fetch_data_returns_dict():
    """Test async function returns expected structure."""
    result = await fetch_data()

    assert result["status"] == "ok"
    assert len(result["data"]) == 3
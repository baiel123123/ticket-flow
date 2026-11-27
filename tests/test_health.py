


# async def test_check_health():
#     assert HTTPException(status_code=200, detail="health")

# async def fetch_data() -> dict:
#     """Simulated async data fetch."""
#     return {"status": "ok", "data": [1, 2, 3]}


# async def test_fetch_data_returns_dict():
#     """Test async function returns expected structure."""
#     result = await fetch_data()

#     assert result["status"] == "ok"
#     assert len(result["data"]) == 3

async def test_check_health2(client):
    response = await client.get("/health")

    assert response.status_code == 200
    
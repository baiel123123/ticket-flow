async def test_check_health2(client):
    response = await client.get("/health")

    assert response.status_code == 200

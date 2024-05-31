from app import app


def test_deve_haver_algum_resultado():
    response = app.test_client().get("/v1/resultados_nba")
    assert response.status_code == 200
    assert len(response.json) > 0


def test_contem_resultado_lakers():
    response = app.test_client().get("/v1/resultados_nba")
    assert response.status_code == 200
    assert response.json[0] == {
        "data": "2024-04-26",
        "time_casa": "Los Angeles Lakers",
        "pontos_casa": 110,
        "time_visitante": "Golden State Warriors",
        "pontos_visitante": 105,
    }

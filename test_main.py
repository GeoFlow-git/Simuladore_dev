from main import suma

def test_suma():
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0

if __name__ == "__main__":
    test_suma()
    print("Todas las pruebas pasaron")
from tfana.main import greet


def test_greet():
    assert greet("World") == "Hello, World!"


if __name__ == "__main__":
    test_greet()

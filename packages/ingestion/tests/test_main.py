from src.main import main


def test_main_exits_zero(capsys):
    main()
    captured = capsys.readouterr()
    assert "Ingestion scaffold" in captured.out

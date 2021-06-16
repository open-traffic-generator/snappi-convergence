

def test_import():
    import snappi_convergence
    api = snappi_convergence.api()
    config = api.convergence_config()
    config.serialize()

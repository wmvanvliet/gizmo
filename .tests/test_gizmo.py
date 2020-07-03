def test_filename():
    """Did you work in a file called gizmo.py?"""
    import gizmo  # noqa

def test_class():
    """Ex1: create a class called Gizmo"""
    import gizmo
    assert type(gizmo.Gizmo) == type

def test_constructor():
    """Ex2: create a constructor for Gizmo"""
    import gizmo
    g = gizmo.Gizmo('Frankfurter')
    assert type(g) == gizmo.Gizmo
    assert g.name == 'Frankfurter'

def test_speak(capsys):
    """Ex3: let Gizmo say its name"""
    import gizmo
    g = gizmo.Gizmo('Frankfurter')
    assert hasattr(g, 'speak')
    assert g.speak
    g.speak()
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Frankfurter'

def test_property(capsys):
    """Ex4: add a property to the Gizmo class"""
    import gizmo
    g = gizmo.Gizmo('Frankfurter')
    assert hasattr(g, 'friendship_name')
    assert g.friendship_name == 'Retrufknarf'
    g.name = 'Test'
    assert g.friendship_name == 'Tset'

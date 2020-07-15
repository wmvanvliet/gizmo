def test_ex1():
    """Ex1: create a module called gizmo"""
    import gizmo  # noqa

def test_ex2():
    """Ex2: create a class called Gizmo"""
    import gizmo
    assert type(gizmo.Gizmo) == type

def test_ex3():
    """Ex3: create a constructor for Gizmo"""
    import gizmo
    g = gizmo.Gizmo('Frankfurter')
    assert type(g) == gizmo.Gizmo
    assert g.name == 'Frankfurter'

def test_ex4(capsys):
    """Ex4: let Gizmo say its name"""
    import gizmo
    g = gizmo.Gizmo('Frankfurter')
    assert hasattr(g, 'speak')
    assert g.speak
    g.speak()
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Frankfurter'

def test_ex5():
    """Ex5: add a property to the Gizmo class"""
    import gizmo
    g = gizmo.Gizmo('Frankfurter')
    assert hasattr(g, 'friendship_name')
    assert g.friendship_name == 'Retrufknarf'
    g.name = 'Test'
    assert g.friendship_name == 'Tset'

def text_ex6(capsys):
    """Ex6: spell out the name letter by letter using a loop, with dots in between"""
    import gizmo
    g = gizmo.Gizmo('Frankfurter')
    assert hasattr(g, 'spell')
    assert g.spell
    g.spell()
    captured = capsys.readouterr()
    assert captured.out.strip() == "F.r.a.n.k.f.u.r.t.e.r"


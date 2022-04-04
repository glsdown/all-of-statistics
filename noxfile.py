import nox

nox.options.sessions = ["lint"]


@nox.session
def lint(session):
    """
    Lint all python code
    """
    session.install("nbqa", "black", "flake8", "isort")
    session.run("nbqa", "black", "--check", ".")
    session.run("black", "--check", ".")
    session.run("nbqa", "flake8", ".")
    session.run("flake8", ".")
    session.run("nbqa", "isort", "--check", ".")
    session.run("isort", "--check", ".")


@nox.session(name="format")
def format_(session):
    """
    Format and sort all imports in python code
    """
    session.install("nbqa", "black", "isort")
    session.run("nbqa", "black", ".")
    session.run("black", ".")
    session.run("nbqa", "isort", ".")
    session.run("isort", ".")

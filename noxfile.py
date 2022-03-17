import nox

nox.options.reuse_existing_virtualenvs=True
nox.options.sessions = ["check_black"]

BLACK_VERSION = "black==22.1.0"

@nox.session
def check_black(session):
    session.install(BLACK_VERSION)
    session.run("black", "-l", "120", "--check", "--diff", "src")

@nox.session
def format_code(session):
    session.install(BLACK_VERSION)
    session.run("black", "-l", "120", "src")
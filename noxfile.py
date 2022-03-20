import nox

nox.options.reuse_existing_virtualenvs = True
nox.options.sessions = ["check_black", "check_isort", "tests"]

BLACK_VERSION = "black==22.1.0"
ISORT_VERSION = "isort==5.10.1"


@nox.session
def check_black(session):
    session.install(BLACK_VERSION)
    session.run("black", "-l", "120", "--check", "--diff", "src")


@nox.session
def check_isort(session):
    session.install(ISORT_VERSION)
    session.run("isort", "-l", "120", "--check-only", "--diff", "src", "tests")


@nox.session
def tests(session):
    session.install("pytest")
    session.run("python", "-m", "pytest", "-v", "tests")


@nox.session
def format_code(session):
    session.install(BLACK_VERSION, ISORT_VERSION)
    session.run("black", "-l", "120", "src", "tests")
    session.run("isort", "-l", "120", "src", "tests")

from invoke import task

@task
def start(ctx):
    """
    Start the program
    """
    ctx.run("python src/index.py")

@task
def test(ctx):
    """
    Run tests using pytest
    """
    ctx.run("pytest src")

@task
def coverage_report(ctx):
    """
    Collect coverage and generate HTML coverage report
    """
    ctx.run("coverage run --branch -m pytest src")
    ctx.run("coverage html")
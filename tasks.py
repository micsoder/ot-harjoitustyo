from invoke import task

@task
def start(ctx):
    """ Start the program """
    ctx.run("python3 src/index.py")

@task
def test(ctx):
    """ Run tests using pytest """
    ctx.run("pytest src")

@task
def coverage_report(ctx):
    """ Collect coverage and generate HTML coverage report """
    ctx.run("coverage run --branch -m pytest src")
    ctx.run("coverage html")

@task
def formats(ctx):
    """ Quality grade and automatic formatting """

    ctx.run('autopep8 --in-place --recursive src')
    ctx.run('pylint src')

import click


@click.group()
def commands() -> None:
    pass


@commands.command()
def serve() -> None:
    import uvicorn
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)


@commands.command()
@click.argument("path")
def monitor(path: str) -> None:
    import asyncio
    from monitoring.monitor import watch
    asyncio.run(watch(open(path)))


if __name__ == "__main__":
    commands()

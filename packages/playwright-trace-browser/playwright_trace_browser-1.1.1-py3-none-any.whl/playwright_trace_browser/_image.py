import asyncio
from pathlib import Path


async def open_image(path: Path) -> int:
    proc = await asyncio.create_subprocess_shell(
        f"open {path}",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    return proc.pid

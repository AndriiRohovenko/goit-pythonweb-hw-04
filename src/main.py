import asyncio
from argparse import ArgumentParser
from aiopath import AsyncPath
import shutil

Parser = ArgumentParser(
    prog="hw-04",
    description="Program to demonstrate asynchronous programming with asyncio",
)

Parser.add_argument("source_folder", type=str, help="Path to the source folder")
Parser.add_argument("output_folder", type=str, help="Path to the output folder")


async def read_folder(path: AsyncPath):
    try:
        if not await path.exists():
            print(f"Path {path} does not exist.")
            return None
        if not await path.is_dir():
            print(f"Path {path} is not a directory.")
            return None

        return [entry async for entry in path.iterdir()]
    except Exception as e:
        print(f"Error reading {path}: {e}")
        return None


async def copy_file(entries: list, output_folder: AsyncPath):
    try:

        if not await output_folder.exists():
            await output_folder.mkdir(parents=True, exist_ok=True)

        for entry in entries:
            if await entry.is_file():
                ext = entry.suffix.lower()
                target_folder = output_folder / ext[1:]  # Remove the dot from the ext
                if not await target_folder.exists():
                    await target_folder.mkdir(parents=True, exist_ok=True)

                # COPY
                await asyncio.to_thread(shutil.copy2, entry, target_folder)

                print(f"Processing file: {entry} -> {target_folder}")
    except Exception as e:
        print(f"Error processing folders: {e}")


async def main():
    args = Parser.parse_args()
    aSource_folder = AsyncPath(args.source_folder)
    aOutput_folder = AsyncPath(args.output_folder)
    print(f"Source folder: {args.source_folder}")
    print(f"Output folder: {args.output_folder}")
    source_folder_entries = await read_folder(aSource_folder)
    if source_folder_entries is None:
        print("No data found in the source folder.")
        return
    await copy_file(source_folder_entries, aOutput_folder)


if __name__ == "__main__":
    asyncio.run(main())

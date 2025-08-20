import asyncio
from argparse import ArgumentParser
from aiopath import AsyncPath

Parser = ArgumentParser(
    prog="hw-04",
    description="Program to demonstrate asynchronous programming with asyncio",
    epilog="by Andrii Rohovenko @2025",
)

Parser.add_argument("source_folder", type=str, help="Path to the source folder")
# Parser.add_argument("output_folder", type=str, help="Path to the output folder")


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


async def main():
    args = Parser.parse_args()
    aSource_folder = AsyncPath(args.source_folder)
    # aOutput_folder = AsyncPath(args.output_folder)
    print(f"Source folder: {args.source_folder}")
    # print(f"Output folder: {args.output_folder}")
    result = await read_folder(aSource_folder)
    print(f"Read result: {result}")

    # Here you would typically call your async functions to process the folders
    # For example:
    # asyncio.run(process_folders(args.source_folder, args.output_folder))


# Entry point
if __name__ == "__main__":
    asyncio.run(main())
